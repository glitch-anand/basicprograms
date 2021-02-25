#check if sum is present on array
s=int(input('enter s:'))
arr=list(map(int,input().split()))
print(arr)
for i in range(len(arr)):
	sum=arr[i]	
	j=i+1
	while j<len(arr):
		if sum==s:
			print("the sum is present from %d to %d"%(i,j-1))
		if sum>s or j==len(arr):
			print(" sum not found")
			break
		sum=sum+arr[j]
		j=j+1

