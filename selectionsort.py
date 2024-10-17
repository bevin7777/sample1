a=[]
n=int(input("Enter the number of elements :"))
print("Enter the elements :")
for i in range(0,n):
	k=int(input())
	a.append(k)
for i in range(0,n-1):
	min=a[i]
	pos=1
	for j in rang(i+1,n):
		if a[i]<min:
			min=a[j]
			pos=j
	if i!=pos:
		temp=a[i]
		a[i]=a[pos]
		a[pos]=temp
print("sorted list")
for i in range(0,n):
	print(a[i])