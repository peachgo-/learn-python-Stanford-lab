#!/usr/bin/env python3 -tt

#  f = open("test.txt", "r+")

# using "with" to ensure the file will be entered and exited
# no need to call f.close()
with open('test.txt', "r+") as f:
    for line in f.readlines():
        line = line.strip()
        print(line)

f.write("New member\n") # BAD, file has been closed.

