"""
1. The user is prompted to give a desired number
2. After, user needs to choose which operation will be used
3. Then... another desired number will need to be given
4. If... user typed '=' then give the result, else if... user gave another
   operating symbol... continue solving, else throw an exeption
"""

result = 0

while True:
    n = float(input("Num: >> "))
    opt = str(input("Opt: >> "))

    match opt:
        case '+':
            result += n
            print(result)
        case '-':
            result -= n
            print(result)
        case 'x' | '*':
            result *= n
            print(result)
        case '/':
            if n != 0:
                result /= n
            else:
                result = result
                print("Error: Can't divide by zero...")
                pass
            
            print(result)
        case '=':
            print(f"Result: {result:.2f}")
            break