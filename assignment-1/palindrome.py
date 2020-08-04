'''
8.	Print all palindrome numbers between 1 to 1000.

'''
min=1
max=1000
print("The palindrome numbers between 1 and 1000 are:")
for i in range(min,max):
    temp=i
    rev=0
    while(i>0):
        x=i%10
        rev=(rev*10)+x
        i=i//10
    if temp==rev:
        print("{}".format(temp),end=' ')