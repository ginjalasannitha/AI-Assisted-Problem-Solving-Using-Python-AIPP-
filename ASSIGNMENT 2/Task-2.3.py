import math
def calculate_area(shape, **kwargs):
    """
    Calculates the area of various shapes (circle, rectangle, triangle).
    Args:
        shape (str): The name of the shape ('circle', 'rectangle', 'triangle').
        **kwargs: Keyword arguments for shape dimensions (e.g., radius, length, etc.).
    Returns:
        float or None: The calculated area or None if the shape is not recognized.
    """
    shape = shape.lower()
    if shape == "circle":
        # Area = pi * r^2
        if 'radius' in kwargs:
            radius = kwargs['radius']
            return math.pi * radius**2
        else:
            print("Error: Circle area requires 'radius'.")
            return None
    elif shape == "rectangle":
        # Area = length * width
        if 'length' in kwargs and 'width' in kwargs:
            length = kwargs['length']
            width = kwargs['width']
            return length * width
        else:
            print("Error: Rectangle area requires 'length' and 'width'.")
            return None
    elif shape == "triangle":
        # Area = 0.5 * base * height
        if 'base' in kwargs and 'height' in kwargs:
            base = kwargs['base']
            height = kwargs['height']
            return 0.5 * base * height
        else:
            print("Error: Triangle area requires 'base' and 'height'.")
            return None
    else:
        print(f"Error: Shape '{shape}' not supported.")
        return None
# Example Usage:
print(f"Circle Area: {calculate_area('Circle', radius=5)}")
print(f"Rectangle Area: {calculate_area('Rectangle', length=10, width=4)}")
print(f"Triangle Area: {calculate_area('Triangle', base=6, height=8)}")
print(f"Square Area: {calculate_area('Square', side=5)}")