''' 
11.	Spider Problem:
    A spider present at the bottom of the well of height H, needs to get out of it, using the slippery wall of the well.
    It decides to climb up the well; it goes up U meters and slips down D meters in one single step.
    So, in each step it covers (U-D) meters, and if the spider gets out of the well by covering U meters in the last step it doesn’t a slip back.
    For example, if the spider climbs up 5 meters and slips down by 3 meters in a single step, it covers (U - D) m in each step and 96 m in 48 steps, but in the 49th step it climbs up 5 m and reaches out of the well and it will not slip down and the step is counted as one step.     

Input: Each test case will contain 3 integers ’H’ height of the well, next ’U’ meters climbs up in each step, and the last ’D’ meters slips down in each step.
Output:  The number of steps 'N' required to get out of the well.
Example 1:
 	Input:						Ouput 
	200 50 1					    5
	Example 2:
 	Input:						Output
	500 20 15					   98

'''
h=int(input("Enter the height of the well: "))
u=int(input("Enter the distance covered: "))
d=int(input("meters slip down in meters: "))
n=0
count=0
while n<h:
    n=n+u-d
    count=count+1
    if n+u>=h:
        count=count+1
        break
print(count)