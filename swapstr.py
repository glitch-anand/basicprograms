n=int(input('enter n:'))
string1=input('enter the first string')
string2=input('enter the second string')
for i in range(0,len(string1)):
	if(string1[i] in string2):
		flag=1
	else:
		flag=0
			
if(flag==1):
	print('YES')
else:
	print('NO')
