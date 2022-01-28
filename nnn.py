from tkinter import *
from tkinter.ttk import *
from time import strftime
root=Tk()
root.title('this clock has been programmed by taha')
def time():
    string=strftime('%H:%B:%C:%D')
    label.config(text=string)
    label.after(1000,time)
label=Label(root,font=("ds_digital",80),background="black",foreground="cyan")
label.pack(anchor='center')
time()
mainloop()