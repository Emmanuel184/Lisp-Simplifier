class lispList:

    def __init__(self) -> None:
        self.right = None
        self.down = None

cons = input().split("'")

for i in range(len(cons[1])):

    if i + 3 < len(cons[1]):
        tempString = cons[1][i] + cons[1][i+1] + cons[1][i+2]

        if (i + 4 < len(cons[1])):
            tempString += cons[1][i + 4]
        

    if i + 3 < len(cons[1]) and cons[1][i] == '(' and cons[1][i + 1] == ' ' and cons[1][i + 2] == '(':
        if i + 4 < len(cons[1]) and cons[1][i + 4] != ")":
            cons[1] = list(cons[1])
            cons[1][i + 1] = ""
            cons[1] = "".join(cons[1])

for i in range(len(cons[2])):

    if i + 3 < len(cons[2]):
        tempString = cons[2][i] + cons[2][i+2] + cons[2][i+2]

        if (i + 4 < len(cons[2])):
            tempString += cons[2][i + 4]
        

    if i + 3 < len(cons[2]) and cons[2][i] == '(' and cons[2][i + 2] == ' ' and cons[2][i + 2] == '(':
        if i + 4 < len(cons[2]) and cons[2][i + 4] != ")":
            cons[2] = list(cons[2])
            cons[2][i + 2] = ""
            cons[2] = "".join(cons[2])
       

cons[1] = list(cons[1])

i = 0

while i < len(cons[1]):

    print("".join(cons[1]))


    if (cons[1][i] == "(" and cons[1][i + 1] != ")") or (i + 1 < len(cons[1]) and cons[1][i] == ")" and cons[1][i - 1] != "("):
        if cons[1][i] == "(":
            cons[1].insert(i + 1, " ")
        elif cons[1][i] == ")":
            cons[1].insert(i, " ")
            i += 1
    i += 1

cons[2] = list(cons[2])

i = 0

while i < len(cons[2]):


    if (cons[2][i] == "(" and cons[2][i + 1] != ")") or  (cons[2][i] == ")" and cons[2][i - 1] != "("):
        if cons[2][i] == "(":
            cons[2].insert(i + 1, " ")
        elif cons[2][i] == ")":
            cons[2].insert(i, " ")
            i += 1
    i += 1

cons[1].insert(len(cons[1]) - 2, " ")
cons[1].pop()

cons[1] = "".join(cons[1])


tabLevel = 0

cons[1] = cons[1].split(" ")


index = 0

while index < len(cons[1]):
    
    if cons[1][index] == "(" or cons[1][index] == ")" or cons[1][index-1] == "(" or cons[1][index - 1] == ")":
        print()
        if cons[1][index] == ")":
            tabLevel += -1
        for j in range(tabLevel):
            print("\t", end="")
    if cons[1][index] == ")":
        print(")")
    elif cons[1][index] == "(":
        tabLevel += 1
        print(cons[1][index])
    else:
        print(f"{cons[1][index]} ", end="")
        if cons[1][index + 1] == ")":
            print()
    
    index += 1

print("--------------------------------------------------------------------------------------------")
    

cons[2] = "".join(cons[2])


tabLevel = 0

cons[2] = cons[2].split(" ")


index = 0

while index < len(cons[2]):

    if len(cons[2]) == 1:
        print(cons[2][0])
        break

    if cons[2][index] == "(" or cons[2][index] == ")" or cons[2][index-1] == "(" or cons[2][index - 1] == ")":
        print()
        if cons[2][index] == ")":
            tabLevel += -1
        for j in range(tabLevel):
            print("\t", end="")
    if cons[2][index] == ")":
        print(")")
    elif cons[2][index] == "(":
        tabLevel += 1
        print(cons[2][index])
    else:
        print(f"{cons[2][index]} ", end="")
        if cons[2][index + 1] == ")":
            print()
    
    index += 1
