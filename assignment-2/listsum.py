'''12.	Compute given Num_list =  [5, 6,8 ,34,89,1] to get desired output
Output: Out_list=[11,14,42,123,90]
'''
count=list()
list1=[5,6,8,34,89,1]
for i in range(1,len(list1)):
    n=list1[i-1]+list1[i]
    count.append(n)
print("output is: ",count)