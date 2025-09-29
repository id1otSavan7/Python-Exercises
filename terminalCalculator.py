class Error(Exception):
    pass

class ValueOutOfRange(Error):
    pass

programState = True
output = 0

def op_add(x1, x2):
    result = x1 + x2
    return result

def op_sub(x1, x2):
    result = x1 - x2
    return result

def op_mult(x1, x2):
    result = x1 * x2
    return result

def op_div(x1, x2):
    result = x1 / x2
    return result


print("Welcome to Basic Calculator!\n")
print("This is a Basic Calculator that calculates two integer.")

while(programState):
    try:
        ui_state = True
        ui_x1 = int(input("Enter first integer: "))
        ui_x2 = int(input("Enter second integer: "))

        print("Available Operations")
        operators = ["1: Addition","2: Subtraction","3: Multiplication","4: Division"]
        for values in operators:
                print(values)

        ui_op = int(input("Enter the number of which operator you want to use: "))
        try:
            if ui_op == 0 or ui_op >= 5:
                raise ValueOutOfRange
            elif ui_op == 1:
                output = op_add(ui_x1, ui_x2)
            elif ui_op == 2:
                output = op_sub(ui_x1, ui_x2)
            elif ui_op == 3:
                output = op_mult(ui_x1, ui_x2)
            elif ui_op == 4:
                try:
                    output = op_div(ui_x1, ui_x2)
                except ZeroDivisionError:
                    output = "Error occured: Value was divided to zero"
            
            print("Result: " + str(output))
        except ValueOutOfRange:
            print("Input out of Range...")

    except ValueError:
        print("Invalid input... Please try again and make sure that you put numeric characters only.")

    while(ui_state):
        ui_cont = input("Continue? [yes/no]: ")
        if ui_cont.lower() == "yes":
            print("Restarting conditions...")
            output = 0
            break
        elif ui_cont.lower() == "no":
            print("Terminating Program...")
            programState = False
            break
        else:
            print("Invalid input, please try again.")
            continue  


      

