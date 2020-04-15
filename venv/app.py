from tkinter import *
import tkinter as tk
import tkinter.messagebox
from functools import partial
from back_end import *

k = 0
total = 0
currentUser = None
loginScreen = None
panelWindow = None
ViewWindow = None
editWindow = None
editInfoBox = None


def Topup():
    global currentUser
    global panelWindow
    topupscreen=tk.Toplevel()#creation of topup screen and dimention of topup scren
    topupscreen.protocol("WM_DELETE_WINDOW", lambda: exit_btn())
    changePanel(panelWindow, topupscreen, True)
    def exit_btn():#exit function if user selects cash
        activityPanel()
        topupscreen.destroy()
    def exit_btn2():#exit function if user Successfully Completes Topup
        currentUser.m_starCard.m_credit+=int(credit.get())
        tkinter.messagebox.showinfo("Top Up Successful", "Your StarCard Has Benn Top Up With "+credit.get()+ " Dhs via Credit Card Number "+creditcardNum.get())
        topupscreen.destroy()
        activityPanel()
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


    if(currentUser.m_type=='C'):
        if(currentUser.m_depends):
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

def ViewInf():
    global ViewWindow
    global panelWindow
    global currentUser
    ViewWindow = Tk()
    ViewWindow.protocol("WM_DELETE_WINDOW", lambda: changePanel(ViewWindow, panelWindow, True))
    changePanel(panelWindow,ViewWindow)
    ViewWindow.geometry("640x480")
    editList = 0
    if currentUser.m_type == 'C':
        editList = [currentUser]
    elif currentUser.m_type == 'E':
        editList = [currentUser] + memberList
    elif currentUser.m_type == 'M':
        editList = [currentUser] + memberList + employeeList
    def populate(frame):
        col = ['Type','Username','FullName','Address','TelePhoneNumber','E mail','StarCard','Depends','Points']
        for i in range(len(col)):
            t = Label(frame,text = col[i])
            t.grid(row = 0, column = i, padx = 5, pady = 2)
        for i in range(len(editList)):
            col = editList[i].Str()
            for j in range(len(col)):
                Label(frame, text = col[j]).grid(row=1+i, column=j, padx = 5, pady = 2)

    def onFrameConfigure(canvas):
        '''Reset the scroll region to encompass the inner frame'''
        canvas.configure(scrollregion=canvas.bbox("all"))

    canvas = tk.Canvas(ViewWindow, borderwidth=0, background="#ffffff")
    frame = tk.Frame(canvas, background="#ffffff")
    vsb = tk.Scrollbar(ViewWindow, orient="vertical", command=canvas.yview)
    hsb = tk.Scrollbar(ViewWindow, orient="horizontal", command=canvas.xview)
    canvas.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    vsb.pack(side="right", fill="y")
    hsb.pack(side="bottom", fill="x")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4, 4), window=frame, anchor="nw")

    frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

    populate(frame)

