file = open("sample.txt") 
while True:
 line = file.readline()
 print "Line is ",line
 if not line: 
	break 
file.close()
print "BYTE"

