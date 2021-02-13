arr1=list(map(int,input("enter the first array").split()))
arr2=list(map(int,input("enter the second array").split()))
print(arr1)
print(arr2)
arr3=arr1+arr2
print(arr3)
arr3.sort()
print(arr3)
length=len(arr3)
flag=0
if length%2==0:
	flag=1
else:
	flag=0
if flag==1:
	n=length//2
	med=(arr3[n]+arr3[n-1])/2
	print(med)
else:
	n=length//2
	print(arr[n])

