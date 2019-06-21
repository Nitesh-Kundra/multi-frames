from tkinter import *

class frame2:

    def __init__(self,wind):
        self.win=wind
        self.win.title("register")

    def addframe1(self):
        self.frame=Frame(self.win)
        self.frame.place(x=30, y=30)

        self.label=Label(self.frame,text="register")
        self.label.grid(row=0,column=0)

        self.win.mainloop()