def format_name(full_name: str) -> str:
    # Handle empty or whitespace input
    if not full_name or full_name.isspace():
        return ""
    # Split name into parts and get first and last
    parts = full_name.strip().split()
    if len(parts) < 2:
        return full_name  
    first_name = parts[0]
    last_name = parts[-1]
    return f"{last_name}, {first_name}"
# Test cases
if __name__ == "__main__":
    test_names = [
        "Ravi Kumar",
        "Sita Lakshmi", 
        "Anil Reddy"
    ]
    for name in test_names:
        formatted = format_name(name)
        print(f"{name} → {formatted}")