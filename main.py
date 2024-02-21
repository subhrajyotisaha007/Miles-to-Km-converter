from tkinter import *

window = Tk()
window.minsize(width=100,height=100)
window.title('Mile to Km converter')
window.config(padx=10,pady=10)

#lable
label_01 = Label()
label_01.config(text='is equal')
label_01.grid(row=1,column=0)
label_01.config(padx=10,pady=10)
label_02 = Label()
label_02.config(text='Km')
label_02.grid(row=1,column=2)
label_02.config(padx=10,pady=10)
label_03 = Label()
label_03.config(text='0')
label_03.grid(row=1,column=1)
label_03.config(padx=10,pady=10)
label_04 = Label()
label_04.config(text='Miles')
label_04.grid(row=0,column=2)
label_04.config(padx=10,pady=10)

#entry
inp = Entry(width=10)
inp.grid(row=0,column=1)


#button
def clicked():
    miles = int(inp.get())
    km = round(miles * 1.60934)
    label_03.config(text=str(km))
button = Button()
button.config(text='Calculate',command=clicked)
button.grid(row=2,column=1)
window.mainloop()
button.config(padx=10,pady=10)
