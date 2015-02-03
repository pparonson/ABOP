# I would recommend always using parentheses to indicate start and end of tuple even though parentheses are optional. 
# Explicit is better than implicit.
zoo = ('python',  'elephant', 'penguin')
# Call len() method and pass zoo var
print "Number of animals in the zoo is", len(zoo)

# Create new tuple and declare new var "new_zoo"
# Notice that we have a tuple within a tuple, however the "zoo" tuple does not lose it's identity
new_zoo = ('monkey', 'camel', zoo)
# Call len() method and pass var "new_zoo"
print "Number of cages in the new zoo is", len(new_zoo)
print "All animals in the new zoo are", new_zoo
# Access the third item in the var tuple "new_zoo" by specifying the "indexing operator".
print "Animals brought from old zoo are", new_zoo[2]
# Access the "third item within the third item" by specifying the the indexing operator. Notice: new_zoo[2][2]
print "Last animal brought from old zoo is", new_zoo[2][2]
# Notice: to accurately print the total number of animals in both tuples add the tuples together by calling len() method and subtract the tuple object "zoo"
print "Number of animals in the new zoo is", len(new_zoo) - 1 + len(new_zoo[2])
