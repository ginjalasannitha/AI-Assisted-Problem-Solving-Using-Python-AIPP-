def cm_to_inches(cm: float) -> float:
    """
    Convert centimeters to inches.
    1 inch = 2.54 centimeters
    
    Args:
        cm (float): Length in centimeters
        
    Returns:
        float: Length in inches
        
    Raises:
        ValueError: If input is negative
    """
    if cm < 0:
        raise ValueError("Length cannot be negative")
    
    return cm / 2.54

# Example usage
if __name__ == "__main__":
    test_values = [10, 25.4, 2.54, 100]
    
    for cm in test_values:
        inches = cm_to_inches(cm)
        print(f"{cm:g} cm = {inches:.3f} inches")