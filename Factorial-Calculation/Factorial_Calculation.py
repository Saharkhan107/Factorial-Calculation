# Factorial Calculation
# Student: Sahar Iqbal
# Date: 10/19/2024

def calculate_factorial(n):
    if n < 0:
        raise ValueError("Input must be a positive integer.")
    if n == 0 or n == 1:
        return 1
    return n * calculate_factorial(n - 1)

# Example usage:
result = calculate_factorial(5)
print(result)  # Output: 120

