# Create dict class "Address Book"
# 'ab' is short for address book

ab = {
    'Aronson_Preston' : 'pparonson@gmail.com', 'Aronson_Peni'\
     : 'peni@peniraedesign.com', 'Aronson_Ashley' : 'brenning34@gmail.com'\
     , 'Brenning_Brooke' : 'brookeykay01@gmail.com'
}

print "Ashley's address is", ab['Aronson_Ashley']

# Deleting a key-value pair
del ab['Brenning_Brooke']
# del ab[0], This doesn't work because it is not an ordered list, and therefore there is no ordered value key?

print "\nThere are {} contacts in the address-book:\n" .format(len(ab))

# for statement assigns variables "name" and "address" to the key : value pair
# Call dict .items method 
# See help(dict) for a list of the dict methods
for name, address in ab.items():
    print "Contact {} at {}." .format(name, address)
    
# Adding a key-value pair
ab['Aronson_Sean'] = 'ssaronson@gmail.com'

# If statement
if 'Aronson_Sean' in ab:
    print "\nSean Aronson\'s address is:", ab['Aronson_Sean']