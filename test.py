#!/usr/bin/env python3
import getopt, sys, argparse
def sum_of_word(word):
    sum = 0
    for char in word:
        sum += ord(char) - 96
    return sum
def main(wordlist, result):
    with open(result, 'w') as result:
        with open(wordlist, 'r') as file:
            for word in file.readlines():
                if sum_of_word(word.strip()) == 100:
                    result.write(word)
#1. sys module
print('the script has the name %s' % (sys.argv[0]))

arguments = len(sys.argv) - 1
print('the script is called with %i arguments' % (arguments))

#output argument-wise
position = 1
while(arguments >= position):
	print("parameter %i: %s" % (position, sys.argv[position]))
	position = position + 1

#2. getopt module
fullCmdArguments = sys.argv
argumentList = fullCmdArguments[1:]
print(argumentList)
unixOptions = 'ho:v'
gnuOptions = ['help', 'output=', 'verbose']

try:
	arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
except getopt.error as err:
	print(str(err))
	sys.exit(2)

for currentArgument, currentValue in arguments:
	if currentArgument in ("-v", "-verbose"):
		print("enabling verbose mode")
	elif currentArgument in ('-h', "--help"):
		print("displaying help")
	elif currentArgument in ("-o", "--output"):
		print(("enabling special output mode (%s)") % (currentValue))

#3. argparse module
text = 'This is a test program. It demonstrates how to use the aparse module with a program description.'
parser = argparse.ArgumentParser(description = text)
parser.parse_args()

if __name__ == '__main__':
    main('words_alpha.txt', 'results.txt')