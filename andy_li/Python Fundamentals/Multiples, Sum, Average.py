## Multiples
# def multiples1():
#     for num in range(1, 1000, 2):
#         print num
#
# print (multiples())
#
# def multiples2():
#     for num in range(5, 1000001, 5):
#         print num
#
# multiples2()

# # Sum List
# def sumLst(lst):
#     sum = 0
#     for val in lst:
#         sum += val
#
#     return sum
#
# a = [1, 2, 5, 10, 255, 3]
# print (sumLst(a))

# Average List
def avg_lst(lst):
    sum = 0
    for val in lst:
        sum += val

    return sum / len(lst)

a = [1, 2, 5, 10, 255, 3]
print (avg_lst(a))
