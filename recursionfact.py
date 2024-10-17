def factorial(n):
	if n==1:
		return 1
	f=n*factorial(n-1)
no=int(input('Enter the number:'))
fact=factorial(no)
print("Factorial is:",fact)