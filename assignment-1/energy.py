'''
4.	Develop a program that calculates the energy needed to heat water from an initial temperature to a final temperature. 
Your program should prompt the user to enter the amount of water in kilograms and the initial and final temperatures of the water. 
The formula to compute the energy is 
      
    Q = M * (finalTemperature – initialTemperature) * 4184.

where M is the weight of water in kilograms, temperatures are in degrees Celsius,  and energy Q is measured in joules. (L6)

'''
wt=float(input("Enter the amount of water in kilograms(kg): "))
t1=float(input("Enter initial temperature of water in celcius(c): "))
t2=float(input("Enter final temperature of water in celcius(c): "))
energy=wt*(t1-t2)*4184
print("The energy needed to heat water from an initial temperature to a final temperature is {} J".format(energy))