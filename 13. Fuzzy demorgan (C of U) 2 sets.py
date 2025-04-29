def fuzzy_complement(set_a: dict[str, float], universe: set[str]):
    return {x: 1 - set_a.get(x, 0) for x in universe}

def fuzzy_union(set_a: dict[str, float], set_b: dict[str, float], universe: set[str]):
    return {x: max(set_a.get(x, 0), set_b.get(x, 0)) for x in universe}

def fuzzy_intersection(set_a: dict[str, float], set_b: dict[str, float], universe: set[str]):
    return {x: min(set_a.get(x, 0), set_b.get(x, 0)) for x in universe}

def print_fuzzy_set(label: str, fuzzy_set: dict[str, float]):
    print(label)
    for key in sorted(fuzzy_set.keys()):
        if fuzzy_set[key] > 0:
            print(f"{key}: {fuzzy_set[key]:.2f}", end=" ")
    print()

set_a = {"A": 0.2, "B": 0.5, "C": 0.8}
set_b = {"B": 0.3, "C": 0.6, "D": 0.9}
universe = set(set_a.keys()).union(set(set_b.keys()))

complement_a = fuzzy_complement(set_a, universe)
print_fuzzy_set("complement set A: ", complement_a)

complement_b = fuzzy_complement(set_b, universe)
print_fuzzy_set("complement set B: ", complement_b)

union_ab = fuzzy_union(set_a, set_b, universe)
print_fuzzy_set("union set AB: ", union_ab)

intersection_ab = fuzzy_intersection(set_a, set_b, universe)
print_fuzzy_set("intersection set AB: ", intersection_ab)

# (A u B)' = A' n B'
comp_of_union = fuzzy_complement(union_ab, universe)
print_fuzzy_set("complement of union set AB: ", comp_of_union)

comp_of_intersections = fuzzy_intersection(complement_a, complement_b, universe)
print_fuzzy_set("intersection of complements set A and B: ", comp_of_intersections)