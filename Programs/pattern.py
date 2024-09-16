n = 8
for i in range(0,n*2-1):
    for j in range(0,n*2-1):
        a,b=i,j
        if(a>(n-1)):
            a = (n-1)-(a - (n-1))
        if(b>(n-1)):
            b = (n-1)-(b - (n-1))
        mini = b if b<a else a
        c = chr(n-mini-(n-mini)+mini+1+64);
        print(,end=" ")
    print(end="\n")
