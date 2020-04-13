from tkinter import *
import tkinter as tk
import tkinter.messagebox
from functools import partial
from back_end import *

loadRecords()
k = 0
total = 0

def Topup(user):
    topupscreen=tk.Toplevel()#creation of topup screen and dimention of topup scren
    def exit_btn():#exit function if user selects cash

        topupscreen.destroy()
        topupscreen.update()
    def exit_btn2():#exit function if user Successfully Completes Topup

        user.m_starCard.m_credit+=int(credit.get())
        tkinter.messagebox.showinfo("Top Up Successful", "Your StarCard Has Benn Top Up With "+credit.get()+ " Dhs via Credit Card Number "+creditcardNum.get())
        topupscreen.destroy()
        topupscreen.update()

    def casho():#Cash function for Cash Button
        tkinter.messagebox.showinfo("Cash Deposit", "A cash machine should be available in Starbucks,You Can Top Up via Cash There")
        exit_btn()

    def credito():#Function for credit button
        go.grid(row=3, column=1)
        enter.grid(row=3, column=2)
        got.grid(row=4, column=1)
        enter1.grid(row=4, column=2)
        top.grid(row=5, column=2)
    #Now we Create All The Widgets that are required in our window
    L_ask = Label(topupscreen, text="How do You Want To Top Up?")
    go = Label(topupscreen, text="Please Enter Credit Card Number : ")
    creditcardNum = StringVar()
    enter = Entry(topupscreen, textvariable=creditcardNum)
    credit = StringVar()
    enter1 = Entry(topupscreen, textvariable=credit)
    got = Label(topupscreen, text="Please Enter Amount : ")
    top = Button(topupscreen, text="Complete Topup", command=exit_btn2)
    B_cash = Button(topupscreen, text="Cash", command=casho)
    B_credit = Button(topupscreen, text="Credit", command=credito)
    #As The Button Gets Called The Widgets Are oriented Accordingly


    if(user.m_type=='C'):
        if(user.m_depends):
            tkinter.messagebox.showinfo("Dependant Card", "Please Ask Your Dependant Card To Top Up!")
            exit_btn()
        else:
            L_ask.grid(row=1)
            B_cash.grid(row=2, column=1)
            B_credit.grid(row=2, column=2)
    else:
        L_ask.grid(row=1)
        B_cash.grid(row=2, column=1)
        B_credit.grid(row=2, column=2)
    topupscreen.geometry("640x480")

def ViewInf(user):
    master = tk.Toplevel()
    master.geometry("640x480")
    menulist = 0
    if (user.m_type == 'C'):
        menulist = [user]
    elif (user.m_type == 'E'):
        menulist = [user] + memberList
    elif (user.m_type == 'M'):
        menulist = [user] + memberList + employeeList
    sb = Scrollbar(master, orient=VERTICAL)
    sb.pack(side=RIGHT, fill=Y)
    listbox = Listbox(master,width=300, height=20, yscrollcommand=sb.set)
    sb.config(command=listbox.yview)
    listbox.pack()

    listbox.insert(END, "User Name      /Password       /Name       /Address    /Telephone      /Email      /Starcard Number    /Credit     Dependant       /Points")

    for item in menulist:
        listbox.insert(END, str(item))


def which_selected():
    # print("At {0}".format(select.curselection()))
    return int(select.curselection()[0])


