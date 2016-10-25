from sys import argv
from os.path import exists

script, from_file , to_file = argv

print " copyin file from ", from_file, "to file", to_file

from_file_open = open(from_file)
from_file_data = from_file_open.read()

print " from file is %d length long"%len(from_file_data)

print " copy to file exists? %r" %exists(to_file)

to_file_open = open(to_file,'a')
to_file_open.write(from_file_data)
to_file_open.close()
print " new file data"
print open(to_file).read()