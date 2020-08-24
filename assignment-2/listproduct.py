'''13. Compute given Num_tuple =  (5, 6,8 ,3,9,1) to get desired output
Output: Out_list = [5, 30, 240, 720, 6480, 6480]
'''
num_tuple=(5,6,8,3,9,1)
out_list=list()
pro=1
for i in num_tuple:
    pro=pro*i
    out_list.append(pro)
print("out_list: ",out_list)