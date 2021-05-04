
n=int(input('enter the number: '))
for i in range(n):
    for j in range(n):
        if i==j:
            print(i,end='')
        else:
            print('0',end='')
    print()            