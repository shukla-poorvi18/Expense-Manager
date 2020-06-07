from tkcalendar import Calendar 
from tkinter import *
from sqlite3 import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import os
import csv
import datetime
import operator
import functools
from functools import partial
import test
class abc:

    ########################################################################LOGIN PAGE#########################################################
    def login(s):
        try:
            s.scr.destroy()
        except:
            pass
        #d=datetime.datetime.today()
        
        screen=Tk()
        screen.state("zoomed")
        screen.title("Login/Registration Window")
        #screen.geometry('1350x6750+0+0')
        screen.geometry("1900x900")
        screen.configure(background="sea green")
        s.client=connect(r"user.db")
        s.cur=s.client.cursor()
        s.backup()
        
        s.scr=screen
        s.l=Label(s.scr,bd=18,text='EXPENSE MANAGER',pady=5,font=('aerial',30,'bold'),bg='orange',fg='black',justify=CENTER,relief=GROOVE)
        s.l.pack(fill=X,side=TOP)
        s.f1=Frame(s.scr,bg='grey',bd=15,height=500,width=500,relief=GROOVE)
        s.f1.place(x=100,y=150)
        s.l1=Label(s.f1,fg='black',text='UserName',font=('times',20,'bold'),bg='orange')
        s.l1.place(x=30,y=60)
        s.e1=Entry(s.f1,fg='black',font=('times',20,'bold'),bg='orange')
        s.e1.place(x=180,y=60)
        s.l2=Label(s.f1,fg='black',text='Password',font=('times',20,'bold'),bg='orange')
        s.l2.place(x=30,y=180)
        s.e2=Entry(s.f1,show='*',fg='black',font=('times',20,'bold'),bg='orange')
        s.e2.place(x=180,y=180)
        s.b1=Button(s.f1,bd=10,fg='black',text='Login',padx=16,pady=1,font=('times',20,'bold'),width=6,bg='orange',relief=RAISED,command=lambda:s.result("login"))
        s.b1.place(x=70,y=300)
        s.b3=Button(s.f1,bd=10,fg='black',text='Register',padx=16,pady=1,font=('times',20,'bold'),width=6,bg='orange',relief=RAISED,command=s.register)
        s.b3.place(x=280,y=300)
        s.canvas=Canvas( s.scr,bd=2,bg="black",height=480,highlightcolor="BLUE",relief=GROOVE,width=450)
        s.canvas.place(x=800,y=150)
        filename =PhotoImage(file ="money.png")
        image = s.canvas.create_image(490,-3, anchor=NE, image=filename)
        s.scr.mainloop()
    #################################################################REGISTER PAGE########################################################
        
    def register(s):
        try:
            s.scr.destroy()
        except:
            pass
        s.scr=Tk()
        s.scr.geometry("1900x900")
        s.scr.state("zoomed")
        s.scr.configure(background="sea green")
        s.l=Label(s.scr,bd=18,text='EXPENSE MANAGER',pady=5,font=('aerial',30,'bold'),bg='orange',fg='black',justify=CENTER,relief=GROOVE)
        s.l.pack(fill=X,side=TOP)
        s.f2=Frame(s.scr,bg='grey',bd=15,height=500,width=500,relief=GROOVE)
        s.f2.place(x=700,y=150)
        s.l3=Label(s.f2,text='Name',font=('times',20,'bold'),bg='orange')
        s.l3.place(x=30,y=40)
        s.e3=Entry(s.f2,font=('times',20,'bold'),bg='orange')
        s.e3.place(x=180,y=40)
        s.l4=Label(s.f2,text='email',font=('times',20,'bold'),bg='orange')
        s.l4.place(x=30,y=110)
        s.e4=Entry(s.f2,font=('times',20,'bold'),bg='orange') 
        s.e4.place(x=180,y=110)
        s.l5=Label(s.f2,text='Password',font=('times',20,'bold'),bg='orange')
        s.l5.place(x=30,y=180)
        s.e5=Entry(s.f2,font=('times',20,'bold'),bg='orange',show='*')
        s.e5.place(x=180,y=180)
        s.l6=Label(s.f2,text='confirm',font=('times',20,'bold'),bg='orange')
        s.l6.place(x=30,y=250)
        s.e6=Entry(s.f2,font=('times',20,'bold'),bg='orange',show='*')
        s.e6.place(x=180,y=250)
        s.l7=Label(s.f2,text='username',font=('times',20,'bold'),bg='orange')
        s.l7.place(x=30,y=320)
        s.e7=Entry(s.f2,font=('times',20,'bold'),bg='orange')
        s.e7.place(x=180,y=320)
        s.b2=Button(s.f2,bd=10,text='Register',padx=16,pady=1,font=('times',20,'bold'),bg='orange',relief=RAISED,command=lambda:s.result("register"))
        s.b2.place(x=200,y=390)
        s.canvas=Canvas( s.scr,bd=2,bg="black",height=480,highlightcolor="BLUE",relief=GROOVE,width=450)
        s.canvas.place(x=100,y=150)
        filename =PhotoImage(file ="money.png")
        image = s.canvas.create_image(0,-3, anchor=NW, image=filename)
        s.scr.mainloop()
    #######################################################LOGIN AND REGISTER FUNCTION########################################################  
    def result(s,val):
        if val=="login":
            if not len(s.e1.get()) or not len(s.e2.get()): # login details not given
                messagebox.showinfo("Invalid credentials","Please fill both the fields to continue.\nPlease try again.")
            else:  #check for correct username
                x=s.cur.execute("select count(*) from user where username=%r"%(s.e1.get()))
                if list(x)[0][0]==0:  #entered username doesn't exist
                    messagebox.showinfo("Invalid credentials.","Username %r doesn't exist.\nPlease 'register' to continue."%(s.e1.get())) #wrong username
                
                    s.register()
                else:  #username exists, check for correct password now
                    x=s.cur.execute("select count(*) from user where password=%r"%(s.e2.get())) #checking for correct password
                    if list(x)[0][0]:       # correct password, grant access to order.
                        print("you logged in successfully")
                        s.username=s.e1.get()
                        s.scr.destroy()
                        s.mainpage()
                        #s.expense()
                    else:                  # wrong password
                        messagebox.showinfo("Wrong password","Please enter a valid password\nForgot password ?")
                        s.rbutton=Button(s.scr,bd=10,fg='black',text='Forget Password',padx=16,pady=1,font=('times',20,'bold'),width=6,bg='orange',relief=RAISED,command=s.recover_password)
                        #s.rbutton=Button(s.scr,text='forget password',command=s.recover_password)
                        s.rbutton.place(x=250,y=550,width=260,height=60)
                        
        elif val=="register":
            if not len(s.e3.get()) or not len(s.e4.get()) or not len(s.e5.get()) or not len(s.e6.get()) or not len(s.e7.get()):# no username given
                messagebox.showinfo("Missing details","Please fill all the fields to continue.")
            else:                           #check for validity of data
                if s.e5.get()==s.e6.get(): #both passwords are same,check for availability of username.
                    if re.search(r'\w+@+\w+.+\w',s.e4.get()):
                        x=s.cur.execute("select count(*) from user where username=%r"%(s.e7.get()))
                        if list(x)[0][0]!=0:   # username already taken.
                            messagebox.showinfo("Oops !","Username %r already exists.\nPlease try another one."%(s.e3.get())) 
                        else:                   # username available.
                            try:
                                s.cur.execute("insert into user values(%r,%r,%r,%r)"%(s.e3.get(),s.e7.get(),s.e4.get(),s.e5.get()))
                                s.client.commit()
                                messagebox.showinfo("Info","You've been successfully registered\nRedirecting to LOGIN window")
                                
                                s.login() #registration done.... redirect to 'login' window
                            except:
                                 pass
                    else:
                        messagebox.showinfo("Oops !","invalid email")
                else:                     #passwords aren't same...reconstruct the 'register' window
                    messagebox.showinfo("Mismatched passwords","Both passwords should be same\nPlease try again.")

        ##########################################################################FORGET PASSWORD FUNCTION###################################################
    def recover_password(s):
        
        try:
            mail=list(s.cur.execute("select email from user where username=%r and name=%r"%(s.e7.get(),s.e3get())))[0][0]
            print('email id is ',mail)
            s.mail=mail
            password=list(s.cur.execute("select password from user where name=%r"%(s.e3.get())))[0][0]
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            print('connected to gmail')
            server.login('meghaairan14@gmail.com','9580170977')
            print('logged in')
            msg='Hello '+e3.get()+'\nYour password for Expense Manager is '+''+password+''
            server.sendmail('meghaairan14@gmail.com',mail,msg)
            print('mail sent')
            server.close()
            messagebox.showinfo('Info','Dear '+e3.get()+', your password has been sent to '+mail+'\nPlease try again using the correct password.')
        except:
            messagebox.showinfo('Error',"Your password couldn't be sent.Please check your internet connection.")

            
    def submit(s,b):
            try:
                if s.date!=None:
                    pass
                else:
                    messagebox.showinfo("Missing Details","Please select a valid date")
            except:
                messagebox.showinfo("Missing Details","Please select a valid date")
                return
            if len(s.e.get())==0:
                messagebox.showinfo("Missing Details","Please fill a valid amount")
                return
            if len(s.username)==0:
                messagebox.showinfo("Missing Details","invalid user")
                return
            if 1==1:
                s.cur.execute('insert into expense (ex_name,amount,date,name,month) values("{0}",{1},"{2}","{3}",{4})'.format(b,int(s.e.get()),s.date,s.username,int(str(s.date)[5:7])))
                s.client.commit()
                s.scr.destroy()
                messagebox.showinfo('Info','Records have been INSERTED successfully')
    def submit1(s,b):
            try:
                if s.date!=None:
                    pass
                else:
                    messagebox.showinfo("Missing Details","Please select a valid date")
            except:
                messagebox.showinfo("Missing Details","Please select a valid date")
                return
            if len(s.e.get())==0:
                messagebox.showinfo("Missing Details","Please fill a valid amount")
                return
            if len(s.username)==0:
                messagebox.showinfo("Missing Details","invalid user")
                return
            if 1==1:
                s.cur.execute('insert into income(name,in_name,in_amt,in_date) values("{}","{}",{},"{}")'.format(s.username,b,int(s.e.get()),s.date))
                s.client.commit()
                s.scr.destroy()
                messagebox.showinfo('Info','Records have been INSERTED successfully')
    def eq(s):
            try:
                s.r=eval(s.e.get())
            except:
                s.r=0
            s.e.delete(0,END)
            s.e.insert(0,s.r)
    def mycal(s):
            def valueupdate():
                val=cal.selection_get()
                s.date=val
                s.d.config(text=val)
                top.destroy()
            top = Toplevel(s.scr)
            cal = Calendar(top,font="Arial 14", selectmode='day',cursor="hand1", year=2020, month=2, day=29)
            cal.pack(fill="both", expand=True)
            ttk.Button(top,text="OK",command=lambda :valueupdate()).pack()
    #############################################################CALCULATOR WINDOW FOR EXPENSE######################################
    def create(s,btn):
        print(btn)
        var1=StringVar()
        s.scr=Toplevel()  ## implemented toplevel instead of Tk()
        s.scr.title(btn)
        s.e=Entry(s.scr,font=('times',15,'bold'),width=30,bd=8,bg='grey')
        s.e.grid(row=0,columnspan=4)
        s.b=Button(s.scr,text='1',command=lambda :s.e.insert(END,'1'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b.grid(row=1,column=0)
        s.b1=Button(s.scr,text='2',command=lambda :s.e.insert(END,'2'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b1.grid(row=1,column=1)
        s.b2=Button(s.scr,text='3',command=lambda :s.e.insert(END,'3'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b2.grid(row=1,column=2)
        s.b3=Button(s.scr,text='4',command=lambda :s.e.insert(END,'4'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b3.grid(row=2,column=0)
        s.b4=Button(s.scr,text='5',command=lambda :s.e.insert(END,'5'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b4.grid(row=2,column=1)
        s.b5=Button(s.scr,text='6',command=lambda :s.e.insert(END,'6'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b5.grid(row=2,column=2)
        s.b11=Button(s.scr,text='+',command=lambda :s.e.insert(END,'+'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b11.grid(row=1,column=3)
        s.b6=Button(s.scr,text='7',command=lambda :s.e.insert(END,'7'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b6.grid(row=3,column=0)
        s.b7=Button(s.scr,text='8',command=lambda :s.e.insert(END,'8'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b7.grid(row=3,column=1)
        s.b8=Button(s.scr,text='9',command=lambda :s.e.insert(END,'9'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b8.grid(row=3,column=2)
        s.b9=Button(s.scr,text='-',command=lambda :s.e.insert(END,'-'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b9.grid(row=2,column=3)        
        s.b10=Button(s.scr,text='0',command=lambda :s.e.insert(END,'0'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b10.grid(row=4,column=1)
        s.b13=Button(s.scr,text='*',command=lambda :s.e.insert(END,'*'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b13.grid(row=4,column=0)
        s.b14=Button(s.scr,text='=',command=s.eq,font=('times',15,'bold'),bd=6,bg='grey',width=5)
        s.b14.grid(row=3,column=3)
        s.b15=Button(s.scr,text='clr',command=lambda :s.e.delete(0,END),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b15.grid(row=4,column=2)
        s.b17=Button(s.scr,bd=6,bg='cornsilk',text='Submit',font=('times',15,'bold'),command=lambda:s.submit(btn))
        s.b17.grid(row=4,column=3)
        s.d=Label(s.scr,height=2,width=32,font=('times',10,'bold'),bg='grey',fg='BLACK')
        s.d.grid(row=5,columnspan=3)
        s.b16=Button(s.scr,bd=6,bg='grey',text='Calendar',font=('times',12,'bold'),command=lambda:s.mycal())
        s.b16.grid(row=5,column=3)
        
        s.scr.mainloop()
    ##################################################CALCULATOR WINDOW FOR INCOME####################################################
    def create1(s,btn):
        print(btn)
        var1=StringVar()
        s.scr=Tk()
        s.scr.title(btn)
        s.e=Entry(s.scr,font=('times',15,'bold'),bd=8,width=30,bg='grey')
        s.e.grid(row=0,columnspan=4)
        s.b=Button(s.scr,text='1',command=lambda :s.e.insert(END,'1'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b.grid(row=1,column=0)
        s.b1=Button(s.scr,text='2',command=lambda :s.e.insert(END,'2'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b1.grid(row=1,column=1)
        s.b2=Button(s.scr,text='3',command=lambda :s.e.insert(END,'3'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b2.grid(row=1,column=2)
        s.b3=Button(s.scr,text='4',command=lambda :s.e.insert(END,'4'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b3.grid(row=2,column=0)
        s.b4=Button(s.scr,text='5',command=lambda :s.e.insert(END,'5'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b4.grid(row=2,column=1)
        s.b5=Button(s.scr,text='6',command=lambda :s.e.insert(END,'6'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b5.grid(row=2,column=2)
        s.b11=Button(s.scr,text='+',command=lambda :s.e.insert(END,'+'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b11.grid(row=1,column=3)
        s.b6=Button(s.scr,text='7',command=lambda :s.e.insert(END,'7'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b6.grid(row=3,column=0)
        s.b7=Button(s.scr,text='8',command=lambda :s.e.insert(END,'8'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b7.grid(row=3,column=1)
        s.b8=Button(s.scr,text='9',command=lambda :s.e.insert(END,'9'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b8.grid(row=3,column=2)
        s.b9=Button(s.scr,text='-',command=lambda :s.e.insert(END,'-'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b9.grid(row=2,column=3)
        s.b10=Button(s.scr,text='0',command=lambda :s.e.insert(END,'0'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b10.grid(row=4,column=1)
        s.b13=Button(s.scr,text='*',command=lambda :s.e.insert(END,'*'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b13.grid(row=4,column=0)
        s.b14=Button(s.scr,text='=',command=s.eq,font=('times',15,'bold'),bd=6,bg='grey',width=5)
        s.b14.grid(row=3,column=3)
        s.b15=Button(s.scr,text='clr',command=lambda :s.e.delete(0,END),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b15.grid(row=4,column=2)
        s.b17=Button(s.scr,bd=6,bg='cornsilk',text='Submit',font=('times',15,'bold'),command=lambda:s.submit1(btn))
        s.b17.grid(row=4,column=3)
        s.d=Label(s.scr,height=2,width=32,font=('times',10,'bold'),bg='grey',fg='BLACK')
        s.d.grid(row=5,columnspan=3)
        s.b16=Button(s.scr,bd=6,bg='grey',text='calendar',font=('times',12,'bold'),command=lambda:s.mycal())
        s.b16.grid(row=5,column=3)
        s.scr.mainloop()
    ###########################################################INCOME PAGE##################################################
    def income(s):
        
        
        try:
            s.scr.destroy()
        except:
            pass
        s.scr1=Tk()
        s.scr1.geometry("1900x900")
        s.scr1.state("zoomed")
        s.scr1.title("Income Categories")
        s.l=Label(s.scr1,text='ADD INCOME',pady=5,font=('aerial',30,'bold'),bg='powder blue',fg='black',justify=CENTER,relief=GROOVE)
        s.l.pack(fill=X,side=TOP)
        s.img=PhotoImage(file=r'i1.png')
        s.b=Button(s.scr1,text="Salary",image=s.img,compound=TOP,command=lambda:s.create1('Salary')).place(x=50,y=130)
        s.img1=PhotoImage(file=r'i2.png').subsample(3,3)
        s.b1=Button(s.scr1,text="Awards",image=s.img1,compound=TOP,command=lambda:s.create1('Awards')).place(x=350,y=130)
        s.img2=PhotoImage(file=r'i3.png').subsample(3,3)
        s.b2=Button(s.scr1,text="Grant",image=s.img2,compound=TOP,command=lambda:s.create1('Grant')).place(x=600,y=130)
        s.img3=PhotoImage(file=r'i4.png').subsample(3,3)
        s.b3=Button(s.scr1,text="Sale",image=s.img3,compound=TOP,command=lambda:s.create1('Sale')).place(x=850,y=130)
        s.img4=PhotoImage(file=r'refunds.png').subsample(3,3)
        s.b4=Button(s.scr1,text="Refunds",image=s.img4,compound=TOP,command=lambda:s.create1('Refunds')).place(x=1400,y=130)
        s.img5=PhotoImage(file=r'i6.png').subsample(7,7)
        s.b5=Button(s.scr1,text="Rentals",image=s.img5,compound=TOP,command=lambda:s.create1('Rentals')).place(x=1100,y=130)
        s.img6=PhotoImage(file=r'i7.png').subsample(3,3)
        s.b6=Button(s.scr1,text="Coupons",image=s.img6,compound=TOP,command=lambda:s.create1('Coupons')).place(x=50,y=330)
        s.img7=PhotoImage(file=r'i8.png').subsample(7,7)
        s.b7=Button(s.scr1,text="Lottery",image=s.img7,compound=TOP,command=lambda:s.create1('Lottery')).place(x=350,y=330)
        s.img8=PhotoImage(file=r'di.png').subsample(3,3)
        s.b8=Button(s.scr1,text="Divedends",image=s.img8,compound=TOP,command=lambda:s.create1('Divedends')).place(x=600,y=330)
        s.img9=PhotoImage(file=r'i10.png').subsample(9,9)
        s.b9=Button(s.scr1,text="Investments",image=s.img9,compound=TOP,command=lambda:s.create1('Investments')).place(x=850,y=330)
        s.img10=PhotoImage(file=r'22.png').subsample(3,3)
        s.b10=Button(s.scr1,text="Others",image=s.img10,compound=TOP,command=lambda:s.create1('Others')).place(x=1100,y=330)
        s.img12=PhotoImage(file=r'back.png').subsample(11,11)
        s.b12=Button(s.scr1,image=s.img12,compound=TOP,bg='powder blue',command=lambda:s.mainpage()).place(x=2,y=2)
        s.scr1.mainloop()
    ##############################################################EXPENSE PAGE###########################################################
    def expense(s):
        
        try:
            s.scr.destroy()
        except:
            pass
        s.scr2=Tk()
        s.scr2.geometry("1900x900")
        s.scr2.state("zoomed")
        s.scr2.title("Expense Categories")
        s.l=Label(s.scr2,text='ADD EXPENSE',pady=5,font=('aerial',30,'bold'),bg='powder blue',fg='black',justify=CENTER,relief=GROOVE)
        s.l.pack(fill=X,side=TOP)
        s.img=PhotoImage(file=r'FOOD.png').subsample(2,2)
        s.b=Button(s.scr2,text="Food",image=s.img,compound=TOP,relief=RAISED,command=lambda:s.create('Food')).place(x=50,y=100)
        s.img1=PhotoImage(file=r'2.png').subsample(4,4)
        s.b1=Button(s.scr2,text="Bill",image=s.img1,compound=TOP,command=lambda:s.create('Bill')).place(x=270,y=100)
        s.img2=PhotoImage(file=r'3.png').subsample(4,4)
        s.b2=Button(s.scr2,text="Transportation",image=s.img2,compound=TOP,command=lambda:s.create('Transportation')).place(x=520,y=100)
        s.img3=PhotoImage(file=r'4.png').subsample(4,4)
        s.b3=Button(s.scr2,text="Home",image=s.img3,compound=TOP,command=lambda:s.create('Home')).place(x=770,y=100)
        s.img4=PhotoImage(file=r'5.png').subsample(3,3)
        s.b4=Button(s.scr2,text="Car",image=s.img4,compound=TOP,command=lambda:s.create('Car')).place(x=1050,y=100)
        s.img5=PhotoImage(file=r'6.png').subsample(4,4)
        s.b5=Button(s.scr2,text="Entertainment",image=s.img5,compound=TOP,command=lambda:s.create('Entertainment')).place(x=1350,y=100)
        s.img6=PhotoImage(file=r'7.png').subsample(4,4)
        s.b6=Button(s.scr2,text="Clothing",image=s.img6,compound=TOP,command=lambda:s.create('Clothing')).place(x=50,y=280)
        s.img7=PhotoImage(file=r'8.png').subsample(4,4)
        s.b7=Button(s.scr2,text="Insurance",image=s.img7,compound=TOP,command=lambda:s.create('Insurance')).place(x=270,y=280)
        s.img8=PhotoImage(file=r'shopping.png').subsample(4,4)
        s.b8=Button(s.scr2,text="Shopping",image=s.img8,compound=TOP,command=lambda:s.create('Shopping')).place(x=520,y=280)
        s.img9=PhotoImage(file=r'tax.png').subsample(2,2)
        s.b9=Button(s.scr2,text="Tax",image=s.img9,compound=TOP,command=lambda:s.create('Tax')).place(x=770,y=280)
        s.img10=PhotoImage(file=r'11.png').subsample(15,15)
        s.b10=Button(s.scr2,text="Electronics",image=s.img10,compound=TOP,command=lambda:s.create('Electronics')).place(x=1050,y=280)
        s.img11=PhotoImage(file=r'12.png').subsample(4,4)
        s.b11=Button(s.scr2,text="Health",image=s.img11,compound=TOP,command=lambda:s.create('Health')).place(x=1350,y=280)
        s.img121=PhotoImage(file=r'13.png').subsample(4,4)
        s.b12=Button(s.scr2,text="Beauty",image=s.img121,compound=TOP,command=lambda:s.create('Beauty')).place(x=50,y=500)
        s.img13=PhotoImage(file=r'14.png').subsample(4,4)
        s.b13=Button(s.scr2,text="Education",image=s.img13,compound=TOP,command=lambda:s.create('Education')).place(x=270,y=500)
        s.img14=PhotoImage(file=r'18.png').subsample(4,4)
        s.b14=Button(s.scr2,text="Sports",image=s.img14,compound=TOP,command=lambda:s.create('Sports')).place(x=520,y=500)
        s.img15=PhotoImage(file=r'17.png').subsample(4,4)
        s.b15=Button(s.scr2,text="Social",image=s.img15,compound=TOP,command=lambda:s.create('Social')).place(x=770,y=500)
        s.img16=PhotoImage(file=r'19.png').subsample(3,3)
        s.b16=Button(s.scr2,text="Gift",image=s.img16,compound=TOP,command=lambda:s.create('Gift')).place(x=1050,y=500)
        s.img17=PhotoImage(file=r'20.png').subsample(4,4)
        s.b17=Button(s.scr2,text="Office",image=s.img17,compound=TOP,command=lambda:s.create('Office')).place(x=1350,y=500)
        s.img18=PhotoImage(file=r'22.png').subsample(4,4)
        s.b18=Button(s.scr2,text="Others",image=s.img18,compound=TOP,command=lambda:s.create('Others')).place(x=50,y=700)
        s.img12=PhotoImage(file=r'back.png').subsample(11,11)
        s.b12=Button(s.scr2,image=s.img12,compound=TOP,bg='powder blue',command=lambda:s.mainpage()).place(x=2,y=2)
        s.scr2.mainloop()
        
    def in_graph(s):
        s.ix=s.cur.execute("select in_name from income where name=%r and in_date like %r "%(s.username,s.year.get()+'-'+str(s.mnt[s.month.get()])+'%'))
        name=[i[0] for i in list(s.ix)]
        s.iy=s.cur.execute("select in_amt from income where name=%r and in_date like %r "%(s.username,s.year.get()+'-'+str(s.mnt[s.month.get()])+'%'))
        amnt=[i[0] for i in list(s.iy)]
        print(name,amnt)
        p=plt.subplot(2,1,1)
        plt.title("Data of "+s.month.get(),fontsize=25,loc='left')
        p.pie(amnt,autopct='%1.1f%%')
        plt.legend(name,loc="best")
        plt.axis("equal")
        p1=plt.subplot(2,1,2)
        p1.bar(name,amnt)
        mng=plt.get_current_fig_manager()
        mng.window.state('zoomed')
        plt.show()
    def ex_graph(s):
        
        s.ex=s.cur.execute("select ex_name from expense where name=%r and date like %r "%(s.username,s.year.get()+'-'+str(s.mnt[s.month.get()])+'%'))
        name=[i[0] for i in list(s.ex)]
        s.ey=s.cur.execute("select amount from expense where name=%r and date like %r "%(s.username,s.year.get()+'-'+str(s.mnt[s.month.get()])+'%'))
        amnt=[i[0] for i in list(s.ey)]
        print(name,amnt)
        p=plt.subplot(2,1,1)
        plt.title("Data of "+s.month.get(),fontsize=25,loc='left')
        p.pie(amnt,autopct='%1.1f%%')
        plt.legend(name,loc="best")
        plt.axis("equal")
        p1=plt.subplot(2,1,2)
        p1.bar(name,amnt)
        mng=plt.get_current_fig_manager()
        mng.window.state('zoomed')
        plt.show()
        
    def annex_graph(s):
        s.ai=s.cur.execute("select ex_name,amount from expense where name=%r and date like %r "%(s.username,s.year.get()+'%'))
        #r=s.cur.execute("select sum(amount) from expense where name=%r and date like %r "%(s.username,s.year.get()+'%'))
        n=s.ai.fetchall()
        #print(r)
        #q=r.fetchall()
        # print(q)
        print(n)
        d={}
        for i,j in n:
            if i in d.keys():
                d[i]=d[i]+j
            else:
                d[i]=j
        l1=[]
        l2=[]
        for i in d.keys():
            l1.append(i)
        for i in d.values():
            l2.append(i)
        r=sum(l2)
        
        p=plt.subplot(2,1,1)
        plt.title("Data of "+s.year.get(),fontsize=25,loc='left')
        p.pie(l2,autopct='%1.1f%%')
        plt.title("Annual expense:%r"%(r),fontsize=25,loc='right')
        
        plt.legend(l1,loc="best")
        plt.axis("equal")
        mng=plt.get_current_fig_manager()
        mng.window.state('zoomed')
        p1=plt.subplot(2,1,2)
        p1.bar(l1,l2)
        plt.show()
    def annin_graph(s):
        s.ai=s.cur.execute("select in_name,in_amt from income where name=%r and in_date like %r "%(s.username,s.year.get()+'%'))
        n=s.ai.fetchall()
        print(n[0][1])
        d={}
        for i,j in n:
            if i in d.keys():
                d[i]=d[i]+j
            else:
                d[i]=j
        l1=[]
        l2=[]
        for i in d.keys():
            l1.append(i)
        for i in d.values():
            l2.append(i)
        r=sum(l2)
        p=plt.subplot(2,1,1)
        plt.title("Data of "+s.year.get(),fontsize=25,loc='left')
        p.pie(l2,autopct='%1.1f%%')
        plt.legend(l1,loc="best")
        plt.axis("equal")
        plt.title("Annual Income:%r"%(r),fontsize=25,loc='right')
        mng=plt.get_current_fig_manager()
        mng.window.state('zoomed')
        p1=plt.subplot(2,1,2)
        p1.bar(l1,l2)
        plt.show()
    def entry3(s,btn_1, color,event):                          # <<<<<< HOVERING >>>>>>   
        s.btn_1.configure(background=color,foreground='white')
    def exit_3(s,btn_1, color, event):
        s.btn_1.configure(background=color,foreground='red')
    def entry4(s,btn_2, color,event):                          # <<<<<< HOVERING >>>>>>   
        s.btn_2.configure(background=color,foreground='white')
    def exit_4(s,btn_2, color, event):
        s.btn_2.configure(background=color,foreground='red')
    def entry5(s,btn_1, color,event):                          # <<<<<< HOVERING >>>>>>   
        s.btn_3.configure(background=color,foreground='white')
    def exit_5(s,btn_1, color, event):
        s.btn_3.configure(background=color,foreground='red')
    def entry6(s,btn_1, color,event):                          # <<<<<< HOVERING >>>>>>   
        s.btn_4.configure(background=color,foreground='white')
    def exit_6(s,btn_1, color, event):
        s.btn_4.configure(background=color,foreground='red')
    def stats(s):
        s.scr3=Tk()
        s.scr3.geometry("700x500")
        s.scr3.title("Expense Manager")
        s.scr3.configure(background="powder blue")
        s.l=Label(s.scr3,bd=0,text='Data representation',pady=5,font=('aerial',20,'bold'),bg='cornsilk',fg='black',justify=CENTER,relief=GROOVE)
        s.l.pack(fill=X,side=TOP)
        s.btn_1=Button(s.scr3,bd=4,fg='red',padx=16,pady=1,text='Monthly Income',font=('times',14,'bold'),bg='white',relief=RAISED,command=lambda:s.in_graph())
        s.btn_1.place(x=100,y=180)
        s.btn_1.bind('<Enter>',partial(s.entry3,s.btn_1,'red'))
        s.btn_1.bind('<Leave>',partial(s.exit_3,s.btn_1,'white'))
        s.btn_2=Button(s.scr3,bd=4,fg='red',padx=16,pady=1,text='Monthly Expense',font=('times',14,'bold'),bg='white',relief=RAISED,command=lambda:s.ex_graph())
        s.btn_2.place(x=100,y=350)
        s.btn_2.bind('<Enter>',partial(s.entry4,s.btn_2,'red'))
        s.btn_2.bind('<Leave>',partial(s.exit_4,s.btn_2,'white'))
        s.btn_3=Button(s.scr3,bd=4,fg='red',padx=16,pady=1,text='Annual Income',font=('times',14,'bold'),bg='white',relief=RAISED,command=lambda:s.annin_graph())
        s.btn_3.place(x=400,y=180)
        s.btn_3.bind('<Enter>',partial(s.entry5,s.btn_3,'red'))
        s.btn_3.bind('<Leave>',partial(s.exit_5,s.btn_3,'white'))
        s.btn_4=Button(s.scr3,bd=4,fg='red',padx=16,pady=1,text='Annual Expense',font=('times',14,'bold'),bg='white',relief=RAISED,command=lambda:s.annex_graph())
        s.btn_4.place(x=400,y=350)
        s.btn_4.bind('<Enter>',partial(s.entry6,s.btn_4,'red'))
        s.btn_4.bind('<Leave>',partial(s.exit_6,s.btn_4,'white'))
        s.scr3.mainloop()
    
    def refresh(s):
        s.mylist.delete(0,END)
        c=s.cur.execute("select sum(amount) from expense where name=%r and date like %r "%(s.username,s.year.get()+'-'+str(s.mnt[s.month.get()])+'%'))
        s.expensev.set(c.fetchone()[0])
        c=s.cur.execute("select sum(in_amt) from income where name=%r and in_date like %r "%(s.username,s.year.get()+'-'+str(s.mnt[s.month.get()])+'%'))
        s.incomev.set(c.fetchone()[0])
        try:
            s.balancev.set(s.incomev.get()-s.expensev.get())
        except:
            s.balancev.set(0)
        #s.scrollbar=Scrollbar(s.f4)
        #s.scrollbar.pack(side=RIGHT,fill=Y)
        #s.mylist=Listbox(s.f4,yscrollcommand=s.scrollbar.set)
        #try:
        r=s.cur.execute("select ex_name,amount from expense where name=%r and date like %r "%(s.username,s.year.get()+'-'+str(s.mnt[s.month.get()])+'%'))
        n=r.fetchall()
        print(n)
        for j,k in n:
             s.mylist.insert(END,'%r                                                                      %r'%(j,k))
             s.mylist.pack(side=LEFT,fill=BOTH)
             s.scrollbar.config(command=s.mylist.yview)
        #except:
         #   messagebox.showinfo('select a record first','select a record first') 
    def info(s):
        messagebox.showinfo('About','''Version:1.2.6
Version Code:9''')
    def delete(s,btn,t):
        s.cur.execute("delete from expense where name=%r and date like %r and ex_name=%r and amount=%r"%(s.username,s.year.get()+'-'+str(s.mnt[s.month.get()])+'%',btn,t))
        s.client.commit()
        messagebox.showinfo('Info','Records have been DELETED successfully')
    def changes(s,btn,t,b):
        s.cur.execute("update expense set amount=%r where name=%r and date like %r and ex_name=%r and amount=%r"%(b,s.username,s.year.get()+'-'+str(s.mnt[s.month.get()])+'%',btn,t)) 
        s.client.commit()
        s.scr5.destroy()
        messagebox.showinfo('Info','Records have been UPDATED successfully')
    def edit_create(s,btn,t):
        print(btn)
        var1=StringVar()
        s.scr5=Tk()
        s.scr5.title(btn)
        s.ea=Entry(s.scr5,font=('times',15,'bold'),bd=8,bg='grey')
        s.ea.grid(row=0,columnspan=4)
        s.b=Button(s.scr5,text='1',command=lambda :s.ea.insert(END,'1'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b.grid(row=1,column=0)
        s.b1=Button(s.scr5,text='2',command=lambda :s.ea.insert(END,'2'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b1.grid(row=1,column=1)
        s.b2=Button(s.scr5,text='3',command=lambda :s.ea.insert(END,'3'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b2.grid(row=1,column=2)
        s.b3=Button(s.scr5,text='4',command=lambda :s.ea.insert(END,'4'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b3.grid(row=2,column=0)
        s.b4=Button(s.scr5,text='5',command=lambda :s.ea.insert(END,'5'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b4.grid(row=2,column=1)
        s.b5=Button(s.scr5,text='6',command=lambda :s.ea.insert(END,'6'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b5.grid(row=2,column=2)
        s.b11=Button(s.scr5,text='+',command=lambda :s.ea.insert(END,'+'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b11.grid(row=1,column=3)

        s.b6=Button(s.scr5,text='7',command=lambda :s.ea.insert(END,'7'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b6.grid(row=3,column=0)
        s.b7=Button(s.scr5,text='8',command=lambda :s.ea.insert(END,'8'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b7.grid(row=3,column=1)
        s.b8=Button(s.scr5,text='9',command=lambda :s.ea.insert(END,'9'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b8.grid(row=3,column=2)
        s.b9=Button(s.scr5,text='-',command=lambda :s.ea.insert(END,'-'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b9.grid(row=2,column=3)
        
        s.b10=Button(s.scr5,text='0',command=lambda :s.ea.insert(END,'0'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b10.grid(row=4,column=1)
        s.b13=Button(s.scr5,text='*',command=lambda :s.ea.insert(END,'*'),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b13.grid(row=4,column=0)
        s.b14=Button(s.scr5,text='=',command=s.eq,font=('times',15,'bold'),bd=6,bg='grey',width=5)
        s.b14.grid(row=3,column=3)
        s.b15=Button(s.scr5,text='clr',command=lambda :s.ea.delete(0,END),bd=6,font=('times',15,'bold'),bg='grey',width=5)
        s.b15.grid(row=4,column=2)
        s.b17=Button(s.scr5,bd=6,bg='grey',text='Submit',font=('times',15,'bold'),command=lambda:s.changes(btn,t,s.ea.get()))
        s.b17.grid(row=4,column=3)
        
        s.scr5.mainloop()  
    
    def edit(s,t):
        print(type(t),t)
        try:
            s.scr.destroy()
            
        except:
            pass
        s.scr4=Tk()
        s.scr4.geometry("1400x900")
        s.scr4.state("zoomed")
        s.scr4.title("Edit")
        s.scr4.configure(background="powder blue")
        s.table=StringVar()
        s.s2=StringVar()
        s.s3=IntVar()
        s.l=Label(s.scr4,text='DETAILS',pady=5,font=('aerial',30,'bold'),bg='powder blue',fg='black',justify=CENTER,relief=GROOVE)
        s.l.pack(fill=X,side=TOP)
        s.imgadd5=PhotoImage(file=r'back.png').subsample(12,12)
        s.b25=Button(s.scr4,bd=4,image=s.imgadd5,compound=TOP,bg='cornsilk',command=lambda:s.mainpage()).place(x=2,y=2)
        s.f3=Frame(s.scr4,bd=5,bg='cornsilk',height=500,width=1000,relief=GROOVE)
        s.f3.place(x=300,y=160)
        s.table.set(t.split()[0].replace("'",""))
        s.l1=Label(s.f3,textvariable=s.table,pady=5,font=('aerial',35,'bold'),bg='cornsilk',fg='black',justify=CENTER)
        s.l1.place(x=400,y=5)
        detail=s.cur.execute("select * from expense where name=%r and date like %r and ex_name=%r and amount=%r "%(s.username,s.year.get()+'-'+str(s.mnt[s.month.get()])+'%',t.split()[0].replace("'",""),t.split()[1]))
        r=detail.fetchall()
        s.s3.set(r[0][2])
        s.s2.set(r[0][3])
        s.canvas2=Canvas(s.f3,height=2,width=980,bg='black')
        s.canvas2.place(x=0,y=70)
        s.l2=Label(s.f3,text='Category',pady=5,font=('aerial',25,'bold'),bg='cornsilk',fg='black',justify=CENTER)
        s.l2.place(x=50,y=150)
        s.l3=Label(s.f3,text='Expense',pady=5,font=('aerial',25),bg='cornsilk',fg='red',justify=CENTER)
        s.l3.place(x=500,y=150)
        s.l4=Label(s.f3,text='Amount',pady=5,font=('aerial',25,'bold'),bg='cornsilk',fg='black',justify=CENTER)
        s.l4.place(x=50,y=250)
        s.l5=Label(s.f3,textvariable=s.s3,pady=5,font=('aerial',25),bg='cornsilk',fg='red',justify=CENTER)
        s.l5.place(x=500,y=250)
        s.l6=Label(s.f3,text='Date',pady=5,font=('aerial',25,'bold'),bg='cornsilk',fg='black',justify=CENTER)
        s.l6.place(x=50,y=350)
        s.l7=Label(s.f3,textvariable=s.s2,pady=5,font=('aerial',25),bg='cornsilk',fg='red',justify=CENTER)
        s.l7.place(x=500,y=350)
        s.l8=Label(s.f3,text='(YYYY/MM/DD)',pady=5,font=('aerial',10),bg='cornsilk',fg='black',justify=CENTER)
        s.l8.place(x=700,y=365)
        s.l8=Label(s.f3,text=':',pady=5,font=('aerial',25,'bold'),bg='cornsilk',fg='black',justify=CENTER)
        s.l8.place(x=400,y=150)
        s.l8=Label(s.f3,text=':',pady=5,font=('aerial',25,'bold'),bg='cornsilk',fg='black',justify=CENTER)
        s.l8.place(x=400,y=250)
        s.l8=Label(s.f3,text=':',pady=5,font=('aerial',25,'bold'),bg='cornsilk',fg='black',justify=CENTER)
        s.l8.place(x=400,y=350)
        s.imgadd4=PhotoImage(file=r'delete.png').subsample(5,5)
        s.b24=Button(s.f3,bd=4,image=s.imgadd4,text='DELETE',compound=TOP,bg='cornsilk',command=lambda:s.delete(t.split()[0].replace("'",""),t.split()[1])).place(x=900,y=400)
        s.imgadd3=PhotoImage(file=r'edit.png').subsample(10,10)
        s.b23=Button(s.f3,bd=4,image=s.imgadd3,compound=TOP,bg='cornsilk',command=lambda:s.edit_create(t.split()[0].replace("'",""),t.split()[1])).place(x=700,y=250)
        
        
        s.scr4.mainloop()
        
    def call(s):
            msg=messagebox.askquestion('Logout?','Are you sure you want to logout?')
            if msg == 'yes':
                s.login()
                
    def entry(s,btn_in, color,event):                          # <<<<<< HOVERING >>>>>>   
        s.btn_in.configure(background=color,foreground='white')
    def exit_(s,btn_in, color, event):
        s.btn_in.configure(background=color,foreground='red')
    def entry1(s,btn_ex, color,event):                          # <<<<<< HOVERING >>>>>>   
        s.btn_ex.configure(background=color,foreground='white')
    def exit_1(s,btn_ex, color, event):
        s.btn_ex.configure(background=color,foreground='red')
    def entry2(s,btn_stat, color,event):                          # <<<<<< HOVERING >>>>>>   
        s.btn_stat.configure(background=color,foreground='white')
    def exit_2(s,btn_stat, color, event):
        s.btn_stat.configure(background=color,foreground='red')

        
      #############################################################################PREDICTION PAGE######################################################################  
    def predict(s):
        s.scr7=Tk()
        s.scr7.geometry("1900x900")
        s.scr7.state("zoomed")
        s.scr7.title("Expense Manager")
        s.l=Label(s.scr7,text='PREDICTION OF EXPENSES',pady=5,font=('aerial',30,'bold'),bg='Powder Blue',fg='black',justify=CENTER,relief=GROOVE)
        s.l.pack(fill=X,side=TOP)
        s.a=IntVar()
        s.b=IntVar()
        s.c=IntVar()
        s.d=IntVar()
        s.e=IntVar()
        s.f=IntVar()
        s.g=IntVar()
        s.h=IntVar()
        s.i=IntVar()
        s.j=IntVar()
        s.k=IntVar()
        s.l=IntVar()
        s.m=IntVar()
        s.n=IntVar()
        s.o=IntVar()
        s.p=IntVar()
        s.q=IntVar()
        s.r=IntVar()
        s.t=IntVar()
        s.u=IntVar()
        s.a.set(sum(test.result1)/len(test.result1))
        s.b.set(sum(test.result2)/len(test.result2))
        s.c.set(sum(test.result3)/len(test.result3))
        s.d.set(sum(test.result4)/len(test.result4))
        s.e.set(sum(test.result5)/len(test.result5))
        s.f.set(sum(test.result6)/len(test.result6))
        s.g.set(sum(test.result7)/len(test.result7))
        s.h.set(sum(test.result8)/len(test.result8))
        s.i.set(sum(test.result9)/len(test.result9))
        s.j.set(sum(test.result10)/len(test.result10))
        s.k.set(sum(test.result11)/len(test.result11))
        s.l.set(sum(test.result12)/len(test.result12))
        s.m.set(sum(test.result13)/len(test.result13))
        s.n.set(sum(test.result14)/len(test.result14))
        s.o.set(sum(test.result15)/len(test.result15))
        s.p.set(sum(test.result16)/len(test.result16))
        s.q.set(sum(test.result17)/len(test.result17))
        s.r.set(sum(test.result18)/len(test.result18))
        s.t.set(sum(test.result19)/len(test.result19))
        s.u.set(sum(test.result)/len(test.result))
        
        s.l1=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,text='food',font=('times',22,'bold'),bg='cornsilk')
        s.l1.place(x=80,y=100)
        s.la=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,font=('times',22,'bold'),bg='cornsilk')
        s.la.place(x=400,y=100)
        s.la.config(text=s.a.get())
        s.l2=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,text='office',font=('times',22,'bold'),bg='cornsilk')
        s.l2.place(x=80,y=150)
        s.lb=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,font=('times',22,'bold'),bg='cornsilk')
        s.lb.place(x=400,y=150)
        s.lb.config(text=s.b.get())
        s.l3=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,text='transportation',font=('times',22,'bold'),bg='cornsilk')
        s.l3.place(x=80,y=200)
        s.lc=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,font=('times',22,'bold'),bg='cornsilk')
        s.lc.place(x=400,y=200)
        s.lc.config(text=s.c.get())
        s.l4=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,text='entertainment',font=('times',22,'bold'),bg='cornsilk')
        s.l4.place(x=80,y=250)
        s.ld=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,font=('times',22,'bold'),bg='cornsilk')
        s.ld.place(x=400,y=250)
        s.ld.config(text=s.d.get())
        s.l5=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,text='shopping',font=('times',22,'bold'),bg='cornsilk')
        s.l5.place(x=80,y=300)
        s.le=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,font=('times',22,'bold'),bg='cornsilk')
        s.le.place(x=400,y=300)
        s.le.config(text=s.e.get())
        s.l6=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,text='tax',font=('times',22,'bold'),bg='cornsilk')
        s.l6.place(x=80,y=350)
        s.lf=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,font=('times',22,'bold'),bg='cornsilk')
        s.lf.place(x=400,y=350)
        s.lf.config(text=s.f.get())
        s.l7=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,text='electronics',font=('times',22,'bold'),bg='cornsilk')
        s.l7.place(x=80,y=400)
        s.lg=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,font=('times',22,'bold'),bg='cornsilk')
        s.lg.place(x=400,y=400)
        s.lg.config(text=s.g.get())
        s.l8=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,text='health',font=('times',22,'bold'),bg='cornsilk')
        s.l8.place(x=80,y=450)
        s.lh=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,font=('times',22,'bold'),bg='cornsilk')
        s.lh.place(x=400,y=450)
        s.lh.config(text=s.h.get())
        s.l9=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,text='beauty',font=('times',22,'bold'),bg='cornsilk')
        s.l9.place(x=80,y=500)
        s.li=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,font=('times',22,'bold'),bg='cornsilk')
        s.li.place(x=400,y=500)
        s.li.config(text=s.t.get())
        s.l11=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,text='education',font=('times',22,'bold'),bg='cornsilk')
        s.l11.place(x=80,y=550)
        s.lj=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,font=('times',22,'bold'),bg='cornsilk')
        s.lj.place(x=400,y=550)
        s.lj.config(text=s.i.get())
        s.l12=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,text='sports',font=('times',22,'bold'),bg='cornsilk')
        s.l12.place(x=950,y=100)
        s.lk=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,font=('times',22,'bold'),bg='cornsilk')
        s.lk.place(x=1270,y=100)
        s.lk.config(text=s.j.get())
        s.l13=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,text='social',font=('times',22,'bold'),bg='cornsilk')
        s.l13.place(x=950,y=150)
        s.ll=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,font=('times',22,'bold'),bg='cornsilk')
        s.ll.place(x=1270,y=150)
        s.ll.config(text=s.k.get())
        s.l14=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,text='gift',font=('times',22,'bold'),bg='cornsilk')
        s.l14.place(x=950,y=200)
        s.lm=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,font=('times',22,'bold'),bg='cornsilk')
        s.lm.place(x=1270,y=200)
        s.lm.config(text=s.l.get())
        s.l15=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,text='others',font=('times',22,'bold'),bg='cornsilk')
        s.l15.place(x=950,y=250)
        s.ln=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,font=('times',22,'bold'),bg='cornsilk')
        s.ln.place(x=1270,y=250)
        s.ln.config(text=s.m.get())
        s.l16=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,text='bill',font=('times',22,'bold'),bg='cornsilk')
        s.l16.place(x=950,y=300)
        s.lo=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,font=('times',22,'bold'),bg='cornsilk')
        s.lo.place(x=1270,y=300)
        s.lo.config(text=s.n.get())
        s.l17=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,text='home',font=('times',22,'bold'),bg='cornsilk')
        s.l17.place(x=950,y=350)
        s.lp=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,font=('times',22,'bold'),bg='cornsilk')
        s.lp.place(x=1270,y=350)
        s.lp.config(text=s.o.get())
        s.l18=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,text='clothing',font=('times',22,'bold'),bg='cornsilk')
        s.l18.place(x=950,y=400)
        s.lq=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,font=('times',22,'bold'),bg='cornsilk')
        s.lq.place(x=1270,y=400)
        s.lq.config(text=s.p.get())
        s.l19=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,text='insuarance',font=('times',22,'bold'),bg='cornsilk')
        s.l19.place(x=950,y=450)
        s.lr=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,font=('times',22,'bold'),bg='cornsilk')
        s.lr.place(x=1270,y=450)
        s.lr.config(text=s.q.get())
        s.l20=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,text='car',font=('times',22,'bold'),bg='cornsilk')
        s.l20.place(x=950,y=500)
        s.lt=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,font=('times',22,'bold'),bg='cornsilk')
        s.lt.place(x=1270,y=500)
        s.lt.config(text=s.r.get())
        s.l21=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,text='Total Expense',font=('times',22,'bold'),bg='cornsilk')
        s.l21.place(x=500,y=700)
        s.lu=Label(s.scr7,bd=4,fg='black',padx=16,pady=1,font=('times',22,'bold'),bg='cornsilk')
        s.lu.place(x=900,y=700)
        s.lu.config(text=s.u.get())
        s.scr7.mainloop()
        
     #######################################################################MAIN PAGE ##############################################################   
        
    def mainpage(s):
        try:
            s.scr.destroy()
            
        except:
            pass
        try:
            s.scr1.destroy()
            
        except:
            pass
        try:
            s.scr2.destroy()
            
        except:
            pass
        try:
            s.scr4.destroy()
            
        except:
            pass
        
        s.scr=Tk()
        s.scr.geometry("1900x900")
        s.scr.state("zoomed")
        s.scr.title("Expense Manager")
        s.month=StringVar()
        s.year=StringVar()
        s.incomev=IntVar()
        s.expensev=IntVar()
        s.balancev=IntVar()
        s.f3=Frame(s.scr,bd=5,bg='cornsilk',height=500,width=500,relief=GROOVE)
        s.f3.place(x=50,y=100)
        s.l=Label(s.scr,bd=7,text='WELCOME %r'%(s.username),pady=5,font=('comic sans',15,'bold'),bg='powder blue',fg='black',justify=LEFT)
        s.l.place(x=10,y=3)
        s.month.set("January")
        s.year.set("2020")
        s.m1=OptionMenu(s.f3,s.month,"January","February","March","April","May","June","July","August","September","October","November","December")
        s.m1.place(x=30,y=40)
        s.y1=OptionMenu(s.f3,s.year,"2015","2016","2017","2018","2019","2020","2021","2022","2023","2024","2025")
        s.y1.place(x=150,y=40)
        s.canvas2=Canvas(s.f3,height=2,width=480,bg='black')
        s.canvas2.place(x=0,y=120)
        s.canvas2.create_line(5,30,500,30)
        s.mnt={"January":'01',"February":'02',"March":'03',"April":'04',"May":'05',"June":'06',"July":'07',"August":'08',"September":'09',"October":'10',"November":'11',"December":'12'}
        c=s.cur.execute("select sum(amount) from expense where name=%r and date like %r "%(s.username,s.year.get()+'-'+str(s.mnt[s.month.get()])+'%'))
        s.expensev.set(c.fetchone()[0])
        s.h=Label(s.scr,bd=4,fg='black',padx=16,pady=1,text='Category                                                                          Amount',font=('times',22,'bold'),bg='cornsilk')
        s.h.place(x=650,y=100)
        s.f4=Frame(s.scr,bd=0,bg='cornsilk',height=500,width=820,relief=GROOVE)
        s.f4.place(x=650,y=139)
        c=s.cur.execute("select sum(in_amt) from income where name=%r and in_date like %r "%(s.username,s.year.get()+'-'+str(s.mnt[s.month.get()])+'%'))
        s.incomev.set(c.fetchone()[0])
        
        try:
            s.balancev.set(s.incomev.get()-s.expensev.get())
        except:
            s.balancev.set(0)
        s.canvas3=Canvas(s.f3,height=2,width=480,bg='black')
        s.canvas3.place(x=0,y=330)
        s.canvas3.create_line(5,30,500,30)
        s.q=s.cur.execute("select 0.8*sum(in_amt) from income where name=%r and in_date like %r "%(s.username,s.year.get()+'-'+str(s.mnt[s.month.get()])+'%'))
        n=s.q.fetchall()
        s.target=n[0][0]
        s.btn_in=Label(s.scr,bd=4,fg='black',padx=16,pady=1,text='Income',font=('times',22,'bold'),bg='cornsilk')
        s.btn_in.place(x=60,y=250)
        s.btn_ex=Label(s.scr,bd=4,text='Expense',fg='black',padx=16,pady=1,font=('times',20,'bold'),bg='cornsilk')
        s.btn_ex.place(x=60,y=350)
        s.btn_bal=Label(s.scr,bd=4,text='Balance',font=('times',20,'bold'),bg='cornsilk')
        s.btn_bal.place(x=70,y=450)
        s.l9=Label(s.scr,bd=4,textvariable=s.incomev,font=('times',20,'bold'),bg='cornsilk',fg='red')
        s.l9.place(x=400,y=250)
        s.l10=Label(s.scr,bd=4,textvariable=s.expensev,font=('times',20,'bold'),bg='cornsilk',fg='red')
        s.l10.place(x=400,y=350)
        s.l11=Label(s.scr,bd=4,textvariable=s.balancev,font=('times',20,'bold'),bg='cornsilk',fg='red')
        s.l11.place(x=400,y=450)
        s.imgadd=PhotoImage(file=r'refresh.png').subsample(10,10)
        s.b20=Button(s.f3,bd=4,image=s.imgadd,compound=TOP,command=lambda:s.refresh()).place(x=370,y=40)
        s.btn_in=Button(s.scr,bd=4,fg='red',padx=16,pady=1,text='Income +',font=('times',20,'bold'),bg='white',relief=RAISED,command=lambda:s.income())
        s.btn_in.place(x=120,y=700)
        s.btn_in.bind('<Enter>',partial(s.entry,s.btn_in,'red'))
        s.btn_in.bind('<Leave>',partial(s.exit_,s.btn_in,'white'))
        
        s.btn_ex=Button(s.scr,bd=4,fg='red',padx=16,pady=1,text='Expense +',font=('times',20,'bold'),bg='white',relief=RAISED,command=lambda:s.expense())
        s.btn_ex.place(x=700,y=700)
        s.btn_ex.bind('<Enter>',partial(s.entry1,s.btn_ex,'red'))
        s.btn_ex.bind('<Leave>',partial(s.exit_1,s.btn_ex,'white'))
        s.btn_stat=Button(s.scr,bd=4,fg='red',padx=16,pady=1,text='Statistics',font=('times',20,'bold'),bg='white',relief=RAISED,command=lambda:s.stats())
        s.btn_stat.place(x=1200,y=700)
        s.btn_stat.bind('<Enter>',partial(s.entry2,s.btn_stat,'red'))
        s.btn_stat.bind('<Leave>',partial(s.exit_2,s.btn_stat,'white'))
        s.imgadd1=PhotoImage(file=r'info.png').subsample(10,10)
        s.b21=Button(s.scr,bd=4,image=s.imgadd1,compound=TOP,command=lambda:s.info()).place(x=1350,y=10)
        s.imgadd2=PhotoImage(file=r'logout.png').subsample(10,12)
        s.b22=Button(s.scr,bd=4,image=s.imgadd2,compound=TOP,command=lambda:s.call()).place(x=1450,y=10)
        s.scrollbar=Scrollbar(s.f4,cursor="dot")
        s.scrollbar.pack(side=RIGHT,fill=Y)
        s.mylist=Listbox(s.f4,font=("times",22,'bold'),bg='cornsilk',fg='black',yscrollcommand=s.scrollbar.set,height=14,width=50,selectmode='SINGLE')
        r=s.cur.execute("select ex_name,amount from expense where name=%r and date like %r "%(s.username,s.year.get()+'-'+str(s.mnt[s.month.get()])+'%'))
        n=r.fetchall()
        for j,k in n:
            s.mylist.insert(END,'%r                                                                          %r'%(j,k))
        s.mylist.pack(side=LEFT,fill=BOTH)
        s.scrollbar.config(command=s.mylist.yview)
        s.imgadd3=PhotoImage(file=r'edit.png').subsample(12,12)
        s.b23=Button(s.scr,bd=4,image=s.imgadd3,compound=TOP,bg='cornsilk',command=lambda:s.edit(s.mylist.get(s.mylist.curselection()))).place(x=1240,y=100)
        s.btn_pre=Button(s.scr,bd=4,fg='red',padx=16,pady=1,text='Predict',font=('times',20,'bold'),bg='white',relief=RAISED,command=lambda:s.predict())
        s.btn_pre.place(x=1150,y=10)
        s.scr.mainloop()
        s.client.commit()
    #################################################################BACKUP FUNCTION#######################################################
    def backup(s):
        s.b=s.cur.execute("select ex_name,amount,date,in_name,in_amt,in_date from expense,income where expense.name=income.name")
        n=s.b.fetchall()
        r=',\n'.join([str(i) for i in n])
        f=open("backup.txt",'w+')
        f.write(r)
        f.close()            
x=abc()
x.login()






