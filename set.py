"""
simon made a multiline string
another
"""
sentance="Apple, banana, and cherry."
sentance2 = "A zzzz"

mySet=set([]);
for char in sentance:
	mySet.add(char)

print "No of Unique chars is ", len(mySet)

mySet2= set([])
for char in sentance2:
        mySet2.add(char)

print "No of Unique chars is ", len(mySet2)
myUnion = mySet.intersection(mySet2)
print "No of unique sets"
for char in myUnion:
    print "Common char is ",char


	
