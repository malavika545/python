'''15.	Write a program that finds the longest palindromic substring of a given string'''
str1=input("Enter a string: ")
n=len(str1) 
big=0
for i in range(0,n):
    for j in range(n,i,-1):
        str2=str1[i:j]
        str3=str2[::-1]
        if str2==str3:
            if len(str2)>big:
                big=len(str2)
                b=str2
print(b)
            
    