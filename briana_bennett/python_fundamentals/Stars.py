# # Part I
# def draw_stars(lst):
#     for num in lst:
#         stars_str = "*" * num
#         print stars_str
#
# x = [4, 6, 1, 3, 5, 7, 25]
# draw_stars(x)


# Part II
def draw_stars(lst):
    for elem in lst:
        if type(elem) is str:
            char = elem[0].lower()
            my_str = char * len(elem)
        else:
            char = "*"
            my_str = char * elem

        print my_str

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x)
