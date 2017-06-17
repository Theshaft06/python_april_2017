

list = [22,45,60,'soikat','rahaman']

sum = 0 
str = ""



for x in list:
	if type(x)==type(0) or type(x) == type(0.1):
		sum = sum + x

	elif(type(x)==type('')):
		str=str+x
		str=str+" "

if sum!=0 and len(str)!=0:
	print "The array you entered is of mixed type"
	print ('sum'),sum
	print (str)
if sum!=0 and len(str)==0:
	print "The array you entered is of integer type"
	print ('sum'),sum
if sum==0 and len(str)!=0:
	print "The array you entered is of string type"
	print (str)






