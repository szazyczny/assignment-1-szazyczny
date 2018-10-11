# (20 points) Write a recursive function isPalindrome(string) that returns True if string is a palindrome, 
# that is, a word that is the same when reversed.
# Examples of palindromes are “deed”, “rotor”, or “aibohphobia”. 
# Hint: A word is a palindrome if the frst and last letters match and the remainder is also a palindrome.

def isPalindrome(s):
    """
    The function will return True if the given string is a palindrome
    and will return Flase if the given sting is not a palindrome
    """
    if len(s) <= 1:     # if only length of 1 then it is a palindrome, if word has odd number of letters it checks the middle letter
        return True
    else:
        return s[0] == s[-1] and isPalindrome(s[1:-1])      # checks first and last letter of word then uses recursion to run the palindrome function on the rest of the word  


inputStr = input("Enter a string: ")
if isPalindrome(inputStr):
    print("That's a palindrome.")
else:
    print("That isn't a palindrome.")


# This was my original code, but I did not use recursion
    # i = 0
    # for i in range(len(s)):
    #     if s[i] == s[-(i + 1)]:
    #         i += 1
    #         if s[i] == s[-(i + 1)]:
    #             return True
    #     else:
    #         return False