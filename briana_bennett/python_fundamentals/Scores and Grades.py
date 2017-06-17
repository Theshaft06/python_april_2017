import random

def scores_grades():
    print "Scores and Grades"

    for i in range(10):
        rand_int = random.randint(60, 100)
        if 60 <= rand_int <= 69:
            print "Score:", str(rand_int) + "; Your grade is D."
        if 70 <= rand_int <= 79:
            print "Score:", str(rand_int) + "; Your grade is C."
        if 80 <= rand_int <= 89:
            print "Score:", str(rand_int) + "; Your grade is B."
        if 90 <= rand_int <= 100:
            print "Score:", str(rand_int) + "; Your grade is A."

    print "End of the program. Bye!"

scores_grades()
