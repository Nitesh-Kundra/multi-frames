from tkinter import *
import frame1
import frame2

class main:
    def __init__(self):
        self.win=Tk()
        self.win.geometry("1200x600")
        self.win.title("main")

    def add_menu(self):
        self.mainmenu=Menu(self.win)
        self.win.config(menu=self.mainmenu)

        self.filemenu=Menu(self.mainmenu)
        self.mainmenu.add_cascade(label="file",menu=self.filemenu)

        self.filemenu.add_command(label="frame1", command=self.frame1)
        self.filemenu.add_command(label="frame2", command=self.frame2)

    def add_frame(self):
        self.frame=Frame(self.win)
        self.frame.place(x=30,y=30)

        self.label1= Label(self.frame, text="main")
        self.label1.grid(row=0, column=0)

        self.win.mainloop()

    def frame1(self):
        self.frame.destroy()
        f1=frame1.frame1(self.win)
        f1.addframe()

    def frame2(self):
        self.frame.destroy()
        f2=frame2.frame2(self.win)
        f2.addframe1()

if __name__=="__main__":
    x=main()
    x.add_menu()
    x.add_frame()