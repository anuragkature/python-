# Example: Division by zero exception handling
try:
    numerator = 10
    denominator = 0
    result = numerator / denominator
    print(result)
except ZeroDivisionError:
    print("Error: Denominator cannot be 0.")
