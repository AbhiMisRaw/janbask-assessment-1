def multiplication():
    """
    Function for printing the multiplication
    table for number 1 to 10
    """
    limit = 10
    for counter in range(1, limit + 1):
        # print(counter)
        for i in range(1, limit + 1):
            print(f"{i*counter} ", end="")

        print()


multiplication()
