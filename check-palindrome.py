def check_palindrome(num: int) -> bool:
    """
    Function to check
    given integer is palindrome or not
    num (int) : required argument
    Returns :
    bool : If it's palindrome it returns True else False
    """
    if num < 0:
        return False
    # Convert to string
    str_num = str(num)
    # Here we reversed the string using slice method and then converted to integer
    # After converting it to Integer We are comparing it with the orignal number
    return num == int(str_num[::-1])


def check_palindrome_custom(num: int) -> bool:
    # Negative numbers are not considered palindromes
    if num < 0:
        return False

    # Initialize variables for the reversed number and the original number
    reversed_num = 0
    original_num = num

    # Reverse the number
    while num > 0:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num //= 10


    # Checking if the reversed number is the same as the original number
    return reversed_num == original_num


# Example usage
print(check_palindrome_custom(121))  # Should print True
print(check_palindrome_custom(-121))  # Should print False
print(check_palindrome_custom(123))  # Should print False


print(check_palindrome(12221), check_palindrome_custom(12221))
print(check_palindrome(1221), check_palindrome_custom(12210))
print(check_palindrome(12321), check_palindrome_custom(1299921))
print(check_palindrome(-12921), check_palindrome_custom(1221))
print(check_palindrome(12021), check_palindrome_custom(-128721))
print(check_palindrome(11), check_palindrome_custom(1281))
print(check_palindrome(12223241), check_palindrome_custom(128721))
print(check_palindrome(12222231), check_palindrome_custom(12721))
print(check_palindrome(1220872121), check_palindrome_custom(-12821))
