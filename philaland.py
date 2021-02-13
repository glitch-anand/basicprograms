testcase=int(input())
for i in range(1,testcase+1):
	count=0
	ip=int(input())
	while ip>=1:
		ip=ip//2
		count+=1
	print(count)
