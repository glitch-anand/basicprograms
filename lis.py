#longest increasing subsequence
def lis(arr):
	tab=[1]*len(arr)
	for i in range(len(arr)):
		for j in range(i+1,len(arr)):
			if arr[i]<arr[j] and tab[i]+1>tab[j]:
				tab[j]=tab[i]+1
	print(max(tab))
arr=list(map(int,input("enter the array").split()))
lis(arr)
