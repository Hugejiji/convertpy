from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding = 10)
frm.grid()
ttk.Label(frm,text="Hello, BItch!").grid(column=0,row=0)
ttk.Label(frm,text="SUCK IT, BItch!").grid(column=0,row=0)

ttk.Button(frm,text="QUIT", command=root.destroy).grid(column=1,row=1)

# call loop
root.mainloop()
