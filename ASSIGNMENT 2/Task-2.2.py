# ...existing code...
def is_palindrome(s: str, *, ignore_case: bool = True, ignore_non_alnum: bool = True) -> bool:
    """
    Return True if string s is a palindrome.
    Options:
      - ignore_case: compare case-insensitively
      - ignore_non_alnum: ignore non-alphanumeric characters (spaces, punctuation)
    """
    if ignore_non_alnum:
        filtered = ''.join(ch for ch in s if ch.isalnum())
    else:
        filtered = s
    if ignore_case:
        filtered = filtered.lower()
    return filtered == filtered[::-1]
# Demo checks (auto-run)
_demo_strings = [
    "racecar",
    "RaceCar",
    "A man, a plan, a canal: Panama",
    "hello",
    "Was it a car or a cat I saw?"
]
print("\nPalindrome checks:")
for s in _demo_strings:
    print(f"'{s}' -> {is_palindrome(s)}")

# ...existing code...