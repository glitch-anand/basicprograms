#vowel check
s=input('enter the string')
vow=['a','e','i','o','u']
count=0
temp=0
for i in range(len(s)):
	if(s[i] in vow):
		count=count+1
	else:
		temp=max(temp,count)
		count=0
temp=max(temp,count)
print(temp)
