str1=input("enter the forst string")
str2=input("enter the second string")
if(len(str1)!=len(str2)):
	print("error")
	

else:
	anticlock=""
	clock=""
	anticlock=(anticlock+str2[len(str2)-2:]+str2[0:len(str2)-2])
	clock=(clock+str2[2:]+str2[0:2])
	if(str1==anticlock or str1==clock):
		print("ROTATION")
	else:
		print("NOT ROTATION")
