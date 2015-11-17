# http://learnpythonthehardway.org/book/ex17.html

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))

# we could do these two on one line, how?
in_data = open(from_file).read()

print("The input file is %d bytes long" % len(in_data))

print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'a')
out_file.write(in_data)

print("Alright, all done.")

out_file.close()
# from_file.close()
