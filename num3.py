n=int(input('enter the number: '))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(' ',end='')
    for j in range(i,n+1):
        print(str(i)+' ',end='') 
    print()       