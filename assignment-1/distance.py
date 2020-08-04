''' 
2.	A Quick Fox Transport Co. wants to develop an application for calculating amount based on distance and weight of goods. The charges (Amount) to be calculated as per rates given below. 
 
Input:  Distance to be travel: 520     
Weight of the goods: 50 
Output: Amount to be charged: 3120 /-

'''
dist=int(input("Ditance to be travelled: "))
wt=int(input("Weight of goods: "))
if dist>=500:
    if wt>=100:
        charge=5
    elif wt>=10 and wt<100:
        charge=6
    elif wt<10:
        charge=7
else:
    if wt>=100:
        charge=8    
    else:
        charge=5
amount=charge*dist
print("Amount to be charged: {} /-".format(amount))