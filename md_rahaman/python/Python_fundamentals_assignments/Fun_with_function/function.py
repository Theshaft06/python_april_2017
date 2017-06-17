



def odd_even():
  for x in range(1,2001):
  	if x%2 == 0:
  		print "The number is {}.".format(x)+"This is even number"
  	else:
  		print "The number is {}.".format(x)+"This is odd number"

def multiply(list,multi):
	newlist = []
	for x in list:
		newlist.append(x * multi)
	return newlist
	
def layered_multiples(arr):
	newarr=[]
	for x in range(0,len(arr)):
		newarr.append([])
		for y in range(arr[x]):
			newarr[x].append(1)
	return newarr

# odd_even()
odd_even()
a=[2,4,5]
b=multiply(a,3)
print b

x = layered_multiples(multiply([2,4,5],3))
print x

