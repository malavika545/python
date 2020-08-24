''' 4.	 Space To Hyphen problem 
Take a string as input, and replaces spaces “ “  with hyphens “-”, and returns a string.
Input: “ This program converts spaces into hyphen”
Output:     “ This-program-converts-spaces-into-hyphen”
'''
str1=input("Enter a string: ")
for i in range(0,len(str1)):
    if(str1[i]==' '):
        str1=str1.replace(str1[i],'-')

print(str1)