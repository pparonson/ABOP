x = 50 # Value of parameter declared in the main block
def func(x):
    print 'x is', x # Local assigned value to x
    x = 2
    print "Changed local x to", x
    
func(x)
print "x is still", x