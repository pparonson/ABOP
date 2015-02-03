# Filename if.py

number = 23
guess = int(raw_input("Enter an interger: "))
if guess == number:
    # New block begins here
    print "Congratulations, You guessed it!"
    print "(but you do not win any prizes.)"
elif guess < number:
    print 'No, it is a little higher that that.'
    # Block ends here
# Another block begins here
else:
    print 'No, it is a little lower than that.'
print 'done'
    # This last statement is always executed after after the if,
    # statement is executed
    
# Note: -bash: 24: command not found