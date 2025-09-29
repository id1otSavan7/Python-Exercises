#Basic user input:
name = input("Enter your name: ")

print("Welcome " + name + ", this is python!")

#Using if... and else conditions
language = ['Filipino','Japanese','Chinese','Korean','English']

status = True

for value in language:
        print(value)

while(status):

    choice = input("What language do you speak?: ")

    if choice == language[0]:
        print("Ah sige sige, tangina mo.")
    elif choice == language[4]:
        print("Hello bitch!")
    else: 
        print("Ahaha, yeah...")

    state = input("Would you like to chat more?[Yes/No]: ")
    if state.lower() == "no":
        print("Yeah, fuck you too!")
        status = False
    elif state.lower() == "yes":
        print("Shit, here we go again. Actually I'm done... Fuck off!")
        status = False
    else: 
         print("It's a simple question, answer me correctly next time...")
         status = False
