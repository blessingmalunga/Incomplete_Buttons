from tkinter import *


root = Tk()
root.title("Calculator")
root.config(bg="black")
#root.geometry("400x350")

Ttext = Entry(root,font=('Arial',10),width=50)
Ttext.grid(row=0,column=0,columnspan=8)
#ROW 1
bAc = Button(root,text='AC',fg="blue")
bAc.grid(row=1,column=0,sticky=W,padx=10,pady=10)

#ROW 2
b7 = Button(root,text='7',fg="blue")
b7.grid(row=2,column=0,sticky=W,ipadx=5,padx=10,pady=10)

#ROW 3
b4 = Button(root,text='4',fg="blue")
b4.grid(row=3,column=0,sticky=W,ipadx=5,padx=10,pady=10)


#ROW 4
b1 = Button(root,text='1',fg="blue")
b1.grid(row=4,column=0,sticky=W,ipadx=5,padx=10,pady=10)


#ROW 5
b0 = Button(root,text='0',fg="blue")
b0.grid(row=5,column=0,columnspan=2,sticky=W,ipadx=40,padx=10,pady=10)


root.mainloop()
