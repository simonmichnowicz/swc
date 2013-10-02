import sys

if (len(sys.argv)!=4):
	print "Error, you must specify 3 strings"
	sys.exit(100)
myList = (sys.argv[1],sys.argv[2],sys.argv[3]);
for  index, value  in enumerate( myList):
	print value,
	if (index == len(myList)-2):
		print "and",
	else:
		if (index != len(myList)-1):
			print ",",
		else:
			print "\n";

print "Bye",



