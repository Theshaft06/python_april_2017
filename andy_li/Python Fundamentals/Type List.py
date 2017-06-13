def type_lst(lst):
    my_str = ""
    my_int = 0

    for val in lst:
        val_type = type(val)

        if val_type is str:
            if val is lst[len(lst) - 1]:
                my_str += val
            else:
                my_str += (val + " ")

        if val_type is int or val_type is float:
            my_int += val

    if my_str is "":
        print ("The array you entered is of integer type.")
        print "Sum:", my_int
    elif my_int is 0:
        print ("The array you entered is of string type.")
        print "String:", my_str
    else:
        print ("The array you entered is of mixed type.")
        print "String:", my_str
        print "Sum:", my_int


l = ['magical unicorns',19,'hello',98.98,'world']
# l = [2,3,1,7,4,12]
# l = ['magical','unicorns']
type_lst(l)
