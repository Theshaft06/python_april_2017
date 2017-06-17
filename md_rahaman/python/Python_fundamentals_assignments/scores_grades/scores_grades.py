

import random

def random_score():
	for x in range(0,10):

		random_num = random.randint(60,100)
		print random_num

		if random_num>=60 and random_num<=69:
			print "Score: {};".format(random_num)+" Your grade is D"

		elif random_num>=70 and random_num<=79:
			print "Score: {};".format(random_num)+" Your grade is C"

		elif random_num>=80 and random_num<=89:
			print "Score: {};".format(random_num)+" Your grade is B"

		else:
			print "Score: {};".format(random_num)+" Your grade is A"

	print "End of the program bye"

print(random_score())