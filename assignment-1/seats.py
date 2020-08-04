'''
3.	The Entertainment Paradise

A theater in Delhi wants to develop a computerized Booking System. The theater offers different types of seats. 
The Ticket rates are- Stalls- Rs. 625/-, Circle- Rs.750/-, Upper Class- Rs.850/- and Box- Rs.1000/-.
A discount is given 10% of total amount if tickets are purchased on Cash.
In case of credit card holders 5% discount is given. 

Input: 	Type of Seat: Circle    
Payment mode: cash
Output: Cost of ticket: 675

 '''
seats=input("Types of seats (circle,stalls,upper class,box): ")
pay=input("Payment mode(cash or card): ")
dict1={'circle':750,'stalls':625,'upper class':850,'box':1000}
if pay.lower()=='cash':
    discount=1/10
elif pay.lower()=='card':
    discount=1/5
else:
    print("correct input")
for seat in dict1:
    if seat==seats:
        rate=dict1[seat]
    else:
        continue
amount=rate-(discount*rate)
print("cost of ticket is {}/-".format(int(amount)))