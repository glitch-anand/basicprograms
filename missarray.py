arr=list(map(int,input().split()))
n=len(arr)
total=((n+1)*(n+2))/2
arrsum=sum(arr)
res=total-arrsum
print(int(res))
