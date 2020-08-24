''' 2.	Take a string from end user and check if the value is palindrome or not'''
str1=input("Enter a string: ")
str2=str1[::-1]
if str1==str2:
    print("Palindrome")
else:
    print("Not a palindrome")