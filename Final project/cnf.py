import random

k = 5
m = 100
n = 50

fo = open("cnf", "w")
for i in range(m):
	boolean = random.choice(["","-"])
	a = random.randint(1,n)
	string = boolean+str(a)
	for i in range(k-1):
	  booleanb = random.choice(["","-"])
	  b = random.randint(1,n)
	  string = string + " " + booleanb+str(b)
	fo.write(string+" 0\n")
fo.close()