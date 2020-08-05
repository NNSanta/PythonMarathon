# Program to check if a string is palindrome or not
my_str = input("Enter a word: ")
# make it suitable for caseless comparison
my_str = my_str.casefold()
# reverse the string
rev_str = reversed(my_str)
# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")

##############################################
def isPalindrome(s):
    return s == s[::-1]
s = input("Enter a word: ")
ans = isPalindrome(s)
if ans:
    print("Yes")
else:
    print("No")
#############################################
x = input("Enter a word: ")
w = ""
for i in x:
    w = i + w
    if (x==w):
        print("YES")