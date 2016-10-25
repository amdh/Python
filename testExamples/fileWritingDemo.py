from sys import argv

script, filename = argv
print "we are goin to erase the file %s"% filename

print "file is opened"
file_open  = open(filename,'w')

file_open.truncate()
print "file is erased"

print " write new lines to the file"
line1 = raw_input("give line1:")
line2 = raw_input("giv line 2:")
line3 =  raw_input("give line3:")

print "writing these lines to the file"

file_open.write(line1)
file_open.write("\n")
file_open.write(line2)
file_open.write("\n")
file_open.write(line3)
file_open.write("\n")

print " wrting done .file closed"
file_open.close()

print open(filename).read()