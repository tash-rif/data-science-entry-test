def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    if (str(x).isnumeric()) and (str(y).isnumeric()):
        temp = x
        x = y
        y = temp
        print("x: ", x)
        print("y: ", y)
    else:
        return -1

# Task 2
# Invoke the function "swap" using the following scenarios:
print(swap("Apple", 10))    # - "Apple", 10
print(swap(9, 17))          # - 9, 17

