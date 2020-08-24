'''1.	Area of Triangle :
Given the lengths of three sides of a triangle, calculate the area of the triangle. '''

a=float(input("Enter 1st side: "))
b=float(input("Enter 2nd side: "))
c=float(input("Enter 3rd side: "))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**(1/2)
print("area of a triangle is: %0.4f " %(area))
