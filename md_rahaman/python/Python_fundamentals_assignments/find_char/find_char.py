

list = ['hello','world','my','name','world','nither']
newlist = []

char = 'o'

for x in range(0, len(list)):

	for y in range(0,len(list[x])):

			# print list[x][y]
		if list[x][y] == "o":
			newlist.append(list[x])
			
print newlist


# # slist.find("o")

# for x in range(0,len(list)):
# 	print list[x]