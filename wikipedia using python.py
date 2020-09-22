




from tkinter import *
import wikipedia
from tkinter.messagebox import showinfo    

window = Tk()
window.title("Wikipedia")
window.geometry('200x70')


def searching():
    search = enter.get()
    answer = wikipedia.summary(search)
    print(answer)
    showinfo("Wikipedia Answer",answer)



label1 = Label(window,text="wikipedia search...")
label1.grid(row=0,column=0)

enter = Entry(window)
enter.grid(row=1,column=0)

button = Button(window,text="search",command=searching)
button.grid(row=3,column=0)



window.mainloop()