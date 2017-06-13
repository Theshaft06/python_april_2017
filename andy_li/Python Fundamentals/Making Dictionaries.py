def make_dict(lst1, lst2):
    if len(lst1) > len(lst2):
        new_dict = zip(lst1, lst2)
    elif len(lst1) < len(lst2):
        new_dict = zip(lst2, lst1)

    return dict(new_dict)

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "deez", "coconuts"]

print make_dict(name, favorite_animal)
