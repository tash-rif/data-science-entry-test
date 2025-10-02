def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    if (str(num).isnumeric()) and (str(divisor).isnumeric()):
        if num % divisor == 0:
            return True
        else:
            return False
    else:
        print("Both num and divisor must be numeric.")
        return None


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
print(check_divisibility(10, 2))        # - 10, 2
print(check_divisibility(7, 3))         # - 7, 3
print(check_divisibility(10, "two"))    # Example of non-numeric input