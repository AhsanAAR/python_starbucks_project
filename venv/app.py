from tkinter import *
import tkinter.messagebox

login = Tk()
loginf=Frame(login)
loginf.pack()
L_UName=Label(loginf, text="Username ",bg="red", fg="white")
L_Pass=Label(loginf, text="Password ",bg="red", fg="white")
L_login=Label(loginf, text="Login To Starbucks",fg="white", bg="green")
E_UName= Entry(loginf)
E_Pass= Entry(loginf)
def gob():
    return
def Login(event):
    i=int(0)
    found=bool(False)
    d_uname = "ali2faraz"
    d_pass = "221bbaker"
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
                if(line.find(d_uname)!=-1):
                    while(line[i]!='!'):
                        i=i+1
                    i+=1
                    while(line[i]!='!'):
                        d_name=d_name+line[i]
                        i+=1
                    i += 1
                    while (line[i] != '!'):
                        d_address = d_address + line[i]
                        i += 1
                    i += 1
                    while (line[i] != '!'):
                        d_tel = d_tel + line[i]
                        i += 1
                    i += 1
                    while (line[i] != '!'):
                        d_email = d_email + line[i]
                        i += 1
                    i += 1
                    while (line[i] != '!'):
                        d_snum = d_snum + line[i]
                        i += 1
                    i += 1
                    while (line[i] != '!'):
                        d_credit = d_credit + line[i]
                        i += 1
                    break
        success = Tk()
        s_name = Label(success, text="Name : "+d_name)
        s_address = Label(success, text="Address : "+d_address)
        s_tel = Label(success, text="Tel : "+d_tel)
        s_email = Label(success, text="E-Mail : "+d_email)
        s_snum = Label(success, text="StarCard : "+d_snum)
        s_credit = Label(success, text="Credit : "+d_credit)
        ok_Button = Button(success, text="Close",command=success.quit)
        s_name.grid(row=2,column=5)
        s_address.grid(row=3, column=5)
        s_tel.grid(row=4, column=5)
        s_email.grid(row=5, column=5)
        s_snum.grid(row=6, column=5)
        s_credit.grid(row=7, column=5)
        ok_Button.grid(row=10,column=8)
        success.geometry("800x600")


Q_Button = Button(loginf, text="Quit", fg="red", command=loginf.quit)
#Q_Button.bind("<Button-1>",loginf.quit)
L_Button=Button(loginf, text="Login", fg="blue",)
L_Button.bind("<Button-1>",Login)
L_login.grid(row=0,column=1)
L_UName.grid(row=1)
L_Pass.grid(row=2)
E_UName.grid(row=1, column=1)
E_Pass.grid(row=2, column=1)
Q_Button.grid(row=4)
L_Button.grid(row=4, column=4)
login.geometry("240x240")
login.mainloop()
