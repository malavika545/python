'''
9.	Sort 3 Integers
Given three integers (given through user input), sort the numbers using |min| and  |max| functions.

'''
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))
small=min(a,b,c)
large=max(a,b,c)
if a==large:
    if b==small:
        b=c
        a=small
        c=large
    elif c==small:
        a=small
        c=large
elif b==large:
    if a==small:
        b=c
        c=large
    elif c==small:
        b=a
        a=small
        c=large
elif c==large:
    if b==small:
        b=a
        a=small
print(a,b,c)