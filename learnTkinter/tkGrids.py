import tkinter as tk

contacts = {
    1 : {
        'name':'Lance Andrei Sombillo',
        'phoneNum':'09935281141'
    }
}

def addRecipient():
    print("I was clicked!")

mainWin = tk.Tk()
mainWin.geometry("420x240")
mainWin.title("Understanding the TkGrids!")

mainWinFrame = tk.Frame(master=mainWin,bd=1,relief="solid", padx=10)
mainWinFrame.pack()

tk.Label(
    mainWinFrame,
    text="Contact Manager",
    font=("Times New Roman", 16, 'bold')
    ).grid(row=0,column=0,columnspan=2, pady=10)
tk.Label(
    mainWinFrame,
    text="First Name:",
).grid(row=1,column=0)
firstName = tk.Entry(
    mainWinFrame,
).grid(row=1, column=1)
tk.Label(
    mainWinFrame,
    text="Last Name:"
).grid(row=2, column=0)
lastName = tk.Entry(
    mainWinFrame,
).grid(row=2, column=1)
tk.Label(
    mainWinFrame,
    text="Phone Number:"
).grid(row=3, column=0)
phoneNum = tk.Entry(
    mainWinFrame,
).grid(row=3, column=1)
addButton = tk.Button(
    mainWinFrame,
    text="ADD Recipient",
    command=addRecipient
).grid(row=4, column=0, columnspan=2, padx=5, pady=10)

mainWin.mainloop()