''' 
9.	Print all Armstrong numbers between 1 to 1000. 

'''
min=1
max=1000
print("The armstrong numbers between 1 and 1000 are:")
for i in range(min,max):
    temp=i
    arm=0
    while(i>0):
        x=i%10
        arm=arm+x*x*x
        i=i//10
    if temp==arm:
        print("{}".format(temp),end=' ')