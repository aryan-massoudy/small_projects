import mpmath

def get_pi_to_x_digits(x):
    # Set the precision (maximum digits) to x + a few extra digits for accuracy
    mpmath.mp.dps = x + 5
    
    # Get the value of Pi to x digits
    pi_value = str(mpmath.mp.pi)
    
    # Print the result
    print(f"Pi to {x} digits: {pi_value[:x + 2]}")  # including '3.'
    
def main():
    # Limit the number of digits
    limit = 1000  # Set a reasonable limit for digits (e.g., 1000)
    
    try:
        x = int(input(f"Enter a number (up to {limit} digits) to get Pi to that many decimal places: "))
        
        if x < 1 or x > limit:
            print(f"Please enter a number between 1 and {limit}.")
        else:
            get_pi_to_x_digits(x)
    
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
