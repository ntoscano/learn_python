from sys import exit # imports function "exit" from file "sys"

def gold_room(): #defining "gold_room" function
    print "This room is full of gold.  How much do you take?"
    next = raw_input("> ") # next is equal the string given in raw_input
    while next.isdigit() is False: #"while" is used here becasue it's is continueous.
        #"if" wouldnt work because it would only loop once.
        print "Man, learn to type a number."
        try:
            next = raw_input("> ")
            next.isdigit()
        except ValueError:
            print "bla"
    if next.isdigit() is True:
        num = int(next)
        if num < 50:
            print "Nice, you're not greedy, you win!"
        
        if num > 50:
            dead("You greedy bastard!")
            exit(0)



def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif "taunt" in next and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."


def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    next = raw_input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()