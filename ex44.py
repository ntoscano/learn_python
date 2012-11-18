class Parent(object): #creates a class called "Parent"
    
    def override(self): #creates a function for parent called 'overide'
        print "PARENT override()"
    
    def implicit(self):
        print "PARENT implicit()"
    
    def altered(self):
        print "PARENT altered()"

class Child(Parent): #creates a subclass of 'parent' called 'child'
    
    def override(self): #overrides the "override" function from the parent class
        print "CHILD override()"
        
    def altered(self): #overrides the "altered" function from the parent class
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered() #changes the fucntion for both the
        #"child" and "parent" class
        print "CHILD, AFTER PARENT altered()"

dad = Parent() #instance of "parent" assigned to "dad"
son = Child() #instance of "child" assigned to "son"

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()