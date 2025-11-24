# ...existing code...
from typing import List, Sequence
from time import perf_counter
from statistics import mean

def reverse_loop(lst: Sequence) -> List:
    """Return a new list by iterating from end to start."""
    out = []
    for i in range(len(lst) - 1, -1, -1):
        out.append(lst[i])
    return out

def reverse_slicing(lst: Sequence) -> List:
    """Return a new list using slicing (lst[::-1])."""
    return lst[::-1]

def reverse_reversed(lst: Sequence) -> List:
    """Return a new list using the built-in reversed() iterator."""
    return list(reversed(lst))

def reverse_inplace_two_pointer(lst: Sequence) -> List:
    """
    Reverse using two-pointer swaps but operate on a copy so input isn't mutated.
    Returns the reversed copy.
    """
    out = list(lst)
    i, j = 0, len(out) - 1
    while i < j:
        out[i], out[j] = out[j], out[i]
        i += 1
        j -= 1
    return out

def run_tests():
    implementations = {
        "loop": reverse_loop,
        "slicing": reverse_slicing,
        "reversed_builtin": reverse_reversed,
        "inplace_two_pointer": reverse_inplace_two_pointer,
    }

    test_cases = [
        [],                 # empty
        [1],                # single element
        [1, 2],             # two elements
        [1, 2, 3, 4, 5],    # odd length
        [10, 20, 30, 40],   # even length
        list("abcde"),      # characters
    ]

    for name, fn in implementations.items():
        for case in test_cases:
            original = case.copy()
            expected = list(reversed(case))
            result = fn(case)
            assert result == expected, f"{name} failed for {case}: got {result}, expected {expected}"
            # ensure original not mutated (all implementations return new lists)
            assert case == original, f"{name} mutated input for {case}"
    return implementations

def benchmark(implementations: dict, sizes=(1000, 5000, 20000), repeats=5):
    timings = {name: [] for name in implementations}
    for n in sizes:
        data = list(range(n))
        for name, fn in implementations.items():
            total = 0.0
            for _ in range(repeats):
                arg = data.copy()
                t0 = perf_counter()
                fn(arg)
                t1 = perf_counter()
                total += (t1 - t0)
            avg = total / repeats
            timings[name].append((n, avg))
    # compute overall average time across sizes for each implementation
    overall = {name: mean(t for _, t in lst) for name, lst in timings.items()}
    # print results
    print("Benchmark results (average seconds):")
    for name, lst in timings.items():
        line = f"{name:20}: " + ", ".join(f"{n}:{t:.6f}" for n, t in lst)
        print(line)
    fastest = min(overall, key=overall.get)
    print(f"\nFastest overall: {fastest} (avg {overall[fastest]:.6f} s over sizes {sizes})")
    return timings, overall

if __name__ == "__main__":
    implementations = run_tests()
    print("All tests passed for all implementations.")
    # Warm-up quick sanity output
    sample = [1, 2, 3, 4, 5]
    for name, fn in implementations.items():
        print(f"{name:20}: {fn(sample)}")
    # Run benchmark and show fastest
    benchmark(implementations, sizes=(1000, 5000, 20000), repeats=5)
# ...existing code...