arr=list(map(int,input().split()))
print(arr)
n=len(arr)
count=0
for i in range(0,n):
	temp=0
	for j in range(i,n):
		temp+=arr[j]
		if (temp%2==0):
			count=count+1
print(count)
