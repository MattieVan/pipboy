#-------------------------------------------------------------------------------
# Name:        Pip Boy
# Purpose:
#
# Author:      Vanhonsebrouck
#
# Created:     14/03/2018
# Copyright:   (c) Vanhonsebrouck 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

from tkinter import *

root = Tk()
var = StringVar()
label_one = Label(root,
         textvariable=var,
         bg="black",
         fg="green2",
         font=("Courier", 60, "bold"))
var.set("Pip Boy")
root.configure(background='black')
label_one.pack()

f = Frame(height=50, width=300)
f.pack_propagate(0)
f.pack()

b = Button(f,
         text="Heart Rate Monitor",
         bg="grey",
         fg="green2",
         font=("Courier", 20, "bold"))
b.pack(fill=BOTH, expand=1)

root.mainloop()

