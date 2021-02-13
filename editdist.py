def editdistance(string1,string2,m,n):
	tab=[[0 for x in range(n + 1)] for x in range(m + 1)]
	for i in range(m+1):
		tab[i][0]=i
	for j in range(n+1):
		tab[0][j]=j
	for i in range(m+1):
		for j in range(n+1):
			if (string1[i-1]==string2[j-1]):
				tab[i][j]=tab[i-1][j-1]
			else:
				tab[i][j]=min(tab[i][j-1],tab[i-1][j],tab[i-1][j-1])+1
	return tab[m][n]					
string1="SUNDAY"
string2="SATURDAY"
print(editdistance(string1,string2,len(string1),len(string2)))

