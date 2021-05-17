def ispalindrome(val):
    if len(val) in (0, 1):
        return True
    elif val[0] != val[-1]:
        return False
    else:
        return ispalindrome(val[1:-1])


val = 'rotor'
print("The value {0} is Palindrome : {1}".format(val, ispalindrome(val)))

val1 = 'retor'
print("The value {0} is Palindrome : {1}".format(val, ispalindrome(val1)))

