def print_max(x, y):
   
    '''Prints the maximum of two numbers.
    The two values must be integers.'''
    
    # Convert to integers, if possible
    x = int(x)
    y = int(y)
    
    if x > y:
        print x, 'maximum'
    else:
        print y, 'maximum'
print_max(3, 5) # Calls the function

print print_max.__doc__ # Calls the docstring function (__doc__)