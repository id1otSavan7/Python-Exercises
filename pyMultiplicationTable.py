print("==============================")
print("     Welcome to pyTable")
print("==============================")

programStatus = True
while(programStatus):
    x = input("Enter Number: ")
    validateInput = x.isnumeric()

    if validateInput == True:
        x = int(x)
        print("Calculating...")
        y = 1
        i = input("How many iterations? ")
        validateIteration = i.isnumeric()

        if validateIteration:
            i = int(i)

            while(validateIteration):
                for y in range(1, i):
                    y += 1
                    z = x*y
                    print(x , "x" , y, "=", z)
                    if y == i:
                        validateIteration = False
        elif y == "end":
            print("Terminatinf execution of the program...")
            programStatus = False
        else:
            print("Input Invalid try again...")
            continue
    elif x == "end":
        print("Terminating execution of the program...")
        programStatus = False
    else:
        print("Input invalid")
        continue

    print("Try again?")
