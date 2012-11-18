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
    
    def central_corridor(self):
        print "The Gothons of Planet Percal #25 have invaded you ship and destroyed"
        print "your entire crew. You are the last surviving member and your last"
        print "mission is to get the neutron destruct bobmb from the Weapons Armory,"
        print "put it in the bridge, and blow the ship uo after getting into an "
        print "escape pod."
        print "\n"
        print "You're running down the central corridor to the Weapons Armory when"
        print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
        print "flowing around his hate filled body. He's blocking the door to the"
        print "Armory and about to pull a weapom to blast you."
        
        action = raw_input("> ")
        
        if "shoot" in action:
            print "Quick on the draw, you yank out your blaster and fire it at the Gothon."
            print "His clown costume is flowing and moving around his body, which throws"
            print "off your aim. Your laser hits his costume but misses him entirely. This"
            print "completly ruins his brand new costume his mother bought for him, which"
            print "makes him fly into an insane rage and blast you repeatedly"
            print "you are dead. Then he eats you."
            return 'death'
        
        elif "dodge" in action:
            print "Like a world class boxer you dodge, weave, slip and slide right"
            print "as the Gothon's blaster cranks a laser past your head."
            print "In the middle of your artful dodge, your foot slips and you"
            print "bang your head on a metal wall and pass out."
            print "You wake up shortly after only to die as the gothon stomps on"
            print "your head and eats you."
            return 'death'
        
        elif "joke" in action:
            print "Lucky for you they made you kearn Gothon instults in the academy."
            print "You tell the one Gothon joke you know:"
            print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhrf."
            print "The Gothon stops, tries not to laugh, then busts out laughing and can't move."
            print "While he's laughing, you run up and shoot him square in the head"
            print "putting him down. Then jump though the Weapons armory door."
            return 'laser_weapon_armory'
        
        else:
            print "No."
            print"hint: Gothon's can't handle jokes"
            return 'central_corridor'
    
    def laser_weapon_armory(self):
        print "you do a dive roll into the Weapon Armory, crouch and scan the room"
        print "for more Gothons that might be hiding. It's dead quiet, too quiet."
        print "You stand up and run to the far side of the room and find the"
        print "neutron bomb in its comtainer. There's a keypad lock on the box"
        print "and you need the code to get the bomb out. If you get the code"
        print "wrong 10 times, then the lock closses forever and you can't"
        print "get the bomb. The code is 3 digits."
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 1
        
        while guess != code and guesses < 10:
            print "BZZZZEDDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")
        
        if guess == code:
            print "The container clicks open and the seal breaks, letting gas out."
            print "You grab the neutron bomb and run as fast as you can to the"
            print "bridge, where you must place it in the right spot."
            return 'the_bridge'
        else:
            print "The lock buzzes one last time and then you hear a sickening"
            print "melting sound as the mechanism is fused together."
            print "You decide to sit there, and finally the Gothons blow up the"
            print "ship from their ship and you die."
            return 'death'


    def the_bridge(self):
        print "You burst onto the Bridge with the netron destruct bomb"
        print "under your arm and suprise 5 Gothons who are trying to"
        print "take control of the ship. Each of them has an even uglier"
        print "clown costume than the last. They haven't pulled their"
        print "weapons out yet, as they see the active bomb under your"
        print "arm and don't want to set it off"
        
        action = raw_input("> ")
        
        if "throw" in action:
            print "In a panic, you throw the bomb at the group of Gothons"
            print "and make a leap for the door. Right as you drop it a"
            print "Gothon shoots you right in the back, killing you."
            print "As you die, you see another Gothon frantically try to disarm"
            print "the bomb. You die knowing they will probably blow up when"
            print "it goes off."
            return 'death'
        
        elif "place" or "set" in action:
            print "You point your blaster at the bomb under your arm"
            print "and the Gothons put their hands up and start to sweat."
            print "You inch backward to the door, open it, and then carefully"
            print "place the bomb on the floor, pointing your blaster at it."
            print "You then jump back through the door, punch the close button"
            print "and blast the lock so the Gothons can't get out."
            print "Now that the bomb is placed you run to the escape pod to"
            print "get off this tin can."
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE!"
            print "HINT: try placing the bomb"
            return 'the_bridge'
        def escape_pod(self):
            print "You rush through the ship desperately trying to make it to"
            print "the escape pod before the whole ship explodes. It seems like"
            print "hardly any Gothons are on the ship, so your run is clear of"
            print "interference. You get to the chamber with the escape pods, and"
            print "now need to pick one to take. Some of them could be damaged"
            print "but you don't have time to look. There's 5 pods, which one"
            print "do you take?"
            
            good_pod = randint (1,5)
            guess = raw_input("[pod #]> ")
            
            
            if int(guess) != good_pod:
                print "You jump into pod %s and hit the eject button." % guess
                print "The pod escapes out into the void of space, then"
                print "implodes as the hull ruptures, crushing your body"
                print "into jam jelly."
                return 'death'
            else:
                print "You jump into pod %s and hit the eject botton." % guess
                print "The pod easily slides out into space heading to"
                print "the planet below. As it flies to the planet, you look"
                print "back and see your ship implode then explode like a"
                print "bright star, taking out the Gothon ship at the same time."
                print "You won!"
                exit (0)


a_game = Game("central_corridor")
a_game.play()