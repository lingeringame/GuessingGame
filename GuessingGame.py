

import random

prevcat = 0
prevdiff = 0

def getGuess():
    #final version: must validate input as 0-100, and not crash on illegal input
    # and loop until correct input
    g = -1
    while g < 0:
        try:
            g = int(input("Your Guess? (0=quit): "))
            if g < 0 or g > 100:
                print("Guessing range is between 1 and 100 only")
        except ValueError:
            print("Illegal input: integers 1 to 100 only")
            g = -1

    return g

def playHighLow(rn):
    print("I am thinking of a whole number between 1 and 100...")
    gcount = 0;
    playing = True
    while playing:
        guess = getGuess()
        gcount += 1
        if guess == 0:
            print("Sorry, you did not guess my number: "
                  + str(rn) + " in " + str(gcount-1) + " tries.")
            playing = False
        elif guess == rn:
            print("You guessed it! It took " + str(gcount) + " tries.")
            playing = False
        elif guess > rn:
            print("Sorry, that guess is too high")
        else:
            print("Sorry, that guess is too low")



def playHotCold(rn):
    print("I am thinking of a number from 1 to 100...")
    gcount = 0;
    playing = True  #boolean: True, or False
    while playing:
        guess = getGuess()
        gcount += 1
        if guess == 0:
            print("Sorry, you did not guess my number: "
                  + str(rn) + " in " + str(gcount-1) + " tries.")
            playing = False
        elif guess == rn:
            print("You guessed it! It took " + str(gcount) + " tries.")
            playing = False
        else:
            showHotCold(rn,guess)
            playing = True
    #end of playHotCold

def showHotCold(rn,guess):
    global prevcat, prevdiff
    diff = abs(rn - guess)  #absolute value of difference
    category = 0
    msg= ""
    if diff >= 60:
        category = 1
        msg = "cold"
    elif diff >=30:
        category = 2
        msg = "warm"
    elif diff >= 16:
        category = 3
        msg = "very warm"
    else:
        category = 4
        msg = "HOT"

    if category == prevcat:
        #add modifier
        if diff == prevdiff:
            msg += " (same degree)"
        elif diff > prevdiff:
            msg += " (getting colder)"
        else:
            if category == 4:
                msg += " (getting HOTTER)"
            else:
                msg += " (getting warmer)"
           
    print("Your guess is: " + msg)
    prevcat = category  #update global variables to 'remember' settings
    prevdiff = diff
    
    

    
def getChoice():
    c = -1
    while c < 0 or c > 2:
        try:
            c = int(input("Game type: 1=Hot/Cold, 2=High/Low, 0=Quit: "))
            if c < 0 or c > 2:
                print("Unknown game type: 0, 1 or 2 only.")
        except ValueError:
            print("Illegal input: integers from 0 to 2 only")
            c = -1
    return c
        


def main():
    print("Welcome to the Guessig Game")

    gametype = getChoice()
    while gametype != 0:
        rnum = random.randint(1,100)
        if gametype == 1:
            playHotCold(rnum)
        elif gametype == 2:
            playHighLow(rnum)
        else:
            print("I do not know that game!")
        print()
        gametype = getChoice()
    print("Thanks for playing!")
        

if __name__ == "__main__":
    main()
    
