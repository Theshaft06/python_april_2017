



def print_dict(x):
	for data in x:
		print "My {} is {}".format(data,x[data])
		# sprint data, weekend[data]

weekend = {"name": "Soikat", "age": "27","country of birth":"Bangladesh","Favorite Language":"Python"} 
print_dict(weekend)