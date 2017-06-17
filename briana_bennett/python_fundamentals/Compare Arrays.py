def compare_lst(lst1, lst2):
    str1 = "".join(str(elem) for elem in lst1)
    str2 = "".join(str(elem) for elem in lst2)

    if str1 == str2:
        print ("The lists are the same.")

    else:
        print ("The lists are not the same.")

# list_one = [1,2,5,6,2]
# list_two = [1,2,5,6,2]
list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
compare_lst(list_one, list_two)
