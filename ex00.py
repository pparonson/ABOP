print "Hello world!" # Note that print is a statement

age = 39
name = 'Preston'

print "{0} was {1} years old when he wrote this book" .format (name, age)
print "Why is {0} playing with that python?" .format (name)

print name + ' is ' + str(age) + ' years old.'

# decimal (.) precision of 3 for float '0.333'
print '{0:.3f}' .format(1.0/3)

# fill with underscores (_) with the text centered
# (^) to 11 width '__hello__'
print '{0:_^11}' .format("hello")

# keyword-based 'Swaroop wrote A Byte of Python'
print "{name} wrote {book}" .format(name = 'Swaroop', book = "A Byte of Python")

print 'a',
print 'b'

print "This is the first line\nThis is the second line."