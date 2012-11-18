from random import randint
import math
 
#==================================================================
#= Player ==========================================================
#==================================================================
class Player(object):
   
   # Getting players starting stats.
   def __init__(self, name="", max_hp=25, lvl=1, xp=0, max_xp=20):
      self.name = name
      self.max_hp = max_hp
      self.hp = self.max_hp
      self.lvl = lvl
      self.xp = xp
      self.max_xp = max_xp
   
   # Displays player stats.
   def get_stats(self):
      return "\nName: %s\nLevel: %d\nHP: %s / %s\n" % (self.name, self.lvl, self.hp, self.max_hp)
     
   def encounter(self):
      chance = randint(1,2)
      if chance == 1:
         return True
      else:
         return False
         
   def level_up(self):
      if self.xp >= self.max_xp:
         print "\n*Congragulations! You've leveled up!*\n"
         self.lvl += 1
         self.max_hp += 5
         self.hp = self.max_hp
         self.max_xp += 10 * self.lvl
     
#==================================================================
#= Enemy ===========================================================
#==================================================================
class Enemy(object):
   
   def __init__(self, name, max_hp, lvl, xp_given):
      self.name = name
      self.max_hp = max_hp
      self.hp = self.max_hp
      self.lvl = lvl
      self.xp_given = xp_given
     
#==================================================================
#= Battle ==========================================================
#==================================================================
class Battle(object):
 
   def __init__(self, player, enemy):
      self.player = player
      self.enemy = enemy
      self.dodge = False
   
   def sys_battle(self):
      print "\nYou've encountered a Level %d %s!" % (self.enemy.lvl,self.enemy.name)
      raw_input("Press ENTER to continue.")
      print "\nType one of the following commands below to attempt an action.\n"
      print "[Attack]"
      print "[Defend]"
      print "[Dodge]\n"
     
      while self.enemy.hp > 0:
         action = raw_input(">>> ")
         
         # Normal attack.
         if action == "attack":
            self.enemy.hp -= math.ceil((self.player.lvl * (randint(11.0,15.0) / 10.0) * 2.0) - (self.enemy.lvl * randint(10.0,14.0) / 10.0))
            print "\nYou swing your sword at it leaving minor cuts! [%s HP: %d / %d]" % (self.enemy.name, self.enemy.hp, self.enemy.max_hp)
            self.player.hp -= math.ceil((self.enemy.lvl * (randint(11.0,15.0) / 10.0) * 2.0) - (self.player.lvl * randint(10.0,14.0) / 10.0))
            print "It attacks back and hurts you! [%s's HP: %d / %d]\n" % (self.player.name, self.player.hp, self.player.max_hp)
            self.dodge = False
         
         # Normal defend.
         elif action == "defend":
            print "\nThe %s attacks but you throw up your sword in a defensive motion!" % self.enemy.name
            self.player.hp -= math.ceil((self.enemy.lvl * (randint(11.0,15.0) / 10.0) * 2.0) - (self.player.lvl * randint(13.0,17.0) / 10.0))
            print "You're able to reduce incoming damage. [%s's HP: %d / %d]\n" % (self.player.name, self.player.hp, self.player.max_hp)
            self.dodge = False
         
         # A successful dodge because the counter is at False.
         elif action == "dodge" and self.dodge == False:
            print "\nThe %s charges at you, but you quickly roll out of the way. [Dodge Successful!]\n" % self.enemy.name
            self.dodge = True
               
         # Unsuccessful dodge because the previous turn was used as a dodge.
         elif action == "dodge" and self.dodge == True:
            self.player.hp -= math.ceil((self.enemy.lvl * (randint(11.0,15.0) / 10.0) * 2.0) - (self.player.lvl * randint(7.0,11.0) / 10.0))
            print "\nThe %s quickly turns around and catches you off gaurd." % self.enemy.name
            print "You don't dodge in time and get hit. [%s's HP: %d / %d]\n" % (self.player.name, self.player.hp, self.player.max_hp)
            self.dodge = False
         
         # Not a valid command.
         else:
            print "\nPlease enter a real command!\n"
           
      print "You've killed a Level %d %s!" % (self.enemy.lvl, self.enemy.name)
      self.player.xp += self.enemy.xp_given
      self.player.level_up()
      raw_input("Press ENTER to exit the battle scene.")
     
      # Restoring enemy HP back to max for the next encounter.
      self.enemy.hp = self.enemy.max_hp
      self.dodge = False
 
#==================================================================
#= Inventory =======================================================
#==================================================================      
class Inventory(object):
   
   # Dictionary of items.
   def __init__(self):
      self.items = {
      }
   
   # Add item to list with amount.
   def add_item(self, item, amount):
      if item in self.items:
         self.items[item] += amount
      else:
         self.items[item] = amount
   
   # Remove item from list with amount.
   def remove_item(self, item, amount):
      if item in self.items and self.items[item] >= amount:
         self.items[item] -= amount
         if self.items[item] == 0:
            del self.items[item]
         return True
      else:
         return False
   
   # Check if item is in dictionary.
   def has_item(self, item):
      if item in self.items:
         return True
      else:
         return False
   
   # Checks for specific amounts.
   def has_num_of_item(self, item, amount):
      if item in self.items and self.items[item] >= amount:
         return True
      else:
         return False
 
