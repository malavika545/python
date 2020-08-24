''' 6.	Tax Calculator
Ask the user for their monthly salary. Calculate whether they have to pay tax and if so, how much is that amount .
Print the result
'''
salary=int(input("Enter the salary: "))
if salary<=250000:
    amount=salary-(0*salary)
elif salary>250000 and salary<=500000:
    amount=salary-(5/100*salary)
elif salary>500000 and salary<=750000:
    amount=salary-(10/100*salary)
elif salary>750000 and salary<=1000000:
    amount=salary-(15/100*salary)
elif salary>1000000 and salary<=1250000:
    amount=salary-(20/100*salary)
elif salary>1250000 and salary<=1500000:
    amount=salary-(25/100*salary)
else:        
    amount=salary-(30/100*salary)
print(amount)