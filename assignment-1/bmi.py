''' 
6. write a program that prompts the user to enter a weight in pounds and height in inches and displays the BMI.

'''
wtp=float(input("Enter weight in pound: "))
htin=float(input("Enter height in inches: "))
wtkg=wtp*0.45359237
htm=htin*.0254
bmi=(wtkg/(htm**2))
if bmi<18.5:
    print("Underweight")
elif bmi>=18.5 and bmi<25.0:
    print("Normal")
elif bmi>=25.0 and bmi<30.0:
    print("Overweight")
elif bmi>=30.0:
    print("Obese")