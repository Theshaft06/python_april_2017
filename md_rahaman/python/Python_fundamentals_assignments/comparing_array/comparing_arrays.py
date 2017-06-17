

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','milk','bread','milk']
result=True

#chekck error first and they true statement at the end

if len(list_one) != len(list_two):

	result = False

else:

	for x in range(0, len(list_one)):
		
		if list_one[x] != list_two[x]:
			result=False

			# count=count+1
if result:
	print "they are the same"
else:
	print "they are not the same"



	# if count==len(list_one) and count == len(list_two):
	# 	print "they are the same"

	




	
	# for y in list_two:
		# if x == y:
		# 	print x
		# 	print y

		# if x!=y:
		# 	print("They are not the same ")

# if cmp(list_one, list_two)==0:
# 	print "they are identical"
# else:
# 	print "they are not the same"


			