#==================================================================
#= Game ============================================================
#==================================================================
class Game(object):
   
   def __init__(self, player, inv, start):
      self.player = player
      self.inv = inv
      self.start = start
      # Variable for toggling the game intro.
      self.intro_done = False
      self.first_battle = False
   
   # Engine for playing the game.
   def play(self):
      next_area = self.start
      while True:
         room = getattr(self, next_area)
         next_area = room()
         
   def area_one(self):
      # Plays the intro if this is the first time starting.
      if not self.intro_done:
         print "\nYou are about to stumble into a strange world."
         print "With it comes vicious creatures."
         print "At any time you can type 'options' display your current stats."
         raw_input("Press ENTER to continue.")
         print "\nYour caravan finally comes to a stop."
         # Changes intro_done so it plays through only this one time.
         self.intro_done = True
     
      print "\nYou arrive in AREA 1..."
      print "There are two passable roads in front of you."
      print "AREA 2 or AREA 3, hmmmm, which will it be?\n"
      while True:
         action = raw_input(">>> ")
         if action == "area 2":
            print "\nYou look ahead with a firm grip on your sheathed blade and continue."
            return 'area_two'
         elif action == "area 3":
            print "\nYou approach an overgrown passway with caution."
            return 'area_three'
         elif action == "options":
            print self.player.get_stats()
            raw_input("Press ENTER to go back.")
         else:
            print "Uhhh what?\n"
         
   def area_two(self):
      if self.player.encounter() == True:
         vespoi_battle.sys_battle()
     
      print "\nYou arrive in AREA 2..."
      print "Seems like a relatively peaceful place."
      print "Looks like we got a couple clear paths ahead of us."
      print "Which will it be? AREA 1, AREA 4, or AREA 5?\n"
      while True:
         action = raw_input(">>> ")
         if action == "area 1":
            print "\nAlready been here before, but what harm could come from a revisit."
            return 'area_one'
         elif action == "area 4":
            print "\nThe road quickly converged into a cave."
            print "Sunlight is dim, but rare crystals light the way."
            return 'area_four'
         elif action == "area 5":
            print "\nThe path leads to an open field with long grass.\n"
            return 'area_five'
         elif action == "options":
            print self.player.get_stats()
            raw_input("Press ENTER to go back.")
            return 'area_two'
         else:
            print "\nUhhh what?\n"
   
   def area_three(self):
      if self.player.encounter() == True:
         vespoi_battle.sys_battle()
     
      if self.inv.has_item('Silver Horn') == False:
         print "\nYou arrive in AREA 3..."
         print "Through the brush, you notice a small shrine."
         print "Placed on it is a silver horn."
         print "Do you walk over and pick it up? Or leave?\n"
         while True:
            answer = raw_input(">>> ")
            if answer == "pick it up":
               print "\nThis might be of some use."
               print "\n*Silver Horn Obtained*"
               self.inv.add_item('Silver Horn', 1)
               print "\nLet's leave back to AREA 1 now."
               raw_input("Press ENTER to leave to previous AREA.")
               return 'area_one'
            elif answer == "options":
               print self.player.get_stats()
               raw_input("Press ENTER to go back")
            elif answer == "leave":
               print "\nI guess we can always come back for this."
               return 'area_one'
            else:
               print "\nUhhhhh what?\n"
      else:
         print "\nYou arrive in AREA 3..."
         print "There really isn't much to do here."
         raw_input("Press ENTER to leave to previous AREA.")
         return 'area_two'
         
   def area_four(self):
      # Plays your first REAL battle.
      if not self.first_battle:
         print "\nYou arrive in AREA 4..."
         print "You see a strange creature resembling a raptor."
         print "Do you approach it or leave?\n"
         while True:
            action = raw_input(">>> ")
            if action == "approach it":
               veloci_battle.sys_battle()
            elif action == "options":
               print self.player.get_stats()
               raw_input("Press ENTER to go back")
            elif action == "leave":
               print "Let's get out of here."
               print "It'll still be here later."
               return 'area_two'
            else:
               print "\nI don't get what you mean?\n"
     
      print "\nYou arrive in AREA 4..."
      print "On the ground you see the carcass of the Velociprey you just killed."
      print "The green and blue crystals light up the surroundings."
      print "Gather some or leave?\n"
      while True:
         action = raw_input(">>> ")
         if action == "gather" and self.inv.has_num_of_item('Ocean Gem', 5) == False:
            gathering = randint(1,2)
            if gathering == 1:
               print "\nMining..."
               print "\n*Ocean Gem Obtained*\n"
               self.inv.add_item('Ocean Gem', 1)
            if gathering == 2:
               print "\nMining..."
               print "Nothing this time.\n"
         elif action == "gather" and self.inv.has_num_of_item('Ocean Gem', 5) == True:
            print "\nHave to many of these already.\n"
         elif action == "options":
            print self.player.get_stats()
            raw_input("Press ENTER to go back")
         elif action == "leave":
            print "Let's get out of here now."
            return 'area_two'
         else:
            print "\nUhhhh what?\n"
               
# Setting up the enemies.
vespoid = Enemy("Vespoid", 5, 1, 6)
velociprey = Enemy("Velociprey", 35, 5, 19)
 
inventory = Inventory()        
player = Player(raw_input("\n-\nWhat is your name, traveler? "))
 
vespoi_battle = Battle(player, vespoid)
veloci_battle = Battle(player, velociprey)
 
game = Game(player, inventory, "area_one")
game.play()