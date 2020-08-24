''' 
10.	Write a program that reads a date from the user and computes its immediate successor. 
The date is the format YYYY-MM-DD. So, 2020-04-15 will have the successor 2020-04-16.'''
date=input("enter date: ").split('-')
for i in range(0,len(date)):
    date[i]=int(date[i])
mydict={'01':31,'02':28,'03':31,'04':30,'05':31,'06':30,'07':31,'08':31,'09':30,'10':31,'11':30,'12':31}
n=len(mydict)
if ((date[0]%4==0) and (date[0]%100!=0)) or (date[0]%400==0):
    mydict['02']=29
for key,value in mydict.items():
    if int(key)==date[1]:
        if date[2]<value:
            date[2]=date[2]+1
            break
        else:
            date[2]=1
            if date[1]<n:
                date[1]=date[1]+1
                break
            else:
                date[1]=1
                date[0]=date[0]+1
print("{}-{}-{}".format(date[0],date[1],date[2]))