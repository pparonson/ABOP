def func(a, b = 5, c = 10):
    print 'a is', a, 'b is', b, 'and c is', c
    # print "a is {}, b is {}, and c is {}" .format(a, b, c)
    # print "a is %d, b is %d, and c is %d" % (a, b, c)
    
# Call the function    
func(3, 7)
func(25, c = 24)
func(c = 50, a = 100)