controlLogic = True

class calculateBMI:
    def __init__(self, height, weight):
        self._height = height
        self._weight = weight

    @property
    def get_remarks(self):
        if self._result < 18.5:
            self._remarks = "Underweight"
        elif self._result < 24.9 and self._result > 18.6:
            self._remarks = "Normal Weight"
        elif self._result < 29.9 and self._result > 25:
            self._remarks = "Overweight"
        elif self._result > 30:
            self._remarks = "Obese"
        
        return (f"You are {self._remarks}. Congratulations!")

    @property
    def get_result(self):
        self._result = (self._weight/(self._height/100) ** 2)
        return self._result
    
class main:
    def decor(func):
        def inner(*args, **kwargs):
            print("=" * 50)
            func(*args, **kwargs)
            print("=" * 50)
        return inner

    @decor
    def displayOutput(result, remarks):
            print(f"BMI Result:\nNumerical Output: {result}\nRemarks: {remarks}")

    @decor
    def displayEntry():
        print("BMI Calculator v1.0")

    def displayQuestionControl():
        return input("Do you want to calculate again [yes/no]? ")

    while controlLogic:
        displayEntry()
        try: 
            height = float(input("Enter height(cm): "))
            weight = float(input("Enter weight(kg): "))

            bmi = calculateBMI(height, weight)
            result = bmi.get_result
            remarks = bmi.get_remarks

            displayOutput(result, remarks)
        except ValueError:
            print("Invalid input, please try again...")
            pass

        cmd = str(displayQuestionControl())
        
        try: 
            if cmd.lower() == "no":
                print("Terminating Program...")
                controlLogic = False
                break
            elif cmd.lower() == "yes":
                print("Restarting prompts, please wait...")
                controlLogic = True
                continue
            else:
                raise ValueError
                
        except ValueError:
            print("Invalid answer, please try again...")
            break
                
            

main()