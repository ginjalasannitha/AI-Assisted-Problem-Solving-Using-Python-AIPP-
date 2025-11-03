def count_vowels_zero_shot(text: str) -> int:
    """Basic vowel counter without prior examples"""
    return sum(1 for char in text.lower() if char in 'aeiou')
# Add zero-shot test
print("\nZero-shot testing:")
test_str = "Hello World"
print(f"'{test_str}' has {count_vowels_zero_shot(test_str)} vowels")
def count_vowels_few_shot(text: str) -> int:
    vowels = set('aeiouAEIOU')
    return sum(1 for char in text if char in vowels)
# Comparative testing
if __name__ == "__main__":
    test_cases = [
        "hello",
        "AI",
        "Ramesh",
        "rhythm",
        "AEIOU"
    ]
    print("\nComparison of approaches:")
    print("-" * 40)
    for text in test_cases:
        zero_result = count_vowels_zero_shot(text)
        few_result = count_vowels_few_shot(text)
        print(f"Input: {text}")
        print(f"Zero-shot: {zero_result}")
        print(f"Few-shot: {few_result}")
        print("-" * 40)