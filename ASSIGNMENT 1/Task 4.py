# ...existing code...
# Recursive and iterative factorial implementations

def factorial_recursive(n: int) -> int:
    """Return n! using recursion. n must be a non-negative integer."""
    if not isinstance(n, int):
        raise TypeError("factorial_recursive() expects an integer")
    if n < 0:
        raise ValueError("factorial_recursive() expects a non-negative integer")
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n: int) -> int:
    """Return n! using an iterative loop. n must be a non-negative integer."""
    if not isinstance(n, int):
        raise TypeError("factorial_iterative() expects an integer")
    if n < 0:
        raise ValueError("factorial_iterative() expects a non-negative integer")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    try:
        while True:
            s = input("Enter a non-negative integer (or 'q' to quit): ").strip()
            if s.lower() == "q":
                print("Exiting.")
                break
            try:
                n = int(s)
            except ValueError:
                print("Invalid input: please enter a whole non-negative integer.")
                continue
            if n < 0:
                print("Please enter a non-negative integer.")
                continue

            method = input("Choose method — recursive (r) or iterative (i) [default i]: ").strip().lower()
            if method == "r":
                try:
                    result = factorial_recursive(n)
                except RecursionError:
                    print("RecursionError: n is too large for recursive computation. Use iterative method.")
                    continue
            else:
                result = factorial_iterative(n)

            print(f"{n}! = {result}")
    except (EOFError, KeyboardInterrupt):
        print("\nExiting.")
# ...existing code...