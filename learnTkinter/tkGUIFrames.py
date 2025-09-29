from tkinter import *

msg = "Lorem ipsum dolor sit amet."

def resize_text(event):
    new_font_size = max(10, event.width // 20)
    body.config(font=("Arial", new_font_size))

window = Tk()
window.geometry("400x200")

mainFrame = Frame(window, bg ="grey") #This is where a frame is instantiated
mainFrame.place(x=0,y=0)

#Will use the variable where we stored the frame by indicating it as its widget's master/parent
navigation = Label(mainFrame, text="This is where the navbar should be...")
header = Label(mainFrame, text="This is where header is...")
body = Label(mainFrame, text= msg, )
footer = Label(mainFrame, text = "This is where footer is...")

navigation.pack(side=TOP, padx=0,pady=10)
header.pack(side=TOP, padx=10, pady=10)
body.pack(fill=BOTH, expand=TRUE,padx=20,pady=20)
footer.pack(side=BOTTOM,padx=10,pady=10)

window.bind("<Configure>", resize_text)
window.mainloop()