the_count = [1, 2, 3, 4, 5]
fruits = ['abpples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a list
for number in the_count:
    print "This is cound %d" % number

#same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

#also we can go through mixed lists too
#notice we hace to use %r since we don't now what's in it
for i in change:
    print "I got %r" % i
    
# we can also built lists, first start with an empty one
elements = [ ]

#then use the range function to do 0 to 5 counts
for i in range (0, 6):
    print "adding %d to the list." % i
    #append is a function that lists understand
    elements.append(i)
    
#not we can print them out too
for i in elements:
    print "Element was: %d" % i