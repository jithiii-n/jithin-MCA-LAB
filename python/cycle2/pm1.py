n1=int(input("Enter first number"))
n2=int(input("Enter the second number"))
n3=int(input("Enter the third number"))
if(n1>n2 and n1>3):
	print(n1,"is greatest")
elif(n2>n1 and n2>n3):
	print(n2,"is greatest")
else:
	print(n3,"is greatest")
