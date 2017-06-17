
import random 

def coin_toss():

	H=0
	T=0

	for x in range(1,5001):
		rand = random.randint(0,1)
		if rand==0:
			H += 1
			print "Attempt #{}: Throwing a coin... It's a Head! ... Got {} head(s) so far and {} tail(s) so far".format(x,H,T)
		else:
			T += 1
			print "Attempt #{}: Throwing a coin... It's a Tail! ... Got {} tail(s) so far and {} head(s) so far".format(x,T,H)
	
	print "{} {}".format(H,T)
coin_toss()
