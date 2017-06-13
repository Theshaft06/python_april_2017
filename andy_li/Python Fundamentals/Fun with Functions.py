# # Odd/Even
# def odd_even():
#     for i in range(1, 2001):
#         # i is odd
#         if i % 2 == 1:
#             print "Number is", str(i) + ". This is an odd number."
#         # i is even
#         if i % 2 == 0:
#             print "Number is", str(i) + ". This is an even number."
#
# odd_even()

# Multiply
def multiply(lst, multiplier):
    for i in range(len(lst)):
        lst[i] *= multiplier

    return lst
#
# a = [2,4,10,16]
# print multiply(a, 5)

# Hacker Challenge
def layered_multiples(lst):
    new_lst = []
    # creates final result list
    for i in lst:
        # creates each internal list
        each_lst = []
        for j in range(i):
            each_lst.append(1)

        new_lst.append(each_lst)

    return new_lst


print layered_multiples(multiply([1,2,3], 2))
