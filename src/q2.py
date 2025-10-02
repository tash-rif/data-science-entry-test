def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    if isinstance(lst, list):
        i = 0
        for x in lst:
            if (x == find_val):
                lst[i] = replace_val
            i += 1
        return lst


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
print(find_and_replace([1, 2, 3, 4, 2, 2], 2, 5))   # - [1, 2, 3, 4, 2, 2], 2, 5
print(find_and_replace(["apple", "banana", "apple"], "apple", "orange"))    # - ["apple", "banana", "apple"], "apple", "orange"
print(find_and_replace("not a list", "apple", "orange"))