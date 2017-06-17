


def D_T(dict):
	list=[]
	for data in dict:
		k = (data,dict[data])
		list.append(k)
	print list




my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

D_T(my_dict)



# print my_dict.items()