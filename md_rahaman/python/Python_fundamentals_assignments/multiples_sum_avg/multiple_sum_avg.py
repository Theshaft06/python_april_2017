

# #Multiples

# #part1
for count in range(1,1000):
	if(count%2!=0):
		print count

# #part2
for count in range(5,1000000):
	if(count%5==0):
		print count



# #Sum List
a = [1, 2, 5, 10, 255, 3]

sum = 0
avg = 0

for x in a:
	sum = sum+x
#finding average
avg = sum/len(a)
print ("sum is: "),sum
print ("avg is: "),avg

