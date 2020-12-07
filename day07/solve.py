#!/usr/bin/env python3
from collections import deque
from functools import partial


def color_and_n(bag_spec):
    # gets "\d+ (\w+ \w+) bags?\.?" with digit being num and two words color
    # remove trailing ',' or 's' so we can slice off r" bags?\.?" using indexing
    # use split(maxsplit=1) so it splits off num from two word color
    n, color = bag_spec.rstrip('s.')[:-4].split(maxsplit=1)
    return (color, n)


obag_to_ibag_to_ns = {}
with open("input.txt", "r") as ifile:
    for line in ifile:
        obag, bag_specs = line.strip().split(" bags contain ")
        obag_to_ibag_to_ns[obag] = dict(color_and_n(bag_spec) for bag_spec in bag_specs.split(", "))

def obag_holds_ibag(obag_spec, ibag):
    return [obag for obag, ibag_to_ns in obag_spec.items() if ibag in ibag_to_ns]

# Pt 1
bags_that_hold = partial(obag_holds_ibag, obag_to_ibag_to_ns)
bags_hold_gold = deque(bags_that_hold("shiny gold"))
accumulator = []
while bags_hold_gold:
    bag = bags_hold_gold.popleft()
    accumulator.append(bag)
    bags_hold_gold.extend(bags_that_hold(bag))

print("Part 1 answer: ", len(set(accumulator)))

