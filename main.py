import tkinter
from tkinter import  *

window = tkinter.Tk()
window.title('UI')
window.minsize(width=500, height=400)
window.config(padx=100,pady=200)

#label
my_label = tkinter.Label(text='I am a label', font=('Arial',24,'bold'))
my_label.grid(row=0,column=0)
my_label.config(pady=20,padx=20)

my_label['text'] = 'hello'
my_label.config(text='hi')

#button
def clicked():
    my_label.config(text= inp.get())
def Notclicked():
    my_label.config(text='text')

button = Button(text='click me', command=clicked)
button.grid(row=1,column=1)

button2 = Button(text='notclick me', command=Notclicked)
button2.grid(row=0,column=2)

#entry
inp = Entry(width=10)
inp.grid(row=2,column=3)





window.mainloop()