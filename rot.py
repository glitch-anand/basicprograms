temp=[]
temp2=[]
temp=input('enter array')
arr=[int(x) for x in temp.split()]
num=int(input('enter num'))
print(arr)
for i in range(len(arr)-num, len(arr)):
	temp2.append(arr[i])
for i in range(0,len(arr)-num):
	temp2.append(arr[i])
print(temp2)
