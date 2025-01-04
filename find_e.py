import math

def calculate_e(digits):
  """
  Calculates the value of Euler's number (e) to the specified number of digits.

  Args:
    digits: The number of decimal places to calculate.

  Returns:
    A string representing the value of e to the specified number of digits.
  """

  # Limit the number of digits to prevent excessive computation
  max_digits = 1000  # Adjust this limit as needed
  if digits > max_digits:
    print(f"Error: Maximum allowed digits is {max_digits}.")
    return None

  # Calculate e using the mathematical constant
  e_value = math.e

  # Format the output with the desired number of decimal places
  e_str = f"{e_value:.{digits}f}"

  return e_str

if __name__ == "__main__":
  try:
    num_digits = int(input("Enter the number of decimal places for e: "))
    result = calculate_e(num_digits)
    if result:
      print(f"e to {num_digits} decimal places: {result}")
  except ValueError:
    print("Invalid input. Please enter a valid integer.")