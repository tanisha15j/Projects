from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
from tkinter import messagebox
import mysql.connector


class RoomBooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1285x550+230+220")


        #variables
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()


         # ====================title==================================================
        lbl_title=Label(self.root,text="ROOM BOOKING",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)


        # =====================logo============================================
        img2=Image.open("C:\\Users\\TANISHA\\OneDrive\\Desktop\\Hotel_Management_System\\Images\\logo.jpg")
        img2=img2.resize((100,40),Image.BICUBIC)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)


        #label frame
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking",padx=2,font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #labels and entries
        #Customer Contact
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=20,font=("times new roman",13,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)

        #Fetch Data Button
        btnFetchData=Button(labelframeleft,command=self.fetch_contact,text="Fetch Data",font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnFetchData.place(x=347,y=4)

        #labels and entries
        #Check-in Date
        check_in_date=Label(labelframeleft,text="Check-in Date",font=("arial",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)

        txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=27,font=("times new roman",13,"bold"))
        txtcheck_in_date.grid(row=1,column=1)

        #Check-out Date
        lbl_check_out=Label(labelframeleft,text="Check-out Date",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_check_out.grid(row=2,column=0,sticky=W)

        txt_check_out=ttk.Entry(labelframeleft,textvariable=self.var_checkout,width=27,font=("times new roman",13,"bold"))
        txt_check_out.grid(row=2,column=1)

        #Room Type
        label_RoomType=Label(labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_management_system")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomType from details")
        room_types=my_cursor.fetchall()

        

        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=25,state="readonly")
        combo_RoomType["values"]=room_types
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)

        #Available Room
        lblRoomAvailable=Label(labelframeleft,text="Available Room",font=("arial",12,"bold"),padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)

        # txtRoomAvailable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,width=27,font=("times new roman",13,"bold"))
        # txtRoomAvailable.grid(row=4,column=1)

        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_management_system")
        my_cursor=conn.cursor()
        my_cursor.execute("select `RoomNo.` from details")
        rows=my_cursor.fetchall()

        combo_RoomNo=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=("arial",12,"bold"),width=25,state="readonly")
        combo_RoomNo["value"]=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4,column=1)

         #Meal
        lblMeal=Label(labelframeleft,text="Meal",font=("arial",12,"bold"),padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)

        txtMeal=ttk.Entry(labelframeleft,textvariable=self.var_meal,width=27,font=("times new roman",13,"bold"))
        txtMeal.grid(row=5,column=1)

        #No. Of Days
        lblNoOfDays=Label(labelframeleft,text="No. Of Days",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)

        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,width=27,font=("times new roman",13,"bold"))
        txtNoOfDays.grid(row=6,column=1)

        #Paid Tax
        lblPaidTax=Label(labelframeleft,text="Paid Tax",font=("arial",12,"bold"),padx=2,pady=6)
        lblPaidTax.grid(row=7,column=0,sticky=W)

        txtPaidTax=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,width=27,font=("times new roman",13,"bold"))
        txtPaidTax.grid(row=7,column=1)

        #Sub Total
        lblSubTotal=Label(labelframeleft,text="Sub Total",font=("arial",12,"bold"),padx=2,pady=6)
        lblSubTotal.grid(row=8,column=0,sticky=W)

        txtSubTotal=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,width=27,font=("times new roman",13,"bold"))
        txtSubTotal.grid(row=8,column=1)

        #Total Cost
        lblTotalCost=Label(labelframeleft,text="Total Cost",font=("arial",12,"bold"),padx=2,pady=6)
        lblTotalCost.grid(row=9,column=0,sticky=W)

        txtTotalCost=ttk.Entry(labelframeleft,textvariable=self.var_total,width=27,font=("times new roman",13,"bold"))
        txtTotalCost.grid(row=9,column=1)

        #Bill Button
        btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)


         #Buttons
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.delete,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        #Right Side Image
        img3=Image.open("C:\\Users\\TANISHA\\OneDrive\\Desktop\\Hotel_Management_System\\Images\\fillerphoto1.jpg")
        img3=img3.resize((520,300),Image.BICUBIC)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=760,y=55,width=520,height=300)



         #Table Frame Search System
        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("times new roman",12,"bold"))
        Table_frame.place(x=435,y=280,width=860,height=260)

        lblSearchBy=Label(Table_frame,font=("arial",12,"bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)


 
        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_Search["value"]=("Contact","Room")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)
  
        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_frame,textvariable=self.txt_search,font=("arial",13,"bold"),width=24)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_frame,text="Search",command=self.search,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_frame,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)

         #Show Data Table
        details_table=Frame(Table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=840,height=180)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,columns=("contact","checkin","checkout","roomtype","roomavailable","meal","noofdays",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="Contact No.")
        self.room_table.heading("checkin",text="Check-In Date")
        self.room_table.heading("checkout",text="Check-Out Date")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Room No.")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noofdays",text="No. Of Days")
        

        self.room_table["show"]="headings"

        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noofdays",width=100)

        self.room_table.pack(fill=BOTH,expand=1)

        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_management_system")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.var_contact.get(),
                                                                                                    self.var_checkin.get(),
                                                                                                    self.var_checkout.get(),
                                                                                                    self.var_roomtype.get(),
                                                                                                    self.var_roomavailable.get(),
                                                                                                    self.var_meal.get(),
                                                                                                    self.var_noofdays.get()
                                                                                                   
                                                                                               ))
                conn.commit()
                self.fetch_data()
                conn.close()
                                                                                                                                                                           
                messagebox.showinfo("Success","Room booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    
    
    #Fetch Data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_management_system")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])

    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_management_system")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set `Check-In`=%s,`Check-Out`=%s,`Room Type`=%s,`Room Available`=%s,Meal=%s,`No. Of Days`=%s where Contact=%s",(
                                                                                                                                                  
                                                                                                                                                    self.var_checkin.get(),
                                                                                                                                                    self.var_checkout.get(),
                                                                                                                                                    self.var_roomtype.get(),
                                                                                                                                                    self.var_roomavailable.get(),
                                                                                                                                                    self.var_meal.get(),
                                                                                                                                                    self.var_noofdays.get(),
                                                                                                                                                    self.var_contact.get()
                                                                                                                                                  ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated successfully",parent=self.root)

    def delete(self):
        delete=messagebox.askyesno("YesNo","Do you want to delete this room",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_management_system")
            my_cursor=conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
            
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")







    # All Data Fetch
    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter Contact Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_management_system")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This Number Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataFrame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataFrame.place(x=450,y=55,width=300,height=180)

                lblName=Label(showDataFrame,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)


               # Gender
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_management_system")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataFrame,text="Gender:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)

                lbl1=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl1.place(x=90,y=30)

                #Email
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_management_system")
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblEmail=Label(showDataFrame,text="Email:",font=("arial",12,"bold"))
                lblEmail.place(x=0,y=60)

                lbl2=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=60)

                #Nationality
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_management_system")
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblNationality=Label(showDataFrame,text="Nationality:",font=("arial",12,"bold"))
                lblNationality.place(x=0,y=90)

                lbl3=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=90)

                #Address
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_management_system")
                my_cursor=conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblAddress=Label(showDataFrame,text="Address:",font=("arial",12,"bold"))
                lblAddress.place(x=0,y=120)

                lbl4=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl4.place(x=90,y=120)


    #Search System
    def search(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_management_system")
         my_cursor=conn.cursor()
         
         
         my_cursor.execute("SELECT * FROM room WHERE " + str(self.search_var.get()) + " LIKE '%" + str(self.txt_search.get()) + "%'")

         rows=my_cursor.fetchall()
         if len(rows)!=0:
             self.room_table.delete(*self.room_table.get_children())
             for i in rows:
                 self.room_table.insert("",END,values=i)

         conn.commit()
         conn.close()
                 


    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()   
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)

        if (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Luxury"):
            q1=float(300)
            q2=float(3000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            Sub_T="Rs."+str("%.2f"%((q5)))
            Total_T="Rs."+str("%.2f"%((q5+(q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(Sub_T)
            self.var_total.set(Total_T)
        
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Luxury"):
            q1=float(500)
            q2=float(3000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            Sub_T="Rs."+str("%.2f"%((q5)))
            Total_T="Rs."+str("%.2f"%((q5+(q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(Sub_T)
            self.var_total.set(Total_T)

        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Luxury"):
            q1=float(700)
            q2=float(3000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            Sub_T="Rs."+str("%.2f"%((q5)))
            Total_T="Rs."+str("%.2f"%((q5+(q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(Sub_T)
            self.var_total.set(Total_T)

        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            Sub_T="Rs."+str("%.2f"%((q5)))
            Total_T="Rs."+str("%.2f"%((q5+(q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(Sub_T)
            self.var_total.set(Total_T)
        
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
            q1=float(500)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            Sub_T="Rs."+str("%.2f"%((q5)))
            Total_T="Rs."+str("%.2f"%((q5+(q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(Sub_T)
            self.var_total.set(Total_T)

        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Single"):
            q1=float(700)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            Sub_T="Rs."+str("%.2f"%((q5)))
            Total_T="Rs."+str("%.2f"%((q5+(q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(Sub_T)
            self.var_total.set(Total_T)

        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Double"):
            q1=float(300)
            q2=float(2000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            Sub_T="Rs."+str("%.2f"%((q5)))
            Total_T="Rs."+str("%.2f"%((q5+(q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(Sub_T)
            self.var_total.set(Total_T)

        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Double"):
            q1=float(500)
            q2=float(2000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            Sub_T="Rs."+str("%.2f"%((q5)))
            Total_T="Rs."+str("%.2f"%((q5+(q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(Sub_T)
            self.var_total.set(Total_T)

        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):
            q1=float(700)
            q2=float(2000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            Sub_T="Rs."+str("%.2f"%((q5)))
            Total_T="Rs."+str("%.2f"%((q5+(q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(Sub_T)
            self.var_total.set(Total_T)





       









if __name__ == "__main__":
    root=Tk()
    obj=RoomBooking(root)
    root.mainloop()
