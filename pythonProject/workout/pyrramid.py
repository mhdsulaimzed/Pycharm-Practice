n=4
k=1
for i in range(1,5):
    for j in range(1,n):
        print(end=" ")

    for k in range(1,k+1):
        print("*",end="")
    print()
    n=n-1
    k=k+2