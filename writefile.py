from sys import argv

script, filename = argv

print "We are going to erase %r." % filename
print "If that doesn't suit you... hit CTRL-C (^ C)"
print "If you do want that, hit RETURN!"

raw_input("? ")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines (in a row no less.)"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

target.write(line1 + "\n" + line2 + "\n" + line3)

print "And finally, we close it"
target.close()