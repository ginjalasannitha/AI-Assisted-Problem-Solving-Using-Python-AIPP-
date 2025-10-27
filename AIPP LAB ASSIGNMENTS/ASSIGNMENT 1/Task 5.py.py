# ...existing code...
import re

def find_max_iterative(nums):
    """Return the largest number in nums.
    Raises ValueError if nums is empty. Expects an iterable of comparable items.
    O(n) time, O(1) extra space.
    """
    if not nums:
        raise ValueError("find_max_iterative() expects a non-empty iterable")
    it = iter(nums)
    try:
        maximum = next(it)
    except StopIteration:
        raise ValueError("find_max_iterative() expects a non-empty iterable")
    for x in it:
        if x > maximum:
            maximum = x
    return maximum

def find_max_builtin(nums):
    """Return the largest number using Python's built-in max()."""
    return max(nums)

if __name__ == "__main__":
    try:
        while True:
            s = input("Enter numbers separated by space or comma (or 'q' to quit): ").strip()
            if s.lower() == "q":
                print("Exiting.")
                break
            if not s:
                print("No input provided.")
                continue

            tokens = [t for t in re.split(r"[\s,]+", s) if t]
            nums = []
            for t in tokens:
                try:
                    # prefer int when possible, fallback to float
                    if '.' in t or 'e' in t.lower():
                        nums.append(float(t))
                    else:
                        nums.append(int(t))
                except ValueError:
                    print(f"Ignoring invalid token: {t}")

            if not nums:
                print("No valid numbers entered.")
                continue

            try:
                print("iterative:", find_max_iterative(nums))
                print("builtin:   ", find_max_builtin(nums))
            except Exception as e:
                print("Error:", e)
    except (EOFError, KeyboardInterrupt):
        print("\nExiting.")
# ...existing code...