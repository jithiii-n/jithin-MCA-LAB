def simp(yn,p,n):
	if yn=="y":
		interest=0.12*n*p
	else:

		interest=0.10*n*p
	print("the simple interest is",interest)

n=int(input("enter the number of years"))
p=int(input("enter the principle amount"))
yn=input("enter whether the person is senior citizen or not(y/n)")

simp(yn,p,n)
