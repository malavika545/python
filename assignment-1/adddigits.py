''' 
7.	Write a program that reads an integer between 100 and 1000 and adds all the digits in the integer 
	(	ex: input 745 	# output =16	(7+4+5)	)
  
'''
sum1=0
num=int(input("Enter an integer between 100 and 1000: "))
if num>=100 and num<=1000:
    while(num>0):
        x=num%10
        sum1=sum1+x
        num=num//10
    print(int(sum1))
else:
    print("please enter number in between 100 and 1000")
