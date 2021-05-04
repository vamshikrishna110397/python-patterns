n=int(input("enter the number: "))
for i in range(n):
    for j in range(i):
        if j%2==0:
            print('0',end="")
        else:
            print('1',end="") 
    print()           