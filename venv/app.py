from tkinter import *
import tkinter as tk
import tkinter.messagebox
from functools import partial
from back_end import *


def Topup(user):
    topupscreen=tk.Toplevel()
    def exit_btn():

        topupscreen.destroy()
        topupscreen.update()

    close = Button(success, text="close", command=exit_btn)

    if(user.m_type=='C'):
        if(user.m_depends=='Y'):
            label1=Label(topupscreen,text="Please Ask Your Dependant Card To Top Up!")
            label1.grid(row=1)
            close.grid(row=2)
    else:
        L_ask=Label(topupscreen,text="How do You Want To Top Up?")
        def casho():
            go=Label(topupscreen,text="(a cash machine should be available in Starbucks,You Can Top Up via Cash There").pack()
            return
        def credito():
            go=Label(topupscreen,text="Please Enter Credit Card Number : ")
            go.grid(row=3,column=1)
            creditcardNum=StringVar()
            enter=Label(topupscreen,textvariable=creditcardNum)
            enter.grid(row=3,column=2)
            got = Label(topupscreen, text="Please Enter Amount : ")
            got.grid(row=4, column=1)
            credit = StringVar()
            enter1 = Label(topupscreen, textvariable=credit)
            enter.grid(row=4, column=2)
            top=Button(topupscreen,text="Complete Topup")
            top.grid(row=5,column=2)

        B_cash=Button(topupscreen,text="Cash",command=casho)



def ViewInf(user):
    master = tk.Toplevel()

    listbox = Listbox(master)
    listbox.pack()

    listbox.insert(END, "User Name/Password/Name/Address/Telephone/Email/Starcard Number/Credit/Points")

    for item in user.m_accessList:
        listbox.insert(END, item)
    return


def EditInf():
    return


def Purchasewin():
    return


def Logout():
    return


def DeleteUser():
    return


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
    signUpScreen = tk.Toplevel()
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
    s_name = Label(signUpScreen, text="Name : " )
    s_address = Label(signUpScreen, text="Address : ")
    s_tel = Label(signUpScreen, text="Tel : ")
    s_email = Label(signUpScreen, text="E-Mail : ")
    s_snum = Label(signUpScreen, text="StarCard : ")
    s_credit = Label(signUpScreen, text="Credit : ")
    s_type = Label(signUpScreen, text="Type : ")
    s_uname=Label(signUpScreen, text="UserName= ")
    s_pass = Label(signUpScreen, text="Password= ")
    e_name = Entry(signUpScreen, textvariable=d_name)
    e_address = Entry(signUpScreen, textvariable=d_address)
    e_tel = Entry(signUpScreen, textvariable=d_tel)
    e_email = Entry(signUpScreen, textvariable=d_email)
    e_snum = Entry(signUpScreen, textvariable=d_snum)
    e_credit = Entry(signUpScreen, textvariable=d_credit)
    e_type = Entry(signUpScreen, textvariable=d_type)
    e_un = Entry(signUpScreen, textvariable=un)
    e_pass = Entry(signUpScreen, show='*',textvariable=passw)
    ok_Button = Button(signUpScreen, text="Ok",command=createu)
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
    signUpScreen.geometry("500x500")


def Login(username, password):
    uName_found = False
    pass_found = False
    d_uname = username.get()
    d_pass = password.get()

    if d_uname == '' or d_pass == '':
        tkinter.messagebox.showinfo("Wrong Input", "No blank fields are allowed")
        return
    with open("WebUser.txt", "r") as f:
        for line in f:
            line = line[:-1]
            line = line.split('!')
            if d_uname == line[0]:
                uName_found = True
                if d_pass == line[1]:
                    pass_found = True
                break
    if(not uName_found):
        tkinter.messagebox.showinfo("Login", "UserName Does Not Exist Taking to Signup")
        CreateUser()
    elif(not pass_found):
        tkinter.messagebox.showinfo("Login Failed", "Password Does not Match")
    else:
        tkinter.messagebox.showinfo("Login", "Login SuccessFull")
        found = False

        user = 0

        for find_user in memberList:
            if found:
                break
            if d_uname == find_user.m_uName:
                user = find_user
                found = True

        for find_user in employeeList:
            if found:
                break
            if d_uname == find_user.m_uName:
                user = find_user
                found = True

        for find_user in managerList:
            if found:
                break
            if d_uname == find_user.m_uName:
                user = find_user
                found = True

        success = tk.Toplevel()
        View = partial(ViewInf,user)
        Edit = partial(EditInf, user)
        order = partial(Purchasewin, user)
        TopUp = partial(Topup, user)
        lout = partial(Logout, user)
        dele = partial(DeleteUser,user)

        def exit_btn():

            success.destroy()
            success.update()

        view = Button(success, text="View Info",command=View)
        edit = Button(success, text="Edit Info", command=Edit)
        purchase = Button(success, text="Make An Order", command=order)
        loguot = Button(success, text="Logout", command=exit_btn)
        if(user.m_type=='M'):
            deleteb=Button(success, text="Delete Users", command=dele)
        topup = Button(success, text="TopUp Star Card", command=TopUp)
        Welcome = Label(success, text="Welcome Back! " + user.m_uName)
        Welcome.grid(row=1,column=2)
        view.grid(row=2, column=2)
        edit.grid(row=3, column=2)
        purchase.grid(row=4, column=2)
        topup.grid(row=5,column=2)
        if (user.m_type == 'M'):
            deleteb.grid(row=6, column=2)
            loguot.grid(row=7, column=2)
        else:
            loguot.grid(row=6, column=2)
        success.geometry("500x500")

loadRecords()
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
