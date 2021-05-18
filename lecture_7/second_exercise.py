def is_palindrome(s):
    # Reversing the string (look at string slicing).
    reversed_s = s[::-1]

    # Checking equality between reversed s and s
    if s == reversed_s:
        return True
    # if it's not equal, returns false.
    return False


print('Is hello palindrome:', is_palindrome('Hello'))
print('Is abba palindrome:', is_palindrome('AbbA'))
