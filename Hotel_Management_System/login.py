from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from hotel import HotelManagementSystem
from customer import Customer
from room import RoomBooking
from details import DetailsRoom






def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file="C:\\Users\\TANISHA\\OneDrive\\Desktop\\Hotel_Management_System\\Images\\bgphoto.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open("C:\\Users\\TANISHA\\OneDrive\\Desktop\\Hotel_Management_System\\Images\\logo.jpg")
        img1=img1.resize((100,100),Image.BICUBIC)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #label
        username_lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username_lbl.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password_lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password_lbl.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,show="*",font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #Icon Images
        img2=Image.open("C:\\Users\\TANISHA\\OneDrive\\Desktop\\Hotel_Management_System\\Images\\logo.jpg")
        img2=img2.resize((25,25),Image.BICUBIC)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=323,width=25,height=25)

        img3=Image.open("C:\\Users\\TANISHA\\OneDrive\\Desktop\\Hotel_Management_System\\Images\\logo.jpg")
        img3=img3.resize((25,25),Image.BICUBIC)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=395,width=25,height=25)
        
        #Login Button
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #Register Button
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)

        #Forgot Password Button
        forgetbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetbtn.place(x=10,y=370,width=160)


    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields required to fill")
        elif self.txtuser.get()=="tanisha" and self.txtpass.get()=="tan15":
            messagebox.showinfo("Success","Welcome to Hotel Management System")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="hotel_management_system")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                       self.txtuser.get(),
                                                                                       self.txtpass.get() 
                                                                                       ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    #reset password
    def reset_pass(self):
        if self.combo_security_q.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="hotel_management_system")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_q.get(),self.txt_security.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset.Please login with new password",parent=self.root2)
                self.root2.destroy()



    #forget password window
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="hotel_management_system")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Please enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_q.place(x=50,y=80)

                self.combo_security_q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_q["values"]=("Select","Your Birth Place","Your Pet Name","Your BestFriend Name")
                self.combo_security_q.place(x=50,y=110,width=250)
                self.combo_security_q.current(0)

                security_a=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_a.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)





        
           


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityq=StringVar()
        self.var_securitya=StringVar()
        self.var_password=StringVar()
        self.var_confirmpassword=StringVar()

        #Bg image
        self.bg=ImageTk.PhotoImage(file="C:\\Users\\TANISHA\\OneDrive\\Desktop\\Hotel_Management_System\\Images\\bgphoto.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #left image
        self.bg1=ImageTk.PhotoImage(file="C:\\Users\\TANISHA\\OneDrive\\Desktop\\Hotel_Management_System\\Images\\coverphoto.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)

        #main frame
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        #Labels and Entries

        #row 1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        #row2
        contact=Label(frame,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        #row3
        security_q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_q.place(x=50,y=240)

        self.combo_security_q=ttk.Combobox(frame,textvariable=self.var_securityq,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_q["values"]=("Select","Your Birth Place","Your Pet Name","Your BestFriend Name")
        self.combo_security_q.place(x=50,y=270,width=250)
        self.combo_security_q.current(0)

        security_a=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_a.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securitya,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        #row4
        password=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        password.place(x=50,y=310)

        self.txt_password=ttk.Entry(frame,textvariable=self.var_password,font=("times new roman",15))
        self.txt_password.place(x=50,y=340,width=250)

        confirm_password=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_password.place(x=370,y=310)

        self.txt_confirm_password=ttk.Entry(frame,textvariable=self.var_confirmpassword,font=("times new roman",15))
        self.txt_confirm_password.place(x=370,y=340,width=250)

        #Check Button
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree the Terms and Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=380)

        #buttons
        b1=Button(frame,command=self.register_data,text="Register",bd=3,relief=RIDGE,cursor="hand2",font=("times new roman",15,"bold"),fg="white",bg="blue",activebackground="blue")
        b1.place(x=10,y=470,width=200)

        b1=Button(frame,command=self.return_login,text="Login",bd=3,relief=RIDGE,cursor="hand2",font=("times new roman",15,"bold"),fg="white",bg="green",activebackground="green")
        b1.place(x=330,y=470,width=200)

    #function declaration
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityq.get()=="Select":
            messagebox.showerror("Error","All fields required")
        elif self.var_password.get()!=self.var_confirmpassword.get():
            messagebox.showerror("Error","Password and Confirm Password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and condition")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="hotel_management_system")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                       self.var_fname.get(),
                                                                                       self.var_lname.get(),
                                                                                       self.var_contact.get(),
                                                                                       self.var_email.get(),
                                                                                       self.var_securityq.get(),
                                                                                       self.var_securitya.get(),
                                                                                       self.var_password.get()
                                                                                         ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfull")

    def return_login(self):
        self.root.destroy()




class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        # =======================cover photo========================================
        img1=Image.open("C:\\Users\\TANISHA\\OneDrive\\Desktop\\Hotel_Management_System\\Images\\coverphoto.jpg")
        img1=img1.resize((1550,140),Image.BICUBIC)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)

        # =====================logo============================================
        img2=Image.open("C:\\Users\\TANISHA\\OneDrive\\Desktop\\Hotel_Management_System\\Images\\logo.jpg")
        img2=img2.resize((230,140),Image.BICUBIC)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)

        # ====================title==================================================
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        # =================main frame==================================================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        # ====================menu=================================================
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

        # ===================button frame============================================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        # ====================buttons==================================================
        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="ROOM",command=self.room_booking,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        room_btn.grid(row=1,column=0,pady=1)
        
        details_btn=Button(btn_frame,text="DETAILS",command=self.room_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        details_btn.grid(row=2,column=0,pady=1)
        
        report_btn=Button(btn_frame,text="REPORT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        logout_btn.grid(row=4,column=0,pady=1)

        # ========================right side image======================================
        img3=Image.open("C:\\Users\\TANISHA\\OneDrive\\Desktop\\Hotel_Management_System\\Images\\bgphoto.jpg")
        img3=img3.resize((1310,590),Image.BICUBIC)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1310,height=590)

        # ===========================down images=======================================
        img4=Image.open("C:\\Users\\TANISHA\\OneDrive\\Desktop\\Hotel_Management_System\\Images\\fillerphoto1.jpg")
        img4=img4.resize((230,210),Image.BICUBIC)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=225,width=230,height=210)

        img5=Image.open("C:\\Users\\TANISHA\\OneDrive\\Desktop\\Hotel_Management_System\\Images\\fillerphoto2.jpg")
        img5=img5.resize((230,190),Image.BICUBIC)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg1=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=420,width=230,height=190)


    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Customer(self.new_window)

    def room_booking(self):
        self.new_window=Toplevel(self.root)
        self.app=RoomBooking(self.new_window)

    def room_details(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)

    def logout(self):
        self.root.destroy()

    






        

if __name__ == "__main__":
    main()



