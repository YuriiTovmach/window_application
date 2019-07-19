from tkinter import *

# root = Tk()
#
# Button(root, text = '1').grid(row = 1, column = 1)
# Button(root, text = '2').grid(row = 1, column = 2)
# Button(root, text = '__3__').grid(row = 2, column = 1, columnspan = 2)
#
# root.mainloop()


root = Tk()

Button(root, text = '1').pack(side = 'left')
Button(root, text = '2').pack(side = 'top')
Button(root, text = '3').pack(side = 'right')
Button(root, text = '4').pack(side = 'bottom')
Button(root, text = '5').pack(fill = 'both')
root.mainloop()

