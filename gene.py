from pprint import pprint
myDNA = {'G':0, 'A':0, 'T':0,'C':0}
input = "GAATTAAC"
for c in input:
    myDNA[c]=myDNA[c]+1
#
print "And the result is\n"
print "A\t",myDNA['A']
print "G\t",myDNA['G']
print "T\t",myDNA['T']
print "C\t",myDNA['C']
pprint(myDNA)
