import random


def chooseRandomly(number):
	opt1 = 0
	opt2 = 0

	for i in range(0, number):
		if (random.randint(0,number) % 2) == 0:
			opt1 += 1
		else:
			opt2 += 1

	if(opt1 > opt2):
		print "opt1 wins"
	else:
		print "opt2 wins"

	return 0


chooseRandomly(1001)