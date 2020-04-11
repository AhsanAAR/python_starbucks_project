from tkinter import *
import tkinter as tk
import tkinter.messagebox
from functools import partial


def Topup():
    topupscreen=tk.Toplevel()



def Login(username, password):
    i=int(0)
    found=bool(False)
    d_uname = username.get()
    d_pass = password.get()
    d_name=""
    d_address=""
    d_tel=""
    d_email=""
    d_snum=""
    d_credit=""
    d_type=""
    with open("WebUser.txt","r") as f:
        for line in f:
            if(line.find(d_uname)!=-1 and line.find(d_pass)!=-1):
                found=True
            if(found):
                break
    if(not found):
        tkinter.messagebox.showinfo("Login Failed", "Username or Password Does not Match")
    else:
        tkinter.messagebox.showinfo("Login", "Login SuccessFull")
        with open("Records.txt", "r") as f:
            for line in f:
                line = line.split('!')
                if line[0]==d_uname:
                    d_pass = line[1]
                    d_name = line[2]
                    d_address = line[3]
                    d_tel = line[4]
                    d_email = line[5]
                    d_snum = line[6]
                    d_credit = line[7]
                    d_type=line[8]
        success = tk.Toplevel()
        s_uname = Label(success, text="User Name : " + d_uname)
        s_pass = Label(success, text="Password : " + d_pass)
        s_name = Label(success, text="Name : " + d_name)
        s_address = Label(success, text="Address : "+d_address)
        s_tel = Label(success, text="Tel : "+d_tel)
        s_email = Label(success, text="E-Mail : "+d_email)
        s_snum = Label(success, text="StarCard : "+d_snum)
        s_credit = Label(success, text="Credit : "+d_credit)
        s_type = Label(success, text="Type : " + d_type)
        ok_Button = Button(success, text="Close",command=exit)
        s_name.grid(row=2,column=5,sticky=N)
        s_address.grid(row=3, column=5,sticky=N)
        s_tel.grid(row=4, column=5,sticky=N)
        s_email.grid(row=5, column=5,sticky=N)
        s_snum.grid(row=6, column=5,sticky=N)
        s_credit.grid(row=7, column=5,sticky=N)
        s_type.grid(row=8, column=5, sticky=N)
        s_uname.grid(row=9, column=5,sticky=N)
        s_pass.grid(row=10, column=5,sticky=N)
        ok_Button.grid(row=11,column=8,sticky=N)
        success.geometry("500x500")


def getnewuserline(username, password, d_name, d_address, d_tel, d_email, d_snum, d_credit, d_type):
    found = bool(False)
    name =d_name.get()
    address = d_address.get()
    tel = d_tel.get()
    email = d_email.get()
    snum = d_snum.get()
    credit = d_credit.get()
    type=d_type.get()
    uname=username.get()
    passw=password.get()
    with open("WebUser.txt", "r") as f:
        for line in f:
            if (line.find(uname) != -1):
                found = True
            if (found):
                break
    if (found):
        tkinter.messagebox.showinfo("UserName Taken", "Username Already Exist in database Try Login")
    else:
        tkinter.messagebox.showinfo("Creation", "Username is available!")
        line='\n'+uname+'!'+passw+'!'+name+'!'+address+'!'+tel+'!'+email+'!'+snum+'!'+credit+'!'+type+'!'
        line02= '\n'+uname+','+passw+','
        with open("Records.txt", "a") as f:
            f.write(line)
        with open("WebUser.txt", "a") as s:
            s.write(line02)
        tkinter.messagebox.showinfo("Creation", "User Created Successfully!")

def CreateUser():
    success = tk.Toplevel()
    d_name = StringVar()
    d_address = StringVar()
    d_tel = StringVar()
    d_email = StringVar()
    d_snum = StringVar()
    d_credit = StringVar()
    d_type = StringVar()
    un=StringVar()
    passw=StringVar()
    createu = partial(getnewuserline, un, passw, d_name, d_address, d_tel, d_email, d_snum, d_credit, d_type)
    i=int(0)
    s_name = Label(success, text="Name : " )
    s_address = Label(success, text="Address : ")
    s_tel = Label(success, text="Tel : ")
    s_email = Label(success, text="E-Mail : ")
    s_snum = Label(success, text="StarCard : ")
    s_credit = Label(success, text="Credit : ")
    s_type = Label(success, text="Type : ")
    s_uname=Label(success, text="UserName= ")
    s_pass = Label(success, text="Password= ")
    e_name = Entry(success, textvariable=d_name)
    e_address = Entry(success, textvariable=d_address)
    e_tel = Entry(success, textvariable=d_tel)
    e_email = Entry(success, textvariable=d_email)
    e_snum = Entry(success, textvariable=d_snum)
    e_credit = Entry(success, textvariable=d_credit)
    e_type = Entry(success, textvariable=d_type)
    e_un = Entry(success, textvariable=un)
    e_pass = Entry(success, show='*',textvariable=passw)
    ok_Button = Button(success, text="Ok",command=createu)
    s_name.grid(row=2)
    s_address.grid(row=3)
    s_tel.grid(row=4)
    s_email.grid(row=5)
    s_snum.grid(row=6)
    s_credit.grid(row=7)
    s_type.grid(row=8)
    e_name.grid(row=2,column=2)
    e_address.grid(row=3,column=2)
    e_tel.grid(row=4,column=2)
    e_email.grid(row=5,column=2)
    e_snum.grid(row=6,column=2)
    e_credit.grid(row=7,column=2)
    e_type.grid(row=8,column=2)
    e_un.grid(row=9, column=2)
    e_pass.grid(row=10, column=2)
    s_uname.grid(row=9)
    s_pass.grid(row=10)
    ok_Button.grid(row=13,column=8)
    success.geometry("500x500")


login = Tk()
loginf=Frame(login,width=240,height=240)
loginf.pack()
username = StringVar()
password = StringVar()
validatelogin = partial(Login, username, password)
create = partial(CreateUser)
L_UName=Label(loginf, text="Username ",bg="red", fg="white")
L_Pass=Label(loginf, text="Password ",bg="red", fg="white")
L_Img=PhotoImage(file="unnamed.png")
L_login=Label(loginf, image=L_Img)
E_UName= Entry(loginf,textvariable=username)
E_Pass= Entry(loginf,textvariable=password,show="*")
def gob():
    return


Q_Button = Button(loginf, text="Quit", fg="red", command=loginf.quit)
L_Button=Button(loginf, text="Login", fg="blue",command=validatelogin)
C_Button=Button(loginf, text="Create Account", fg="green",command=create)
L_login.grid(row=0,column=1)
L_UName.grid(row=1)
L_Pass.grid(row=2)
E_UName.grid(row=1, column=1)
E_Pass.grid(row=2, column=1)
Q_Button.grid(row=4)
L_Button.grid(row=4, column=4)
C_Button.grid(row=4, column=2)
login.geometry("480x480")
login.mainloop()
