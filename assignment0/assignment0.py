#!/usr/bin/python
# Add your code here

# BIZBOARD_TECH: ASSIGNMENT 0
# DANIELLE FEFFER

# 1. set up environment -- DONE
# 2. FizzBuzz problem: Write a program that prints the numbers from 1 to 100. 
#    But for multiples of three print "Fizz" instead of the number and for the 
#    multiples of five print "Buzz". For numbers which are multiples of both three 
#    and five print "FizzBuzz". 
#   
#	Pseudocode: 
# 	1) if num / 3 == num // 3, print Fizz
# 	2) if num / 5 == num // 5, print Buzz
# 	3) else print num
# 	4) print /n
# 	5) num++

def fizzbuzz():
	start = 1
	end = 100

	num = start

	while num <= end:
		if (num % 3 == 0 and num %5 == 0):
			print "FizzBuzz"
		elif num % 3 == 0:
			print "Fizz"
		elif num % 5 == 0:
			print "Buzz"
		else:
			print num
		num += 1

# 3. Write a function that takes one string argument and returns that string
#    with the most common letter swapped for the least common letter
#
# 	Pseudocode: 
# 	1) input string
#	2) cast to lowercase
# 	3) count num of instances of a
# 	4) count num of instances of b
# 	5) if b > a, replace b as MAX
# 	6) go to z, use ascii to figure out which letter is stored in max

def strswap(word):
	wordupper = word.upper()
	curletter = 65
	maxletter = curletter
	minletter = curletter
	MAX = wordupper.count(chr(curletter))
	MIN = MAX
	
	#find the most common letter and the least common letter
	while (curletter < 90):
		curletter = curletter + 1
		curcount = wordupper.count(chr(curletter))
	
		if (curcount > MAX):
			MAX = curcount
			maxletter = curletter
		
		if (0 < curcount < MIN):
			MIN = curcount
			minletter = curletter

	#swap the uppercase most common letter and least common letter
	word = word.replace(chr(maxletter), "X")
	word = word.replace(chr(minletter), chr(maxletter))
	word = word.replace("X", chr(minletter))

	#swap the lowercase most common letter and least common letter
	maxletter += 32
	minletter += 32
	word = word.replace(chr(maxletter), "X")
	word = word.replace(chr(minletter), chr(maxletter))
	word = word.replace("X", chr(minletter))

	#return the new word
	return word

# BIZBOARD_TECH: ASSIGNMENT 0
# DANIELLE FEFFER

# 4. Write a function that will take a number n followed by an
#    arbitrary number of string arguments and return the
#    concatenation of the longest n arguments from longest to
#    shortest. If n is -1, concatenate all of the arguments in this
#    fashion. (Optional: Try passing a non-string argument after
#    the first one. What happens? What are some ways to
#    handle this gracefully?)
#
# 	Pseudocode: 
# 	1) take in n, args, make list
# 	2) if n = -1 case
#	3) concat into new word
#   4) return new word
#
# NOTE ON THE OPTIONAL PART:
# I tried to make the non-string argument into a string by calling (str())
# on that element but it didn't work.  Not really sure why.  Here's what
# I tried:
# for i in args_list:
# 		if (isinstance(i, str) == False):
# 			x = str(i)
# 			args_list[i] = x
# 			args_list[i] = x
# 			print i, "is not a string, but has been converted to one"
# Another way to handle this would be to remove i from the list, but that
# would have made iterations difficult.

def sortconcat(n, *args):
	args_list = list(args)
	args_list.sort(key=len, reverse=True)
	word = ""
	if (n == -1):
		word = word.join(args_list)

	else:
		n_list = args_list[0:n]
		word = word.join(n_list)

	return word

# 5a. DONE
# 5b. Write a Python function that simulates this approach to
#     the Look Away minigame, assuming that Luigi always looks
#     forward and that Mario, Wario, and Peach each randomly
#     choose to look either forward, up, down, left, or right with
#     uniform probability. Your function should take a number of
#     trials to run as input and return the fraction of trials on which
#     Luigi won. You will probably find the random module
#     <http://docs.python.org/library/random.html> useful.
# 5c. Optional
#
# 	Pseudocode: 
# 	1) take in n trials
# 	2) run trials; if a player gets 0, they're out, continue until
#	   until 5 rounds are done, counting how many times a player gets 0 
#	3) return number of wins/number of trials, converting the nums to strs

import random
import fractions

def LookAwayLuigi(ntrials):
	
	mLose = False
	wLose = False
	pLose = False
	wincount = 0

	curtrial = 0
	print ntrials
	while (curtrial < ntrials): #for each trial

		rounds = 0
		while (rounds < 5): #for each round within each trial
			#print "rounds", rounds
			mario = random.randint(0, 4)
			#print mario
			wario = random.randint(0, 4)
			#print wario
			peach = random.randint(0, 4)
			#print peach

			#say that getting 0 = forward = losing
			if (mario == 0):
				mLose = True
			if (wario == 0):
				wLose = True
			if (peach == 0):
				pLose = True

			rounds += 1

		if (mLose and wLose and pLose == True):
			wincount += 1

		curtrial += 1

	return str(wincount) + "/" + str(ntrials)

# 8a. (I assume this was a misnumbering thing so there isn't 
#	  a problem 6 or 7?)
#
#	 Using the urllib and json modules, write a function that will 
#	 get the data for the Quad -> Mass Ave/Garden trip and print 
#	 out the times at which the next three shuttles will leave along 
#	 with the number of minutes between each such time and the 
#	 current time
#
# 	Pseudocode: 
# 	1) somehow download object thing, reading into file, reading into string
# 	2) go through stuff, take out 3 first departures
#	3) format departures
#	4) cast to datetime so things can be subtracted from each other
#	5) print data
#
#	NOTE1: using lists and iterating would have been a better solution.
#	NOTE2: also, my dealing with hour changes is not very graceful here.

import json
import urllib
import datetime
import time

def getStops():
	url = 'http://shuttleboy.cs50.net/api/1.2/trips?a=Quad&b=Mass+Ave+Garden+St&output=json'
	filein = urllib.urlopen(url)  #get data from sit
	
	stringdata = filein.read() #put data in string
	
	#make data python-usable
	stopdata = json.loads(stringdata) 
	format = '%H:%M:%S'
	
	#get first 3 shuttle times
	sh1 = stopdata[0][u'departs']
	sh1 = sh1[11:16]
	
	sh2 = stopdata[1][u'departs']
	sh2 = sh2[11:16]

	sh3 = stopdata[2][u'departs']
	sh3 = sh3[11:16]

	#get current time
	nowmin = time.localtime(time.time())[4]
	nowhr = time.localtime(time.time())[3]
	
	#get differences
	diff1 = int(sh1[3:]) - nowmin
	if diff1 < 0:
		diff1 += 60
	diff1 += 60 * (int(sh1[:2]) - nowhr - 1)

	diff2 = int(sh2[3:]) - nowmin
	if diff2 < 0:
		diff2 += 60
	diff2 += 60 * (int(sh2[:2]) - nowhr - 1)

	diff3 = int(sh3[3:]) - nowmin
	if diff3 < 0:
		diff3 += 60
	diff3 += 60 * (int(sh3[:2]) - nowhr)
	
	#print statements
	print "Current Time:", nowhr, ":", nowmin
	print "Next Shuttle is", diff1,"minutes from now, at", sh1
	print "Following Shuttle is", diff2, "minutes from now, at", sh2
	print "Shuttle after that is", diff3, "minutes from now, at", sh3