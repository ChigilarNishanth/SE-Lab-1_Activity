"""
Data Processor Application (Roll No: 56)
Lab 7 - Fixed & Hardened Version
"""
import math

def process_user_age(age):
    """Parses user age with strict type, infinity, and range validation."""
    if age is None or isinstance(age, (bool, list, dict, set, tuple)):
        raise TypeError("Age must be an integer or valid numeric string.")
    
    try:
        if isinstance(age, float):
            if math.isnan(age) or math.isinf(age):
                raise ValueError("Age cannot be NaN or Infinity.")
            age_num = int(age)
        else:
            age_num = int(str(age).strip())
    except (ValueError, TypeError):
        raise TypeError("Invalid age input format.")

    if not (0 <= age_num <= 120):
        raise ValueError(f"Age {age_num} out of valid range (0-120).")
    
    return age_num

def calculate_average(numbers):
    """Calculates average of numbers with empty collection and non-numeric checks."""
    if not isinstance(numbers, (list, tuple)):
        raise TypeError("Input must be a list or tuple of numbers.")
    
    if len(numbers) == 0:
        raise ValueError("Cannot calculate average of an empty collection.")

    valid_sum = 0.0
    for num in numbers:
        if isinstance(num, bool) or not isinstance(num, (int, float)):
            raise TypeError("All items in list must be numeric.")
        if math.isnan(num) or math.isinf(num):
            raise ValueError("Collection contains invalid numeric values (NaN/Inf).")
        valid_sum += num

    return valid_sum / len(numbers)

def format_user_name(name):
    """Formats user name with string type enforcement and non-empty checks."""
    if not isinstance(name, str):
        raise TypeError("Name must be a string.")

    cleaned = name.strip().title()
    if len(cleaned) == 0:
        raise ValueError("Name cannot be empty or whitespace-only.")

    return cleaned

if __name__ == "__main__":
    print("--- Running Fixed Processor with Sample Inputs ---")
    print("Age:", process_user_age("25"))
    print("Average:", calculate_average([10, 20, 30]))
    print("Name:", format_user_name("   nishanth chigilar   "))
