'''14. Write a Python code that takes a number and returns a list of its digits. 
So for 586392 it should return [5,8,6,3,9,2]'''
num=input("Enter a number: ")
list1=list()
for i in num:
    n=int(i)
    list1.append(n)
print("list of its digits: ",list1)