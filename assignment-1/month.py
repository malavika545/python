''' 
5.	Develop a program that prompts user to enter month and  print 
    a.	“Winter ” -   December ,January and February
    b.	“Spring”  -   March ,April and May
    c.	“Summer”  --- June ,July, August
    d.	“Autumn ”  -- September ,October, November

'''
month=input("Enter the month: ")
list1=[['Winter','december','january','february'],['Spring','march','april','may'],['Summer','june','july','august'],['Autumn','september','october','november']]
for i in range(len(list1)):
    if month in list1[i]:
        print(list1[i][0])
    else:
        continue
