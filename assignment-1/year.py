'''
 1.	Develop a code for below scenario
  year%12={
           0:Moneky
           1:Rooster
           2:Dog
           3:Pig
           4:Rat
           5:Ox
           6:Tiger
           7:Rabbit
           8:Dragon
           9.Snake
           10.Horse
           11.Sheep
           }
  
'''
year=int(input("Enter year:"))
rem=year%12
output={0:"Monkey",1:"Rooster",2:"Dog",3:"Pig",4:"Rat",5:"Ox",6:"Tiger",7:"Rabbit",8:"Dragon",9:"Snake",10:"Horse",11:"Sheep"}
print(output[rem])
