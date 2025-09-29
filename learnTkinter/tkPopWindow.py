import tkinter as tk

def openSecondWindow():
    mainWindow.withdraw()

    secondWindow = tk.Toplevel(mainWindow)
    secondWindow.geometry("420x240")
    secondWindow.title("Second Window")

    secWinFrame = tk.Frame(master=secondWindow)
    secWinFrame.pack()

    body = tk.Label(
        master=secWinFrame,
        text="Were at the Second Window.",
        font=("Times New Roman", 12),            
                    )
    
    def openMainWindow():
        mainWindow.deiconify()
        secondWindow.destroy()

    button = tk.Button(
        master=secWinFrame,
        text="Go back to Main Window",
        command=openMainWindow
    )
    body.pack(padx=10,pady=10)
    button.pack(side="bottom", padx=10,pady=10)
    

mainWindow = tk.Tk()
mainWindow.geometry("420x240")
mainWindow.title("Windows")

mainWinFrame = tk.Frame(master=mainWindow)
mainWinFrame.pack()

body = tk.Label(
    master=mainWinFrame,
    text="Were at the Main Frame.",
    font=("Times New Roman", 12),            
                )
button = tk.Button(
    master=mainWinFrame,
    text="Go to Second Window",
    command=openSecondWindow
)
body.pack(padx=10,pady=10)
button.pack(side="bottom", padx=10,pady=10)

mainWindow.mainloop()