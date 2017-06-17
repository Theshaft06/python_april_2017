

x = [19,2,54,-2,7,12,98,32,10,-3,6]
y=[]

x.sort()
print x

print(len(x)/2)
first_half=x[:len(x)/2]
second_half=x[len(x)/2:]

y.append(first_half)
y.append(second_half)

print(y)
