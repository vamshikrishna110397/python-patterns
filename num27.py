n=int(input('enter the number: '))
for i in range(n):
    for j in range(n):
        if j==0 or i+j==n//2 or j==i-2:
            print('*',end='')
        else:
            print(' ',end='')
    print()            