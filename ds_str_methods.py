# This is a string object
name = 'Aronson'

# .startswith method
if name.startswith('Aro'):
	print "Yes, the string starts with 'Aro'."

# Note case sensitivity
if 'a' in name:
	print "Yes, it contains the string 'a'."

if 'A' in name:
	print "Yes, it contains the string 'A'."

# .find method
if name.find('son') != -1:
	print "Yes, it contains the string 'son'."

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']

# .join method
print delimiter.join(mylist)