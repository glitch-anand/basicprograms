arr=list(map(int,input().split()))
print(arr)
maxnow=0
maxused=0
i=0
for i in range(0,len(arr)):
	maxused+=arr[i]
	if (maxused>maxnow):
		maxnow=maxused
	if(maxused<0):
		maxused=0
print(maxnow) 

