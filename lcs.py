def lcs(str1,str2,lenstr1,lenstr2):
	if lenstr1==0 or lenstr2==0:
		return 0
	elif str1[lenstr1-1]==str2[lenstr2-1]:
		return 1+lcs(str1,str2,lenstr1-1,lenstr2-1)
	else:
		maxim=max(lcs(str1,str2,lenstr1,lenstr2-1),lcs(str1,str2,lenstr1-1,lenstr2))
		return maxim
str1=input("enter the first string")
str2=input("enter the second string")
lenstr1=len(str1)
lenstr2=len(str2)
print("the length of LCS is ", lcs(str1,str2,lenstr1,lenstr2))

