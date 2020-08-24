'''16.	 Substring Check (Bug Funny)
Given two binary strings, A (of length 10) and B (of length 5), output 1 if B is a substring of A and 0 otherwise.
First two lines of input:

1010110010          10110
1110111011           10011
First two lines of output:
1
0
'''
n=int(input("Enter how many times u want to run the loop: "))
for i in range(0,n):
    a=input("Enter a: ")
    b=input("Enter b: ")
    if b in a:
        print("1")
    else:
        print("0")