def EditInf(user):

    menulist=0
    if(user.m_type=='C'):
        menulist=[user]
    elif(user.m_type=='E'):
        menulist=[user]+memberList
    elif(user.m_type=='M'):
        menulist = [user] + memberList + employeeList
    def delete_entry():
        q = int(listbox.curselection()[0])
        del menulist[which_selected()]
        listbox.delete(0, END)
        for item in menulist:
            listbox.insert(END, str(item))

    def update_entry():
        q = int(listbox.curselection()[0])
        userr=menulist[q]
        signUpScreen = tk.Toplevel()
        d_name = StringVar()
        d_address = StringVar()
        d_tel = StringVar()
        d_email = StringVar()
        passw = StringVar()

        def udate():
            userr.m_fullName = d_name.get()
            userr.m_address = d_address.get()
            userr.m_telNum = d_tel.get()
            userr.m_email = d_email.get()
            userr.m_password = passw.get()
            tkinter.messagebox.showinfo("Edit", "Details Updated Successfully")
            signUpScreen.destroy()
            signUpScreen.update()

        s_name = Label(signUpScreen, text="Name : ")
        s_address = Label(signUpScreen, text="Address : ")
        s_tel = Label(signUpScreen, text="Tel : ")
        s_email = Label(signUpScreen, text="E-Mail : ")
        s_pass = Label(signUpScreen, text="Password : ")
        e_name = Entry(signUpScreen, textvariable=d_name)
        e_address = Entry(signUpScreen, textvariable=d_address)
        e_tel = Entry(signUpScreen, textvariable=d_tel)
        e_email = Entry(signUpScreen, textvariable=d_email)
        e_pass = Entry(signUpScreen, show='*', textvariable=passw)
        ok_Button = Button(signUpScreen, text="Ok", command=udate)
        s_name.grid(row=2)
        s_address.grid(row=3)
        s_tel.grid(row=4)
        s_email.grid(row=5)
        e_name.grid(row=2, column=2)
        e_address.grid(row=3, column=2)
        e_tel.grid(row=4, column=2)
        e_email.grid(row=5, column=2)
        e_pass.grid(row=10, column=2)
        s_pass.grid(row=10)
        ok_Button.grid(row=13, column=8)
        signUpScreen.geometry("500x500")

    master = tk.Toplevel()
    f1 = Frame(master, width=200, height=200)
    f2 = Frame(master, width=200, height=200)
    f1.grid(row=0)
    f2.grid(row=1)
    sb = Scrollbar(f1, orient=VERTICAL)
    sb.pack(side=RIGHT, fill=Y)
    listbox = Listbox(f1, width=100, height=20, yscrollcommand=sb.set)
    b2 = Button(f2, text="Edit", command=update_entry)
    b3 = Button(f2, text="Delete", command=delete_entry)
    listbox.pack()
    b2.pack()
    if(user.m_type=="M"):
        b3.pack()
    for item in menulist:
        listbox.insert(END, str(item))

def Purchasewin(user):


    def exit_btn():#exit function if user selects cash

        topupscreen.destroy()
        topupscreen.update()


    def checkout():
        global total
        if(user.m_starCard.m_credit>=total):
            user.m_starCard.m_credit -= total
            tkinter.messagebox.showinfo("Order Successful","Your Order Was Successful Please Wait While We PrePare It For You")
            tkinter.messagebox.showinfo("Remaining Balance","Your Remaining Balance is Dhs" + str(user.m_starCard.m_credit))
            exit_btn()
        else:
            tkinter.messagebox.showinfo("Order UnsuccessFul","Your Order Could Not Preceed Due to Insufficient Funds")
            tkinter.messagebox.showinfo("TidBid","TopUp Your Account And Try Again")
            exit_btn()


    def addtocart(items, listbox):
        global k
        if (k != 0):
            listbox.delete(END)
        global total
        total += items.m_price
        i = items.m_itemName + "      " + str(items.m_price)
        listbox.insert(END, i)
        j = "Total : " + str(total)+" Dhs"
        listbox.insert(END, j)
        if (k == 0):
            k += 1
        return

    PurWin = tk.Toplevel()
    f1 = Frame(PurWin, width=200, height=200)
    f2 = Frame(PurWin, width=200, height=200)
    f1.grid(row=0)
    f2.grid(row=1)
    PurWin.geometry("640x480")
    mainmenu = Menu(PurWin)
    PurWin.config(menu=mainmenu)
    itemmenu = Menu(mainmenu)
    mainmenu.add_cascade(label="Add Items", menu=itemmenu)
    sb = Scrollbar(f1, orient=VERTICAL)
    sb.pack(side=RIGHT, fill=Y)
    listbox = Listbox(f1, width=50, height=10, yscrollcommand=sb.set)
    sb.config(command=listbox.yview)
    listbox.pack()
    listbox.insert(END, "Items        Price")
    checkoutbutton = Button(f2, text="Prceed To Checkout", command=checkout)
    checkoutbutton.pack()
    for items in itemsList:
        im = partial(addtocart, items, listbox)
        itemmenu.add_command(label=items.m_itemName + "  " + str(items.m_price), command=im)

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
        crlabel=Label(success,text="Current Balance : "+ str(user.m_starCard.m_credit)+" Dhs ")
        crlabel.grid(row=8,column=2)
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
