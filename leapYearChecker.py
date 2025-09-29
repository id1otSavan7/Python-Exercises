progStatus = True #Program Status

while(progStatus): #Loop program if status is True
    year = input("Enter year[Type \"end\" to exit]: ")
    
    validateInput = year.isnumeric()

    if year == "end":
        progStatus = False
        print("Terminating execution of Program...")
    elif validateInput == True: 
        year = int(year)
        #print(type(year))

        if (year % 4) == 0: #Takes Leap Years from years divisible by 4
            if (year % 100) == 0: #Takes in Years that are divisible by 100 which are not Leap Years
                if (year % 400) == 0: #Takes Leap Years from centuries divisible by 400
                    print(year, " is a Leap Year.") 
                else: #If it is not divisible by 400 then...
                    print(year, " is not a Leap Year.")
            else: #If it is not divisible by 100 then...
                print(year , " is a Leap Year.")
        else: #If it is not divisible by 4 then...
            print(year, " is not a Leap Year.")

    else:
        print("Input invalid, Please try again...")
        continue