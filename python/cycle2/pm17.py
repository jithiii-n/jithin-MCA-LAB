dict1={'a':1,'bb':2,'c':3,'d':4,'e':5}
sorted_dict=[]
for k,r in dict1.items():
	sorted_dict.append((r,k))
	sorted_dict.sort()
sorted_des=[]
for k,r in dict1.items():
	sorted_des.append((r,k))
	sorted_des.sort(reverse=True)
print(sorted_dict)
print(sorted_des)
