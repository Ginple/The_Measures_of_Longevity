"""A marker that predicts an outcome without controlling it.

SYNTHETIC. No real data. Exact arithmetic with fractions.
Purpose (English chapter 3, section 3): show that a marker can predict an event well while changing the
marker changes nothing, because both depend on a hidden common cause.

Population of 1000 people. A hidden condition Z is present in 300 of them.
- The marker is high in 80 percent of people with Z and in 20 percent of people without Z.
- The event happens to 40 percent of people with Z and to 10 percent of people without Z,
  whatever their marker (the marker has no effect of its own).
Intervention: a perfectly safe treatment sets everyone's marker to low. Because the marker has no effect,
the expected number of events is unchanged.
"""
from fractions import Fraction as F
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent / 'evidence/CONFOUNDED_MARKER_SYNTHETIC_output.json'
N, NZ = 1000, 300
P_HIGH = {True: F(8, 10), False: F(2, 10)}
P_EVENT = {True: F(4, 10), False: F(1, 10)}


def build():
    groups = {}
    for z in (True, False):
        n = NZ if z else N - NZ
        for high in (True, False):
            people = n * (P_HIGH[z] if high else 1 - P_HIGH[z])
            groups[(z, high)] = (people, people * P_EVENT[z])
    def total(high):
        people = sum(g[0] for k, g in groups.items() if k[1] == high)
        events = sum(g[1] for k, g in groups.items() if k[1] == high)
        return people, events
    hp, he = total(True)
    lp, le = total(False)
    risk_high, risk_low = he / hp, le / lp
    events_before = he + le
    events_after = sum(n * P_EVENT[z] for z, n in ((True, NZ), (False, N - NZ)))
    return dict(
        nature='SYNTHETIC illustration; no real data; exact fractions',
        script='knowledge_base/pilots/ch03_four_links_en/confounded_marker.py',
        people_marker_high=int(hp), events_marker_high=int(he),
        people_marker_low=int(lp), events_marker_low=int(le),
        risk_marker_high=f'{float(risk_high):.3f}', risk_marker_low=f'{float(risk_low):.3f}',
        risk_ratio_high_vs_low=f'{float(risk_high / risk_low):.2f}',
        events_without_treatment=int(events_before), events_with_marker_set_low=int(events_after))


if __name__ == '__main__':
    data = build()
    OUT.write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(data, indent=2))
