# from tkinter import *

# root = Tk()
#
# Button(root, text = '1').grid(row = 1, column = 1)
# Button(root, text = '2').grid(row = 1, column = 2)
# Button(root, text = '__3__').grid(row = 2, column = 1, columnspan = 2)
#
# root.mainloop()


# root = Tk()
#
# Button(root, text = '1').pack(side = 'left')
# Button(root, text = '2').pack(side = 'top')
# Button(root, text = '3').pack(side = 'right')
# Button(root, text = '4').pack(side = 'bottom')
# Button(root, text = '5').pack(fill = 'both')
# root.mainloop()

from PIL import Image, ImageTk
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label, Style

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Absolute positioning")
        self.pack(fill=BOTH, expand=1)

        Style().configure("TFrame", background="#333")

        bard = Image.open("pyramid_Cheopsa.jpg")
        bardejov = ImageTk.PhotoImage(bard)
        label1 = Label(self, image=bardejov)
        label1.image = bardejov
        label1.place(x=20, y=20)

        rot = Image.open("colossus_Rhodes.jpg")
        rotunda = ImageTk.PhotoImage(rot)
        label2 = Label(self, image=rotunda)
        label2.image = rotunda
        label2.place(x=40, y=160)

        minc = Image.open("temple_Artemidy.jpg")
        mincol = ImageTk.PhotoImage(minc)
        label3 = Label(self, image=mincol)
        label3.image = mincol
        label3.place(x=170, y=50)


def main():

    root = Tk()
    root.geometry("300x280+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
