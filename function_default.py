# Define function "say" and associated parameters.
# Default value for "times" parameter = 1
def say(message, times = 1):
    print message * times
    
# Call "say" function    
say('Hello', 3)
say ('World')