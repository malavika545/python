''' 3.	Write a program that reads a year from the user and displays a message 
Indicating whether or not it is a leap year.
'''
year=int(input("Enter a year: "))
if year%4==0:
    if year%100:
        if year%400:
            print(year,"is a leap year")
        else:
            print(year,"is not a leap year")
    else:
        print(year,"is a leap year")
else:
    print(year,"is not a leap year")