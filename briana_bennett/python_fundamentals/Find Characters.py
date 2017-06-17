def find_char(lst, char):
    my_lst = []

    for elem in lst:
        if char in elem:
            my_lst.append(elem)

    print (my_lst)

l = ['hello','world','my','name','is','Anna']
char = 'o'

find_char(l, char)
