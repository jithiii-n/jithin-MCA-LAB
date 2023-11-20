inp=input("enter a string")
char_freq={}
for char in inp:
	if char in char_freq:
		char_freq[char]+=1
	else:
		char_freq[char]=1
print("character freq in the string:")
for char,count in char_freq.items():
	if char.isspace():
		print(f"space.{count} times")
	else:
		print(f"{char}:{count} times")
