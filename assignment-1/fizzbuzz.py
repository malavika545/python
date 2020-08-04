''' 
10.	Write a Java program which iterates the integers from 1 to 100.
 For multiples of three print "Fizz" instead of the number and print "Buzz" for the multiples of five.
 When number is divided by both three and five, print "fizz buzz".
 
'''
min=1
max=100
for i in range(min,max):
    if i%3==0 and i%5==0:
        print("fizzbuzz",end=' ')
    elif i%3==0:
        print("fizz",end=' ')
    elif i%5==0:
        print("buzz",end=' ')
    else:
        print(i,end=' ')