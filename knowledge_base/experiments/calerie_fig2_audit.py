#!/usr/bin/env python3
"""Summarize arm/visit ROW COUNTS in a locally supplied Fig. 2 source CSV.

Input: Waziry et al., 2023, Nature Aging, Figure 2 left column source data:
https://static-content.springer.com/esm/art%3A10.1038%2Fs43587-022-00357-y/MediaObjects/43587_2022_357_MOESM5_ESM.csv
No internet access or file download is performed. This CSV does not contain a
participant identifier in the observed header. Do not infer participant linkage
from row order. No participant-level records or identifiers are printed.

This only tabulates rows, not paired individuals, original mixed-model results,
trial randomization, or endpoint effects. Source contents and terms should be
verified independently by a qualified researcher before use.
"""
import argparse
import csv
import hashlib
import io
import sys
from collections import Counter
from pathlib import Path

REQUIRED = {"CR", "fu", "pace_br", "pcphenoage_br", "pcgrimage_br"}
ARMS = {"CR", "AL"}
VISITS = {"Baseline", "12mo", "24mo"}


def summarize(data: bytes):
    digest = hashlib.sha256(data).hexdigest()
    stream = io.StringIO(data.decode("utf-8-sig"), newline="")
    reader = csv.DictReader(stream)
    if reader.fieldnames is None or len(reader.fieldnames) != len(set(reader.fieldnames)):
        raise ValueError("missing or duplicate CSV header")
    if set(reader.fieldnames) != REQUIRED:
        raise ValueError("unexpected columns; inspect source schema before analysis")
    totals = Counter()
    missing = Counter()
    for row in reader:
        if None in row or any(v is None for v in row.values()):
            raise ValueError("malformed row")
        arm, visit = row["CR"].strip(), row["fu"].strip()
        if arm not in ARMS or visit not in VISITS:
            raise ValueError("unexpected arm or visit")
        totals[(arm, visit)] += 1
        for clock in ("pace_br", "pcphenoage_br", "pcgrimage_br"):
            value = row[clock].strip()
            if not value or value.upper() in {"NA", "NAN", "."}:
                missing[(arm, visit, clock)] += 1
            else:
                float(value)  # validate numeric fields without reporting records
    if not totals:
        raise ValueError("no data rows")
    return digest, totals, missing


def test_synthetic():
    fixture = ("CR,fu,pace_br,pcphenoage_br,pcgrimage_br\n"
               "CR,Baseline,1,2,3\nCR,12mo,0.9,2.1,\nAL,Baseline,1,2,3\n").encode()
    _, counts, missing = summarize(fixture)
    assert counts[("CR", "Baseline")] == 1 and counts[("AL", "Baseline")] == 1
    assert missing[("CR", "12mo", "pcgrimage_br")] == 1
    for malformed in (b"x,y\n1,2\n", fixture + b"UNKNOWN,12mo,1,2,3\n"):
        try:
            summarize(malformed)
        except ValueError:
            pass
        else:
            raise AssertionError("malformed input accepted")
    print("Synthetic schema, row-count, missing-value, rejection tests passed.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", nargs="?", type=Path, help="locally supplied published source CSV")
    args = parser.parse_args()
    test_synthetic()
    if args.csv is None:
        print("No source file provided; only synthetic tests were run.")
        return
    try:
        digest, counts, missing = summarize(args.csv.read_bytes())
    except (ValueError, OSError, UnicodeError) as exc:
        print(f"Cannot audit input: {exc}", file=sys.stderr)
        raise SystemExit(2)
    print(f"SHA-256 of supplied local bytes: {digest}")
    print("Rows by arm/visit (not verified unique people):")
    for arm in ("CR", "AL"):
        for visit in ("Baseline", "12mo", "24mo"):
            print(f"  {arm:2} {visit:8} {counts[(arm, visit)]:3}")
    print("Missing clock values by arm/visit:")
    for arm in ("CR", "AL"):
        for visit in ("Baseline", "12mo", "24mo"):
            print(f"  {arm:2} {visit:8} " + " ".join(
                f"{name}={missing[(arm, visit, name)]}"
                for name in ("pace_br", "pcphenoage_br", "pcgrimage_br")
            ))
    print("No participant ID: row counts alone cannot establish complete cases or X31.")


if __name__ == "__main__":
    main()
