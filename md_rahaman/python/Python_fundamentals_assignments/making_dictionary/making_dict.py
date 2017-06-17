


def make_dict(arr1,arr2):

	make_dict=zip(arr1,arr2)
	print make_dict
	new_dict = dict(make_dict)
	print new_dict

	# new_dict = {}

	# for x in range(0,len(arr1)):
	# 	new_dict[arr1[x]] = arr2[x]

	# print new_dict
	# return new_dict





name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins"]

make_dict(name,favorite_animal)
