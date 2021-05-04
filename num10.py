n=5
for i in range(n):
    for j in range(1,i):
        if j%2==0:
            print('#',end='')
        elif j%3==0:
            print("*",end='')
        else:
            print('@',end='') 
    print()  
