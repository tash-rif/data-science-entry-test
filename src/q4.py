def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    if isinstance(s, str):
        return s[::-1]  # [::]: This is the slicing syntax. It consists of three parts: [start:stop:step]. 
                        # The -1 as the step means "step backward," effectively reversing the sequence.


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
print(string_reverse("Hello World"))    # - "Hello World"
print(string_reverse("Python"))         # - "Python"