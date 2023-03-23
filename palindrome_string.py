# Input: madam
# Output: Palindrome
# Input: welcome
# Output: Not Palindrome

# Approach 1:
# 1) Find reverse of string
# 2) Check if reverse and original are same or not
s = input("Enter a string: ")    # abcde

# print(s[:])     # abcde
# print(s[0:5])     # abcde
# print(s[0:5:1])     # abcde
# print(s[0:5:2])     # ace
# print(s[::])     # abcde

reverse_s = s[::-1]      # edcba

if reverse_s == s:
    print(s, "is a Palindrome")
else:
    print(s, "is not a Palindrome")

# Enter a string: madam
# madam is a Palindrome
