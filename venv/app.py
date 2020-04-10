from tkinter import *
import tkinter.messagebox

login = Tk()
loginf=Frame(login,width=240,height=240)
loginf.pack()
L_UName=Label(loginf, text="Username ",bg="red", fg="white")
L_Pass=Label(loginf, text="Password ",bg="red", fg="white")
L_Img=PhotoImage(file="unnamed.png")
L_login=Label(loginf, image=L_Img)
#L_login.place(x=0, y=0, relwidth=1, relheight=1)
E_UName= Entry(loginf)
E_Pass= Entry(loginf)
def gob():
    return
def Login(event):
    i=int(0)
    found=bool(False)
    d_uname = "Mariam"
    d_pass = "Saqer"
    d_name=""
    d_address=""
    d_tel=""
    d_email=""
    d_snum=""
    d_credit=""
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
                d_uname = line[0]
                d_pass = line[1]
                d_name = line[2]
                d_address = line[3]
                d_tel = line[4]
                d_email = line[5]
                d_snum = line[6]
                d_credit = line[7]
        success = Tk()
        s_uname = Label(success, text="User Name : " + d_uname)
        s_pass = Label(success, text="Password : " + d_pass)
        s_name = Label(success, text="Name : " + d_name)
        s_address = Label(success, text="Address : "+d_address)
        s_tel = Label(success, text="Tel : "+d_tel)
        s_email = Label(success, text="E-Mail : "+d_email)
        s_snum = Label(success, text="StarCard : "+d_snum)
        s_credit = Label(success, text="Credit : "+d_credit)
        ok_Button = Button(success, text="Close",command=exit)

        s_name.grid(row=2,column=5,sticky=N)
        s_address.grid(row=3, column=5,sticky=N)
        s_tel.grid(row=4, column=5,sticky=N)
        s_email.grid(row=5, column=5,sticky=N)
        s_snum.grid(row=6, column=5,sticky=N)
        s_credit.grid(row=7, column=5,sticky=N)
        s_uname.grid(row=8, column=5,sticky=N)
        s_pass.grid(row=9, column=5,sticky=N)
        ok_Button.grid(row=11,column=8,sticky=N)
        success.geometry("500x500")
def CreateUser(event):
    i=int(0)
    found=bool(False)
    d_uname = "Mariam"
    d_pass = "Saqer"
    d_name=""
    d_address=""
    d_tel=""
    d_email=""
    d_snum=""
    d_credit=""
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
                d_uname = line[0]
                d_pass = line[1]
                d_name = line[2]
                d_address = line[3]
                d_tel = line[4]
                d_email = line[5]
                d_snum = line[6]
                d_credit = line[7]
        success = Tk()
        s_uname = Label(success, text="User Name : " + d_uname)
        s_pass = Label(success, text="Password : " + d_pass)
        s_name = Label(success, text="Name : " + d_name)
        s_address = Label(success, text="Address : "+d_address)
        s_tel = Label(success, text="Tel : "+d_tel)
        s_email = Label(success, text="E-Mail : "+d_email)
        s_snum = Label(success, text="StarCard : "+d_snum)
        s_credit = Label(success, text="Credit : "+d_credit)
        ok_Button = Button(success, text="Close",command=exit)

        s_name.grid(row=2,column=5)
        s_address.grid(row=3, column=5)
        s_tel.grid(row=4, column=5)
        s_email.grid(row=5, column=5)
        s_snum.grid(row=6, column=5)
        s_credit.grid(row=7, column=5)
        s_uname.grid(row=8, column=5)
        s_pass.grid(row=9, column=5)
        ok_Button.grid(row=11,column=8)
        success.geometry("500x500")


Q_Button = Button(loginf, text="Quit", fg="red", command=loginf.quit)
L_Button=Button(loginf, text="Login", fg="blue",)
L_Button.bind("<Button-1>",Login)
C_Button=Button(loginf, text="Create Account", fg="green",)
C_Button.bind("<Button-1>",CreateUser)
L_login.grid(row=0,column=1)
L_UName.grid(row=1)
L_Pass.grid(row=2)
E_UName.grid(row=1, column=1)
E_Pass.grid(row=2, column=1)
Q_Button.grid(row=4)
L_Button.grid(row=4, column=4)
login.geometry("480x480")
login.mainloop()
