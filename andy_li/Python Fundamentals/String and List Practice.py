# # Find and Replace
# str = "It's thanksgiving day. It's my birthday,too!"
#
# print (str.find("day"))
# print (str.replace("day", "month"))
#
# # Min and Max
# def min_max(lst):
#     min_num = lst[0]
#     max_num = lst[0]
#     for num in lst:
#         if num < min_num:
#             min_num = num
#         if num > max_num:
#             max_num = num
#
#     return "Minimum number = " + str(min_num), "Maximum number = " + str(max_num)
#
# lst = [2, 54, -2, 7, 12, 98]
# print min_max(lst)
#
# # First and Last
#
# def first_last(lst):
#     new_lst = []
#     new_lst.append(lst[0])
#     new_lst.append(lst[len(lst) - 1])
#
#     return new_lst
#
# x = ["hello",2,54,-2,7,12,98,"world"]
# print (first_last(x))

# New List
def new_list(lst):
    result_lst = []
    half_lst = []
    lst.sort()
    half_ind = len(lst) / 2

    for elem1 in lst[:half_ind]:
        half_lst.append(elem1)

    result_lst.append(half_lst)

    for elem2 in lst[half_ind:]:
        result_lst.append(elem2)

    return result_lst

x = [19,2,54,-2,7,12,98,32,10,-3,6]
print (new_list(x))