def EditInf():
    global currentUser
    global panelWindow
    global editWindow
    editWindow = tk.Toplevel()
    editWindow.protocol("WM_DELETE_WINDOW", lambda: changePanel(editWindow, panelWindow, True))
    changePanel(panelWindow, editWindow)
    editList=0
    if currentUser.m_type=='C':
        editList=[currentUser]
    elif currentUser.m_type=='E':
        editList=[currentUser]+memberList
    elif currentUser.m_type=='M':
        editList = [currentUser] + memberList + employeeList

    def deleteUser(selection):
        if selection == (0,):
            return
        username = listbox.get(selection)
        if currentUser.m_uName == username:
            return
        found = False
        for i in range(len(memberList)):
            if found:
                break
            if memberList[i].m_uName == username:
                del memberList[i]
                found = True
        for i in range(len(employeeList)):
            if found:
                break
            if employeeList[i].m_uName == username:
                del employeeList[i]
                found = True
        editWindow.destroy()
        EditInf()

    def updateUser(selection):
        if selection == (0,):
            return
        username = listbox.get(selection)
        global editInfoBox
        editInfoBox = tk.Toplevel()
        def exitUpdateScreen():
            editInfoBox.destroy()
            EditInf()
        editWindow.protocol("WM_DELETE_WINDOW", lambda: exitUpdateScreen())
        changePanel(editWindow, editInfoBox)
        found = False
        userr = None
        for user in managerList:
            if found:
                break
            if user.m_uName == username:
                userr = user
                found = True
        for user in memberList:
            if found:
                break
            if user.m_uName == username:
                userr = user
                found = True
        for user in employeeList:
            if found:
                break
            if user.m_uName == username:
                userr = user
                found = True
        UserName = StringVar()
        UserName.set(userr.m_uName)
        Name = StringVar()
        Name.set(userr.m_fullName)
        Address = StringVar()
        Address.set(userr.m_address)
        Telephone = StringVar()
        Telephone.set(userr.m_telNum)
        Email = StringVar()
        Email.set(userr.m_email)
        password = StringVar()
        password.set(userr.m_password)

        def udate():
            if Name.get()=='' or Address.get()=='' or Telephone.get()=='' or Email.get() == '' or password.get()=='':
                tkinter.messagebox.showinfo("Wrong Data", "No Empty Fields allowed")
                return
            if  UserName.get() != currentUser.m_uName:
                for user in memberList + employeeList + managerList:
                    if UserName.get() == user.m_uName:
                        if count > 1:
                            tkinter.messagebox.showinfo("Invalid", "This Username is already taken")
                            return
            userr.m_uName = UserName.get()
            userr.m_fullName = Name.get()
            userr.m_address = Address.get()
            userr.m_telNum = Telephone.get()
            userr.m_email = Email.get()
            userr.m_password = password.get()
            tkinter.messagebox.showinfo("Edit", "Details Updated Successfully")
            editInfoBox.destroy()
            editWindow.destroy()
            EditInf()

        label_uName = Label(editInfoBox, text="User Name : ")
        label_Name = Label(editInfoBox, text="Name : ")
        label_Address = Label(editInfoBox, text="Address : ")
        label_TelNum = Label(editInfoBox, text="Tel : ")
        label_Email = Label(editInfoBox, text="E-Mail : ")
        label_Pass = Label(editInfoBox, text="Password : ")
        uNameField = Entry(editInfoBox, textvariable = UserName)
        nameField = Entry(editInfoBox, textvariable=Name)
        addressField = Entry(editInfoBox, textvariable=Address)
        telNumField = Entry(editInfoBox, textvariable=Telephone)
        eMailField = Entry(editInfoBox, textvariable=Email)
        passwordField = Entry(editInfoBox, textvariable=password)
        ok_Button = Button(editInfoBox, text="Ok", command=udate)
        label_Name.grid(row=2)
        label_Address.grid(row=3)
        label_TelNum.grid(row=4)
        label_Email.grid(row=5)
        nameField.grid(row=2, column=2)
        addressField.grid(row=3, column=2)
        telNumField.grid(row=4, column=2)
        eMailField.grid(row=5, column=2)
        if username == currentUser.m_uName:
            label_uName.grid(row=1)
            uNameField.grid(row=1, column=2)
            passwordField.grid(row=10, column=2)
            label_Pass.grid(row=10)
        ok_Button.grid(row=13, column=8)
        editInfoBox.geometry("500x500")

    f1 = Frame(editWindow, width=200, height=200)
    f2 = Frame(editWindow, width=200, height=200)
    f1.grid(row=0)
    f2.grid(row=1)
    sb = Scrollbar(f1, orient=VERTICAL)
    sb.pack(side=RIGHT, fill=Y)
    listbox = Listbox(f1, width=100, height=20, yscrollcommand=sb.set)
    b2 = Button(f2, text="Edit", command= lambda : updateUser(listbox.curselection()))
    b3 = Button(f2, text="Delete", command= lambda : deleteUser((listbox.curselection())))
    listbox.pack()
    b2.pack()
    if(currentUser.m_type=="M"):
        b3.pack()
    listbox.insert(END, "UserName")
    for user in editList:
        listbox.insert(END, user.m_uName)

def Purchasewin():
    global currentUser
    global panelWindow
    PurWin = tk.Toplevel()
    PurWin.protocol("WM_DELETE_WINDOW", lambda: exit_btn())
    changePanel(panelWindow, PurWin, True)

    def exit_btn():#exit function if user selects cash
        PurWin.destroy()
        activityPanel()

    def checkout():
        global total
        if(currentUser.m_starCard.m_credit>=total):
            currentUser.m_starCard.m_credit -= total
            tkinter.messagebox.showinfo("Order Successful","Your Order Was Successful Please Wait While We PrePare It For You")
            tkinter.messagebox.showinfo("Remaining Balance","Your Remaining Balance is Dhs" + str(currentUser.m_starCard.m_credit))
            exit_btn()
        else:
            tkinter.messagebox.showinfo("Order UnsuccessFul","Your Order Could Not Preceed Due to Insufficient Funds")
            tkinter.messagebox.showinfo("TidBid","TopUp Your Account And Try Again")
            exit_btn()

    def addtocart(items, listbox):
        global k
        if k != 0:
            listbox.delete(END)
            listbox.delete(END)
            listbox.delete(END)
        global total
        total += items.m_price
        i = items.m_itemName + "      " + str(items.m_price)
        listbox.insert(END, i)
        j = "Total : " + str(total)+" Dhs"
        listbox.insert(END, j)
        disc = currentUser.discount()
        discprice = total * disc / 100
        j = "After : " + str(disc) + " % discount of " + str(discprice)
        listbox.insert(END, j)
        total = total - discprice
        j = "SubTotal : " + str(total)
        listbox.insert(END, j)
        if k == 0:
            k += 1
        return
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

