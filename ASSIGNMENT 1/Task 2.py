# ...existing code...
def is_prime(n: int) -> bool:
    """Return True if n is a prime number (n >= 2), otherwise False."""
    if not isinstance(n, int):
        raise TypeError("is_prime() expects an integer")
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    limit = int(n**0.5) + 1
    while i <= limit:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    try:
        while True:
            s = input("Enter an integer (or 'q' to quit): ").strip()
            if s.lower() == "q":
                print("Exiting.")
                break
            try:
                num = int(s)
            except ValueError:
                print("Invalid input: please enter a whole integer (e.g. 17).")
                continue
            if is_prime(num):
                print(f"{num} is prime.")
            else:
                print(f"{num} is not prime.")
    except (EOFError, KeyboardInterrupt):
        print("\nExiting.")
# ...existing code...