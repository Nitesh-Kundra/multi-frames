from tkinter import *

class frame1:

    def __init__(self,wind):
        self.win=wind
        self.win.title("login")

    def addframe(self):
        self.frame=Frame(self.win)
        self.frame.place(x=30,y=30)

        self.labeluser=Label(self.frame, text="username")
        self.labeluser.grid(row=1,column=1)

        self.username=Entry(self.frame)
        self.username.grid(row=1,column=3)

        self.labelpass=Label(self.frame, text="password")
        self.labelpass.grid(row=2,column=1)

        self.password=Entry(self.frame,show="*")
        self.password.grid(row=2,column=3)

        self.win.mainloop()
