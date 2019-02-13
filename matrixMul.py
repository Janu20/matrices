for _ in range(int(input())):
    n1,m1=map(int,input().split(" "))
    a1=[]
    a2=[]
    z=[]
    z1=[]
    sum=0
    for i in range(n1):
        a1.append(list(map(int,input().split())))
    n2,m2=map(int,input().split(" "))
    for i in range(n2):
        a2.append(list(map(int,input().split())))
    #print(a2)
    for i in range(n1):
        for j in range(m2):
            for k in range(m1):
                sum+=a1[i][k]*a2[k][j]
            z1.append(sum)
            sum=0
        z.append(list(z1))
        z1=[]
    for i in range(n1):
        for j in range(m2):
            print(z[i][j],end=" ")
        print()
