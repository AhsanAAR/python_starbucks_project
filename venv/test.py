from back_end import *
from tkinter import *
import tkinter as tk
import tkinter.messagebox
from functools import partial

# [print(item) for item in starCardList]
# print('#')
# [print(item) for item in memberList]
# [print(item) for item in employeeList]
# [print(item) for item in managerList]
# print('#')
# [print(item) for item in itemsList]
k=0

def addtocart(items,listbox):
    global k
    if(k!=0):
        listbox.delete(END)
    global total
    total+=items.m_price
    i=items.m_itemName + "      " + str(items.m_price)
    listbox.insert(END,i)
    j="Total : "+ str(total)
    listbox.insert(END,j)
    if(k==0):
        k+=1
    return

total=0
PurWin=Tk()
f1=Frame(PurWin,width=200,height=200)
f2=Frame(PurWin,width=200,height=200)
f1.grid(row=0)
f2.grid(row=1)
PurWin.geometry("640x480")
mainmenu=Menu(PurWin)
PurWin.config(menu=mainmenu)
itemmenu=Menu(mainmenu)
mainmenu.add_cascade(label="Add Items",menu=itemmenu)
sb = Scrollbar(f1, orient=VERTICAL)
sb.pack(side=RIGHT, fill=Y)
listbox = Listbox(f1,width=50, height=10, yscrollcommand=sb.set)
sb.config(command=listbox.yview)
listbox.pack()
listbox.insert(END, "Items        Price")
checkoutbutton=Button(f2,text="Prceed To Checkout",command=donothing)
checkoutbutton.pack()
for items in itemsList:
    im=partial(addtocart,items,listbox)
    itemmenu.add_command(label=items.m_itemName +"  "+ str(items.m_price),command=im)
PurWin.mainloop()