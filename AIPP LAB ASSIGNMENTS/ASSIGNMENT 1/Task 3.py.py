# ...existing code...
# Function to reverse a string
def reverse_string(s: str) -> str:
    """Return the reverse of s. Raises TypeError if s is not a str."""
    if not isinstance(s, str):
        raise TypeError("reverse_string() expects a string")
    # use reversed() to handle large strings efficiently
    return ''.join(reversed(s))

if __name__ == "__main__":
    try:
        while True:
            s = input("Enter a string (or 'q' to quit): ")
            if s.strip().lower() == "q":
                print("Exiting.")
                break
            print("Reversed:", reverse_string(s))
    except (EOFError, KeyboardInterrupt):
        print("\nExiting.")
# ...existing code...