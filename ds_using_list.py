# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

# print "I have", len(shoplist), "items to purchase."
# print "I have {0} items to purchase" .format(len(shoplist))
# print "I have %s items to purchase" % (shoplist)
print "I have", shoplist.len(), "items to purchase."

print "These items are:",
# for .. in loop statement: iterates over a sequence of objects (i.e. go through ea item in a sequence)
# Remember that the "else" statement is optional
for item in shoplist:
    print item,
    
print "\nI also have to buy rice."
# Call .append method to pass object to class list / array
shoplist.append('rice')
print "My shopping list is now", shoplist
# print "My shopping list is now {}" .format(shoplist)
# print "My shopping list is now %s" % (shoplist)
print "I will sort my list now"
# Call .sort method to pass object to class listq
# It is important to understand that this method affects the list itself and does not return a modified list - this is different from the way strings work. This is what we mean by saying that lists are mutable and that strings are immutable.
shoplist.sort()
print "Sorted shopping list is", shoplist
# print "Sorted shopping list is {}" .format(shoplist)
# print "Sorted shopping list is %s" % (shoplist)
print "The first item I will buy is", shoplist[0]
# print "The first item I will buy is {}" .format(shoplist[0])
# print "The first item I will buy is %s" % (shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print "I bought the", olditem
# print "I bought the {}" .format(olditem)
#print "I bought the %s" % (olditem)
print "My shopping list is now", shoplist
#print "My shopping list is now {}" .format(shoplist)
#print "My shopping list is now %s" % (shoplist)



