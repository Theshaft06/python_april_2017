def filter_by_type(input):
    # Integer
    if type(input) is int:
        if input >= 100:
            print "That's a big number!"
        else:
            print "That's a small number"

    # String
    if type(input) is str:
        if len(input) >= 50:
            print ("Long sentence.")
        else:
            print ("Short sentence.")

    # List
    if type(input) is list:
        if len(input) >= 10:
            print ("Big list!")
        else:
            print ("Short list.")

sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

test_lst = [sI, mI, bI, eI, spI, sS, mS, bS, eS, aL, mL, lL, eL, spL]
for val in test_lst:
    filter_by_type(val)
