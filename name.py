import sys

if len(sys.argv)>2:
    sys.exit("Too many arguments")
elif len(sys.argv)<2:
    sys.exit("Too few arguments")

print("Hello, my name is",sys.argv[1])