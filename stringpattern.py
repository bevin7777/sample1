word=input("Enter a word :")
l=len(word)
for i in range(1,l+1):
	print(word[0:i])
for j in range(0,i+1):
		print(word[j],end=" ")
	