from sys import exit
from random import randint

class Game(object):
    
    def __init__(self, start):
        self.quips = [
            "You died. You kinda suck at this.",
            "Your mom would be proud. If she were smarter"
            "Such a luser.",
            "I have a small puppy that is better at this."
        ]
        self.start = start
        
    def play(self):
        next_room_name = self.start
        
        while True:
            print "\n-------"
            room = getattr(self, next_room_name)
            next_room_name = room()
    
    
    def death(self):
        print self.quips[randint(0, len(self.quips)-1)]
        exit(1)
    
    def your_room(self):
        print "You are a skilled ninja in 15th cent. Japan equiped with only ninja stars"
        print "becasue you had gotten drunk the night before and traded your sword for"
        print "a puppy. (the puppy ran away already)"
        print "\n"
        print "You are awaken in the middle of the night by the screams"
        print "of your fellow villagers. You hear some one in the hall way"
        print "out side of your room. You slowly open your door, and at the end of"
        print "the hall, there is an enemy ninja trying to steal your valuables."
        return 'fight_or_flight'
        
    def fight_or_flight(self):
        action = raw_input("> ")
        
        if "star" in action:
            print "As you're about to throw the ninja star, you hear other enemy ninja near by"
            print "and realise that if you hit the ninja, but don't kill him, he could call for help"
            print "where do you aim?"
            return 'ninja_star'
        else:
            print "try a ninja star next time"
            return 'fight_or_flight'
    def ninja_star(self):
        
        action = raw_input("> ")
        
        if "body" in action:
            print "You hit him right in the heart like a pro!"
            print "in his last dying breath, he calls for help..."
            return 'death'
        
        if "head" in action:
            print "You miss completly, he sees you and alerts the others"
            return 'death'
        
        if "neck" in action:
            print "You hit him right in the throat like a boss! He is unable to make"
            print "a noise as he bleeds out"
            print "you take his sword"
            return 'outside'
        else:
            print "try the body, head, or neck area's"
            return 'ninja_star'

    
    def outside(self):
        print "You skillfully escape your house undetected and"
        print "see the leader of the enemy ninjas in the middle of the street."
        print "You realise that if you take him out, the rest of the invading ninjas"
        print " will retreat."
        
        action = raw_input("> ")
        
        if "attack" in action:
            print "You were no match for him, you were dead before you hit the floor"
            print "ninjas are trained to follow, assasinate, and use stealth"
            print "to their advantage, not just walk up to an enemy and swing their sward"
            return 'death'
        
        elif "follow" in action:
            return 'woods'
        else:
            print "no."
            print " attack him, or follow him."
            return 'outside'
    def woods(self):
        print "You follow him into the dark woods and finally get him alone."
        print "You realize this is your time to act, now or never."
        
        action = raw_input("> ")
        
        if any("sneak", "assasinate", "stealth") not in action:
            print"...cmon, you're a ninja! you can't just attack!"
            print "STEALTH, SNEAK ATTACKS, ASSASINATIONS!"
            print "The gods decide that you have come too close to loose now."
            print "they give you another chance"
            return 'woods'
        else:
            print "You throw a ninja star at a near by tree to distract the warlord,"
            print "you take out his legs, get him on the ground and have your blade to his neck"
            print "You take off his mask to stare into his eyes as he dies, and realise, it's your father."
            return 'the_choice'
        
    def the_choice(self):
        action = raw_input("Do you kill him, or let him live? ")
        
        if "kill" in action:
            print "good job, you win!"
            exit(0)
        elif "live" in action:
            print "as soon as you let him up, he stabs you in the lung."
            return 'death'
        else:
            print "no."
            return 'the_choice'

a_game = Game("your_room")
a_game.play()