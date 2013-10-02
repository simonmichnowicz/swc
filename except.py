file_name="test.cvs"
try:
    file=open(file_name)
except:
    print "Can't find file", file_name
print file.readline()
