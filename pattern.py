def print_pattern():
    """
    This function print the following pattern:
    1
    2 2
    3 3 3
    4 4 4 4
    5 5 5 5 5
    """
    limit = 5

    # for prinitng each row
    for counter in range(1, limit + 1):

        # to print each individual digit
        for i in range(1, counter + 1):

            # In this print function 'end' parameter is used to stop jumping in new line.
            print(f"{counter} ", end="")

        # to jump in a new line
        print()


def print_n_pattern(n: int):
    """
    This function prints the following pattern:
    1
    2 2
    3 3 3
    ...
    n n n ... n

    Parameters:
    n (int): The number of rows in the pattern.
    """
    # Loop through each row from 1 to n
    for counter in range(1, n + 1):
        # Print the number 'counter', 'counter' times in the same row
        for i in range(1, counter + 1):
            # Use 'end' to stay on the same line
            print(f"{counter} ", end="")
        # To jump in a new line
        print()


# calling the function
print_pattern()
print("_________________")
print_n_pattern(5)
print("_________________")
print_n_pattern(8)
print("_________________")
