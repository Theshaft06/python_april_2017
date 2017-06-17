
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]


# for student in students:
# 	# print student
# 	print student["first_name"]+" "+student["last_name"]

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

for key, value in users.iteritems():
	print key
 	for index in range(0,len(value)):
 		# print key

 		x=len(value[index]['first_name'])
 		y=len(value[index]['last_name'])
 		length = x+y

 		print "{} - {} {} - {}".format(index+1,value[index]['first_name'],value[index]['last_name'],length)
 	# 	print "hello"
 	# if key == "Instructors":
 	# 	print "Whats up "

# for key,value in users.iteritems():
# 	# print value
# 	for val in value:
# 		print val["first_name"]
#  	# for student in range(0,len(value)):
#  	# 	print value[student]

# # for student in users['Students']:

# #  	# for item in student:
# #  	# 	print student[item]
 		 
# for user in users:
# print users['Students']

# print users['Instructors']


