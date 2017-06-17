
def grades(arr):
    letter = " "
    for i in range(0, len(arr)):

        if arr[i] >= 90:
            letter = "A"
        elif arr[i] >= 80:
            letter = "B"
        elif arr[i] >= 70:
            letter = "C"
        else:
            letter = "D"
        print "Score: " + str(i) + "Your Grade is " + letter

arr= []
for i in range(1, 10):
    import random
    random_num = random.random()
    arr.append(random_num*100)
    print random_num*100

grades(arr)
