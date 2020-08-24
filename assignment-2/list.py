''' 7.	Take a list of integers as an argument, and converts it into a single integer (return the integer).
*Input*: [11, 33, 50]
*Output*: 113350
'''
list1=input("Enter elements of lists: ").split(',')
for i in range(0,len(list1)):
    print(list1[i],end='')
