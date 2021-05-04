n=int(input("enter the number: "))
for i in range (n):
    for j in range(i):
        if i%2==0:
            print('#',end='')
        else:
            print('*',end='') 
    print()           