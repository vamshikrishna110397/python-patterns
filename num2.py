n=int(input("enter the number: "))
for i in range(n):
    for j in range(n-i,n):
        print(j,end=" ")
    print()