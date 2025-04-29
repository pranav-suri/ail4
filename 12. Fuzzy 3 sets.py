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
set_c = {"C": 0.4, "D": 0.7, "E": 0.1}
universe = set(set_a.keys()).union(set(set_b.keys())).union(set(set_c.keys()))

complement_a = fuzzy_complement(set_a, universe)
print_fuzzy_set("complement set A: ", complement_a)

complement_b = fuzzy_complement(set_b, universe)
print_fuzzy_set("complement set B: ", complement_b)

union_ab = fuzzy_union(set_a, set_b, universe)
print_fuzzy_set("union set AB: ", union_ab)

union_abc = fuzzy_union(union_ab, set_c, universe)
print_fuzzy_set("union set ABC: ", union_abc)

intersection_ab = fuzzy_intersection(set_a, set_b, universe)
print_fuzzy_set("intersection set AB: ", intersection_ab)

intersection_abc = fuzzy_intersection(intersection_ab, set_c, universe)
print_fuzzy_set("intersection set ABC: ", intersection_abc)

