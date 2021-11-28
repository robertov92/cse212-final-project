def is_palindrome(str_raw):
    # Clean up the string
    str = ""
    for i in range(len(str_raw)):
        if str_raw[i].isalnum():
            str += str_raw[i]
    str = str.lower()

    # The remaining of the problem is the same
    # as the one from the tutorial

    # Declare a stack and save the first half of
    # the string contents
    stack = []
    for i in range(len(str) // 2):
        stack.append(str[i])
    # Determine the correct half of string to
    # check if the string is a palindrome
    correct_half = 0
    if len(str) % 2 == 0:
        correct_half = len(str) // 2
    else:
        correct_half = len(str) // 2 + 1

    for i in range(correct_half, len(str)):
        if str[i] != stack.pop():
            return False
    return True

print(is_palindrome("A man, a plan, a canal: Panama."))
print(is_palindrome("race car"))
print(is_palindrome("stacks are cool"))
print(is_palindrome("fun N U F111"))
print(is_palindrome("fun N U F"))