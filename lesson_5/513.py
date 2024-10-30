def myPalindrome(number):
    original_number = number
    reversePalindrome = 0

    while number != 0:
        a = number % 10
        reversePalindrome = reversePalindrome * 10 + a
        number //= 10

    if original_number == reversePalindrome:
        return True
    else:
        return False

print(myPalindrome(123))
print(myPalindrome(222))