def CreateUser():
    signUpWindow = tk.Toplevel()
    global loginScreen

    type = 'E'

    changePanel(loginScreen,signUpWindow)
    signUpWindow.protocol("WM_DELETE_WINDOW", lambda: changePanel(signUpWindow,loginScreen,True))

    UserNameString = StringVar()
    NameString = StringVar()
    AddressString = StringVar()
    TeleNumString = StringVar()
    EmailString = StringVar()
    passwordString = StringVar()
    TypeString = StringVar()
    TypeString.set('Employee')

    label_uName = Label(signUpWindow, text="User Name : ")
    label_Name = Label(signUpWindow, text="Name : ")
    label_Address = Label(signUpWindow, text="Address : ")
    label_TeleNum = Label(signUpWindow, text="Tel : ")
    label_Email = Label(signUpWindow, text="E-Mail : ")
    label_Password = Label(signUpWindow, text="Password :  ")
    label_Type = Label(signUpWindow, text="Type :  ")

    uNameField = Entry(signUpWindow, textvariable=UserNameString)
    NameField = Entry(signUpWindow, textvariable=NameString)
    AddressField = Entry(signUpWindow, textvariable=AddressString)
    TelNumField = Entry(signUpWindow, textvariable=TeleNumString)
    EmailField = Entry(signUpWindow, textvariable=EmailString)
    PasswordField = Entry(signUpWindow, textvariable=passwordString)
    TypeField = Entry(signUpWindow, textvariable = TypeString, state = 'disabled')

    button_Employee = Button(signUpWindow, text="Employee", command=lambda : sete())
    button_Manger = Button(signUpWindow, text="Manager", command=lambda : setm())
    button_Customer = Button(signUpWindow, text="Customer", command=lambda : setc())

    label_uName.grid(row = 1)
    label_Name.grid(row=2)
    label_Address.grid(row=3)
    label_TeleNum.grid(row=4)
    label_Email.grid(row=5)
    label_Password.grid(row = 6)
    label_Type.grid(row = 7)

    uNameField.grid(row=1,column=2)
    NameField.grid(row=2, column=2)
    AddressField.grid(row=3, column=2)
    TelNumField.grid(row=4, column=2)
    EmailField.grid(row=5, column=2)
    PasswordField.grid(row=6, column=2)
    TypeField.grid(row=7,column=2)

    button_Employee.grid(row=7, column=3)
    button_Manger.grid(row=7, column=4)
    button_Customer.grid(row=7, column=5)

    ok_Button = Button(signUpWindow, text="Ok",command= lambda : addUser())
    ok_Button.grid(row=13, column=3)
    signUpWindow.geometry("500x500")

    def addUser():
        global currentUser
        if (UserNameString.get() == '' or NameString.get() == '' or AddressString.get() == ''
                or TeleNumString.get() == '' or EmailString.get() == '' or
                PasswordField.get() == '' or type == ''):
            tkinter.messagebox.showinfo("Invalid","No Blank Fields Allowed")
            return
        for user in memberList + employeeList + managerList:
            if user.m_uName == uNameField.get():
                tkinter.messagebox.showinfo("Wrong Username", "This Uesrname is already in use")
                return
        myStarCard = newStarCard()
        starCardList.append(myStarCard)
        if type == 'C':
            currentUser = member(UserNameString.get(), passwordString.get(), NameString.get(), AddressString.get(),
                                 TeleNumString.get(), EmailString.get(), myStarCard.m_cardNum, False, 0)
            memberList.append(currentUser)
        elif type == 'E':
            currentUser = basic_employee(UserNameString.get(), passwordString.get(), NameString.get(), AddressString.get(),
                                 TeleNumString.get(), EmailString.get(), myStarCard.m_cardNum)
            employeeList.append(currentUser)
        else:
            currentUser = manager(UserNameString.get(), passwordString.get(), NameString.get(),
                                         AddressString.get(),
                                         TeleNumString.get(), EmailString.get(), myStarCard.m_cardNum)
            managerList.append(currentUser)
        tkinter.messagebox.showinfo("User Created", "Your Account has Successfully been Crated. Login with your details")
        writeToFiles()
        changePanel(signUpWindow, loginScreen, True)

    def sete():
        global type
        type = 'E'
        TypeString.set('Employee')

    def setc():
        global type
        type = 'C'
        TypeString.set('Customer')

    def setm():
        global type
        type = 'M'
        TypeString.set('Manager')

