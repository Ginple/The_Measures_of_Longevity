"""Two entirely synthetic randomized trials with identical observed margins.

Demonstrates non-identification of an always-survivor effect, not real data.
The constructed assignments are balanced within each latent type for clarity;
no actual study can stratify assignment by these unobservable potential outcomes.
Scores are binary and undefined after death. This is not a power simulation.
"""
from dataclasses import dataclass
import json


@dataclass(frozen=True)
class Person:
    treatment: int
    survives0: bool
    survives1: bool
    y0: int | None
    y1: int | None


def add_type(people, n, survives0, survives1, y0, y1):
    if n <= 0 or n % 2:
        raise ValueError('synthetic type count must be positive and even')
    for treatment in (0, 1):
        people.extend(Person(treatment, survives0, survives1, y0, y1) for _ in range(n // 2))


def population(world):
    people = []
    if world == 'A':
        add_type(people, 100, True, True, 1, 1)
        add_type(people, 50, False, True, None, 0)
        add_type(people, 50, True, False, 0, None)
    elif world == 'B':
        add_type(people, 50, True, True, 1, 1)
        add_type(people, 50, True, True, 0, 1)
        add_type(people, 50, False, True, None, 0)
        add_type(people, 50, True, False, 1, None)
    else:
        raise ValueError('world must be A or B')
    return people


def report(world):
    people = population(world)
    arms = {}
    for arm in (0, 1):
        group = [p for p in people if p.treatment == arm]
        survivors = [p for p in group if (p.survives1 if arm else p.survives0)]
        scores = [p.y1 if arm else p.y0 for p in survivors]
        arms[str(arm)] = {'n': len(group), 'survivors': len(survivors),
                          'survivor_score_1': sum(scores),
                          'mean_among_survivors': sum(scores) / len(survivors),
                          # This explicit binary endpoint is not the function score.
                          'alive_and_score_1': sum(scores) / len(group)}
    always = [p for p in people if p.survives0 and p.survives1]
    sace = sum(p.y1 - p.y0 for p in always) / len(always)
    return {'world': world, 'observed_arms': arms, 'latent_always_survivors': len(always),
            'latent_sace': sace,
            'composite_treatment_minus_control': arms['1']['alive_and_score_1'] - arms['0']['alive_and_score_1']}


if __name__ == '__main__':
    print(json.dumps({'classification': 'SYNTHETIC; latent potential outcomes are not observable in real trials',
                      'worlds': [report('A'), report('B')]}, indent=2))
