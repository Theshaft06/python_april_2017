

# def draw_stars(lsit):
# 	for value in list:
# 		print '*' * value


def draw_stars(x):
	for i in range(0,len(x)):

		if type(x[i]) == type(0):
			for j in range(x[i]):
				# print j,
				print '*',

			print('\n')

		elif type(x[i]) == type(""):
			for j in range(0,len(x[i])):
				print x[i][0],
			print '\n'



x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x)