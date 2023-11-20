li=input("Enter the values:").split(',')
li=[int(item) for item in list]
remove=[i for i in li if i%2!=0]
print("original list:",li)
print("New list without even numbers:",remove)

