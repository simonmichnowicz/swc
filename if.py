import sys


number = int(sys.argv[1])

if (number < 50) and ( number>0):

    print "Minor"

elif (number >= 50) and (100 > number):

    print "Major"

else:
    print "Severe"
