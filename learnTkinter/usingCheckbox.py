from tkinter import *

self._roots = Tk()
self._roots.title("Question. Can you answer?")

qst = "What do you think is the best programming language?"
defFontValue = ('Times New Roman', 12)

choice = [1, 2, 3, 4]

def submitAnswer():
    for i in range(len(choice)):
        cc = choice.get()
    
    if cc[0] == 1:
        print(f"You chose {choice[0]}")
    elif cc[1] == 1:
        print(f"You chose {choice[1]}")
    elif cc[2] == 1:
        print(f"You chose {choice[2]}")
    elif cc[3] == 1:
        print(f"You chose {choice[3]}")
    elif cc[0:] == 1:
        print("You are a real mad programmer!")
    else:
        print("You don't want that? Fine...")
       

titleHeader = Label(
    self._roots, 
    text = "Question. Can you answer?",
    font = ("Times New Roman", 16, 'bold'),
    justify= LEFT,
)

question = Label(
    self._roots,
    text = qst,
    font = defFontValue
)

firstChoice = Checkbutton(
    self._roots,
    text = "Java",
    variable = choice[0],
    onvalue= 1,
    offvalue= 0,
    font = defFontValue,
)

secChoice = Checkbutton(
    self._roots,
    text = "Python",
    variable = choice[1],
    font = defFontValue,
    onvalue = 1,
    offvalue = 0
)

thirdChoice = Checkbutton(
    self._roots,
    text = "C#",
    variable = choice[2],
    font = defFontValue,
    onvalue = 1,
    offvalue = 0
)

fourthChoice = Checkbutton(
    self._roots,
    text = "C++",
    variable = choice[3],
    font = defFontValue,
    onvalue = 1,
    offvalue = 0
)

submitButton = Button(
    self._roots,
    text = "SUBMIT",
    font = defFontValue,
    command = lambda : submitAnswer()
)

titleHeader.pack()
question.pack()
firstChoice.pack()
secChoice.pack()
thirdChoice.pack()
fourthChoice.pack()
submitButton.pack()

self._roots.mainloop()

