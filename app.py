#!/usr/bin/python
import sys

# Implementation of FizzBuzz v2.00

# Version 2: if number is prime, print "<number> is a prime" instead
#            Take one argument,  and count up to it

class FizzBuzz():
    def __init__(self):
        pass

    # Run from 1 to "end", which is the given number.
    def run(self, end, out=sys.stdout):
        for i in range(1, end + 1):
		for x in range(2, i):
			if (x == (i - 1)):
				print i, "is a prime"
			elif ((i % x) == 0):
				break
			else:
				continue

    # Seems to give correct values. Tested with 1 and 2.
    def calc(self, i):
        return i

if __name__ == "__main__":
    app = FizzBuzz()
    app.run(int(sys.argv[1]))
