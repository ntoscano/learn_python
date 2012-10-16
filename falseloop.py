def false_loop():
    next = raw_input("> ")
    if next.isdigit() is False:
        print "Man, learn to type a number."
        false_loop
    num = int(next)
    if num < 50:
        print "Nice, you're not greedy, you win!"
    exit(0)
    if num > 50:
        dead("You greedy bastard!")

false_loop