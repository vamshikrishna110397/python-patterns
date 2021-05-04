n=int(input('enter the number: '))
for i in range(n+1):
    for j in range(i):
        print(' ',end='')
    for j in range (i,n+1):
        print(str(j)+' ',end='')
    print()
for i in range(n,0,-1):
    for j in range(i):
        print(' ',end='')
    for j in range(i,n+1):
        print(str(j)+' ',end='')
    print()                    