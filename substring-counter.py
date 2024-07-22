def substring_counter(string: str, substr: str) -> int:
    """
    This function count the occurances
    of given substring in a string.
    In this function, We've used String's in-built function 'count()'
    to count the occurances.
    """
    return string.count(substr)


def custom_substring_counter(string: str, substr: str) -> int:
    """
    This is custom function which includes the logic of counting
    a given substring in a String object.
    """
    count = 0
    # calculating the length of sub string
    length_substr = len(substr)
    for i in range(0, len(string)):
        # iteratively comparing each sliced string to a substring
        if substr == string[i : i + length_substr]:
            # If they are equal we incrementing the counter
            count += 1
    return count


intro = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
substr = "in"

print(substring_counter(intro, substr))  #  expected output 3
print(custom_substring_counter(intro, substr))
