def is_atom(s):
    if not isinstance(s, str):
        return False
    if s == "":
        return False
    return is_letter(s[0]) and all(is_letter(c) or c.isdigit() for c in s[1:])

def is_letter(s):
    return len(s) == 1 and s.lower() in "_abcdefghijklmnopqrstuvwxyz"

def load(s):
    if len(s) % 2 != 0 and s[1] == '<--':
        if len(s) > 2:
            if all(x == '&' for x in s[3::2]):
                return s[::2]
            else:
                return False
        else:
            return s[::2]
    else:
        return False

def infer_all(KB,rules):
    new_inferred = []
    stillMore = True
    while(stillMore):
        new = []
        for x in rules:
            if all(elem in KB+new_inferred for elem in x[1:]) and x[0] not in KB+new_inferred:
                    new.append(x[0])
        if new ==[]:
            stillMore = False
        else:
            for k in new:
                new_inferred.append(k)
    return new_inferred


KB = []


isTrue = True
while isTrue:

    print("kb> ", end='')
    command = input()

    if command == "exit":
        isTrue = False

    else:
        tokenized_command = command.split(" ")
        if tokenized_command[0] == "load":
            if tokenized_command[1] != "":
                rules = []
                f = open(tokenized_command[1], "r")
                counter = 0
                for x in f:
                    if x.strip('\n').strip(' ') != '':
                        print(x.strip('\n'))
                        a = load(x.strip("\n").strip(" ").split(" "))
                        if a == False:
                            print(
                                "Error: " + tokenized_command[1] + " is not a valid knowledge base")
                        else:
                            counter = counter + 1
                            rules.append(a)
                print("\n" + str(counter) + " new rule(s) added\n")

        elif tokenized_command[0] == "tell":
            if len(tokenized_command) == 1:
                print("Error: tell needs at least one atom\n")
            else:
                for i in tokenized_command[1:]:
                    if is_atom(i):
                        if i in KB:
                            print("atom \"" + i + "\" already known to be true\n")
                        else:
                            KB.append(i)
                            print("\"" + i + "\" added to KB\n")
                    else:
                        print("\"" + i + "\" is not an atom\n" )
        elif tokenized_command[0] == "infer_all":
            newly_inferred = infer_all(KB,rules)
            if newly_inferred == []:
                print("Newly inferred atoms:\n    <none>")
                print("Atoms already known to be true")
                print("   ", end='')
                print(*KB, sep = ", ")
                print(" ")
            else:
                print("Newly inferred atoms:")
                print("   ", end='')
                print(*newly_inferred, sep = ", ")
                print("Atoms already known to be true")
                print("   ", end='')
                print(*KB, sep = ", ")
                print(" ")
                for i in newly_inferred:
                    KB.append(i)
        else:
            print("Error: unknown command \"" + tokenized_command[0] + "\"")
