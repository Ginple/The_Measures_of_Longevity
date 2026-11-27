#!/usr/bin/env python3
"""Conditional set-consistency check of counts transcribed from CALERIE text.

This is not participant-level data, a replication, or evidence about which
reported number is correct. The logic applies only if the input sets have the
same group, baseline measurement, and definition of eligible participants.
"""


def intersection_bounds(universe: int, first: int, second: int) -> tuple[int, int]:
    if not (0 <= first <= universe and 0 <= second <= universe):
        raise ValueError("each time-point count must be within the universe")
    return max(0, first + second - universe), min(first, second)


def exact_partition_if_union(first: int, second: int, union: int) -> tuple[int, int, int]:
    """Counts in first only, second only, both, if the union is exactly known."""
    if not all(isinstance(x, int) and not isinstance(x, bool) for x in (first, second, union)):
        raise ValueError("counts must be integers")
    if not (0 <= first <= union and 0 <= second <= union and union <= first + second):
        raise ValueError("invalid union or set counts")
    both = first + second - union
    return first - both, second - both, both


def report(label: str, universe: int, first: int, second: int, reported: int) -> None:
    lower, upper = intersection_bounds(universe, first, second)
    compatible = lower <= reported <= upper
    print(
        f"{label}: universe={universe}, 12m={first}, 24m={second}, "
        f"intersection bounds=[{lower},{upper}], reported={reported}, "
        f"compatible under common-set assumptions={compatible}"
    )


def main() -> None:
    assert intersection_bounds(128, 125, 117) == (114, 117)
    assert intersection_bounds(69, 66, 68) == (65, 66)
    assert intersection_bounds(197, 191, 185) == (179, 185)
    assert intersection_bounds(10, 6, 5) == (1, 5)
    print("Conditional consistency check; counts are published text, not raw data.")
    report("restriction", 128, 125, 117, 105)
    report("control", 69, 66, 68, 59)
    report("control S1 conditional", 69, 65, 68, 59)
    report("combined", 197, 191, 185, 164)
    print("If and only if the quoted universe is exactly the union, partitions are:")
    for label, n, a, b in [("restriction", 128, 125, 117), ("control", 69, 66, 68),
                           ("control S1 conditional", 69, 65, 68)]:
        first_only, second_only, both = exact_partition_if_union(a, b, n)
        print(f"{label}: first-only={first_only}, second-only={second_only}, both={both}")
    report("synthetic consistent example", 10, 6, 5, 2)
    print("Incompatibility is not a finding about which count is wrong or the trial effect.")


if __name__ == "__main__":
    main()
