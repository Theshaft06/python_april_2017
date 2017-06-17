

x=[2,54,-2,7,12,98]
y=[]

min=x[0]
max=x[0]

for number in x:

	if(max<number):
		max=number
	if(min>number):
		min=number
y.append(max)
y.append(min)

print max
print min
print y