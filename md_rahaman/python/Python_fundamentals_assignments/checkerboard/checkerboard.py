
space=" "
star = "*"

# for i in range(0,2):
# 	for j in range(0,2):
# 		print("* * * *")
# 		print(" * * * * ")

# for i in range(0,2):
# 	for j in range(0,2):
# 		print star+space

for i in range(1,8):
	if(i%2!=0):
		for j in range(0,6):
			print '*',
	else:
		print ' ',
		for j in range(0,6):
			print '*',

	print "\n"
		