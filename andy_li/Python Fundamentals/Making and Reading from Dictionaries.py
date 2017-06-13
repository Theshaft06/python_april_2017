def dictify(dict):
    for key, val in dict.iteritems():
        print "My", str(key), "is", str(val) + "."


d = {"name": "Anna", "age": 101, "country of birth": "The United States", "favorite language": "Python"}

dictify(d)
