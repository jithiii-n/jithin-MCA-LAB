str1=input("Enter the first string:")
str2=input("Enter the second string:")
x=str1[0:1]+str2[1:2]+str1[2:]
y=str2[0:1]+str1[1:2]+str2[2:]
str3=x+" "+y
print(str3)

