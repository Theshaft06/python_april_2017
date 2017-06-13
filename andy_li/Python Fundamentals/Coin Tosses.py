import random

def coin_tosses():
    print "Starting the program..."
    heads_count = 0
    tails_count = 0
    coin_val = ""

    for flips in range(1, 51):
        rand_int = random.randint(0, 1)
        if rand_int is 0:
            coin_val = "head"
            heads_count += 1
        if rand_int is 1:
            coin_val = "tail"
            tails_count += 1

        print "Attempt #" + str(flips) + ": Throwing a coin... It's a " + str(coin_val) + "! ... Got " + str(heads_count) + " head(s) so far and " + str(tails_count) + " tail(s) so far."

        coin_val = ""

    print "Ending the program, thank you!"

coin_tosses()
