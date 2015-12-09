Names = "Names.txt"
"""infile = open(Names,'r')
print(infile.readline())
infile.close()"""

infile = open(Names,'r')
Alpha = infile.readlines()

for i in sorted(Alpha):
    print (i)
infile.close()
