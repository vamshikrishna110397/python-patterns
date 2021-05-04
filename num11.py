n=int(input('enter the number: '))
for i in range (n):
    for j in range(n-i,0,-1):
        print(' ',end='')
    for j in range(1,i):
        if i%2==0:
            print(str(j)+' ',end='')
        else:
            print(" "+str(' '),end='') 
    print()

