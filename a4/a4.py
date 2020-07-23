def is_atom(s):
    if not isinstance(s, str):
        return False
    if s == "":
        return False
    return is_letter(s[0]) and all(is_letter(c) or c.isdigit() for c in s[1:])

def is_letter(s):
    return len(s) == 1 and s.lower() in "_abcdefghijklmnopqrstuvwxyz"

def load(s):
	if len(s) % 2 != 0 and s[1]== '<--':
		if len(s)>2:
			if all(x == '&' for x in s[3::2]):
				return s[::2]
			else:
				return False
		else:
			return s[::2]
	else:
		return False

rules = []
KB = []
isTrue = True;
while isTrue: 

     print("kb> ", end='') 
     command = input()

     if command == "exit":
     	isTrue = False;

     else:
     	tokenized_command = command.split(" ")
     	if tokenized_command[0] == "load":

     		if tokenized_command[1] != "":
     			f = open(tokenized_command[1],"r")
     			counter = 0
     			for x in f:
     				if x.strip('\n').strip(' ')!= '':
     					print(x.strip('\n'))
     					x = x.strip("\n").strip(" ").split(" ")
     					a = load(x)
     					if a == False:
     						print("Error: " + tokenized_command[1] + " is not a valid knowledge base")
     						isTrue = False
     					else:
     						counter = counter + 1;
     						rules.append(a)
     			print(str(counter) + " new rule(s) added")
     			print(rules)
     	else:
     		print("Error: unknown command \""+ tokenized_command[0] + "\"")
     		isTrue = False