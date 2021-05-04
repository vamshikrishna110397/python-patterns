n=int(input('enter the number: '))
for i in range(n):
    if i%2==0:
        print("*",end='')
    elif i%3==0:
        print('#',end='')
    else:
        print('@',end='')
print()                