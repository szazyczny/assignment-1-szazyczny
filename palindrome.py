# (20 points) Write a recursive function isPalindrome(string) that returns True if string is a palindrome, 
# that is, a word that is the same when reversed.
# Examples of palindromes are “deed”, “rotor”, or “aibohphobia”. 
# Hint: A word is a palindrome if the frst and last letters match and the remainder is also a palindrome.

def isPalindrome(s):
    i = 0
    for i in range(len(s)):
        if s[i] == s[-(i + 1)]:
            i += 1
            if s[i] == s[-(i + 1)]:
                return True
        else:
            return False


inputStr = input("Enter a string: ")
if isPalindrome(inputStr):
    print("That's a palindrome.")
else:
    print("That isn't a palindrome.")