def activityPanel():
    global panelWindow
    global loginScreen
    panelWindow = tk.Toplevel()
    changePanel(loginScreen,panelWindow)
    panelWindow.protocol("WM_DELETE_WINDOW", lambda : logOut())
    def logOut():
        writeToFiles()
        changePanel(panelWindow,loginScreen,True)

    button_viewInfo = Button(panelWindow, text="View Info", command = lambda : ViewInf())
    button_editInfo = Button(panelWindow, text="Edit Info", command = lambda : EditInf())
    button_purchase = Button(panelWindow, text="Make An Order", command = lambda : Purchasewin())
    button_LogOut = Button(panelWindow, text="Logout", command = lambda : logOut())
    button_TopUp = Button(panelWindow, text="TopUp Star Card", command = lambda : Topup())
    label_welcome = Label(panelWindow, text="Welcome Back! ")
    label_credits = Label(panelWindow, text="Current Balance : " + str(currentUser.m_starCard.m_credit) + " Dhs ")
    label_welcome.pack(pady = 10)
    button_viewInfo.pack(pady = 10)
    button_editInfo.pack(pady = 10)
    button_purchase.pack(pady = 10)
    button_TopUp.pack(pady = 10)
    button_LogOut.pack(pady = 10)
    label_credits.pack(pady = 10)
    panelWindow.geometry("500x500")

def changePanel(first,second, destroy = False):
    first.withdraw()
    second.deiconify()
    if destroy:
        first.destroy()

def checkLogInData(username, password):
    found_username = False
    found_password = False

    if username == '' or password == '':
        tkinter.messagebox.showinfo("Wrong Input", "No blank fields are allowed")
        return
    # finds the username and password in Records.txt
    with open("WebUser.txt", "r") as f:
        for line in f:
            line = line[:-1]
            line = line.split('!')
            if username == line[0]:
                found_username = True
                if password == line[1]:
                    found_password = True
                break
    if not found_username:
        tkinter.messagebox.showinfo("Login", "UserName Does Not Exist Taking to Signup")
        CreateUser()
    elif not found_password:
        tkinter.messagebox.showinfo("Login Failed", "Password Does not Match")
    else: # the username and password have been found
        tkinter.messagebox.showinfo("Login", "Login SuccessFull")
        found = False
        # find the object for the username and password
        for find_user in memberList + employeeList + managerList:
            if found:
                break
            if username == find_user.m_uName:
                global currentUser
                currentUser = find_user
                found = True
        activityPanel()

#the main Login Screen loop
def startUp():
    global loginScreen
    loginScreen = Tk()
    loginFrame = Frame(loginScreen,width=240,height=240)
    loginFrame.pack()
    username = StringVar()
    password = StringVar()
    label_username = Label(loginFrame, text="Username ",bg="red", fg="white")
    label_password = Label(loginFrame, text="Password ",bg="red", fg="white")
    backImage = PhotoImage(file="unnamed.png")
    label_login = Label(loginFrame, image=backImage)
    usernameField = Entry(loginFrame,textvariable=username)
    passwordField= Entry(loginFrame,textvariable=password,show="*")
    button_quit = Button(loginFrame, text="Quit", fg="red",command=loginScreen.quit)
    button_login = Button(loginFrame, text="Login", fg="blue",command=lambda :checkLogInData(username.get(), password.get()))
    button_create = Button(loginFrame, text="Create Account", fg="green",command=CreateUser)
    label_login.grid(row=0,column=1)
    label_username.grid(row=1)
    label_password.grid(row=2)
    usernameField.grid(row=1, column=1)
    passwordField.grid(row=2, column=1)
    button_quit.grid(row=4)
    button_login.grid(row=4, column=4)
    button_create.grid(row=4, column=2)
    loginScreen.geometry("480x480")
    loginScreen.mainloop()