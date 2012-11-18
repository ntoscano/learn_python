def laser_weapon_armory(self):
    print "you do a dive roll into the Weapon Armory, crouch and scan the room"
    print "for more Gothons that might be hiding. It's dead quiet, too quiet."
    print "You stand up and run to the far side of the room and find the"
    print "neutron bomb in its comtainer. There's a keypad lock on the box"
    print "and you need the code to get the bomb out. If you get the code"
    print "wrong 10 times, then the lock closses forever and you can't"
    print "get the bomb. The code is 3 digits."
    code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
    guess = raw_intput("[keypad]> ")
    guesses = 1
    
    return "laser_weapon_armory"
laser_weapon_armory()