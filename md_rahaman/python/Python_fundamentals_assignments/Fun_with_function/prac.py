def layered_multiples(arr):
	newarr=[]
	for x in range(0,len(arr)):
		newarr.append([])
		for y in range(arr[x]):
			newarr[x].append(1)
	return newarr



print(layered_multiples([6,12,15]))
