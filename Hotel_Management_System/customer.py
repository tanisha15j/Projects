from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from tkinter import messagebox
import mysql.connector

class Customer:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1285x550+230+220")

        #variables
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        self.var_address=StringVar()










         

         # ====================title==================================================
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)


         # =====================logo============================================
        img2=Image.open("C:\\Users\\TANISHA\\OneDrive\\Desktop\\Hotel_Management_System\\Images\\logo.jpg")
        img2=img2.resize((100,40),Image.BICUBIC)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        #label frame
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",padx=2,font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=425,height=490)


        #labels and entries
        #Customer Reference
        lbl_cust_ref=Label(labelframeleft,text="Customer Reference",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,width=27,textvariable=self.var_ref,font=("times new roman",13,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)

        #Customer Name
        cname=Label(labelframeleft,font=("arial",12,"bold"),text="Customer Name:",padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,font=("arial",12,"bold"),width=27)
        txtcname.grid(row=1,column=1)

        #Mother Name
        lblmname=Label(labelframeleft,font=("arial",12,"bold"),text="Mother Name:",padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)
        txtmname=ttk.Entry(labelframeleft,textvariable=self.var_mother,font=("arial",12,"bold"),width=27)
        txtmname.grid(row=2,column=1)

        #Gender Combobox
        label_gender=Label(labelframeleft,font=("arial",12,"bold"),text="Gender:",padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=25,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        #Post Code
        lblPostCode=Label(labelframeleft,font=("arial",12,"bold"),text="PostCode:",padx=2,pady=6)
        lblPostCode.grid(row=4,column=0,sticky=W)
        txtPostCode=ttk.Entry(labelframeleft,textvariable=self.var_post,font=("arial",12,"bold"),width=27)
        txtPostCode.grid(row=4,column=1)

        #Mobile Number
        lblMobile=Label(labelframeleft,font=("arial",12,"bold"),text="Mobile:",padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)
        txtMobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,font=("arial",12,"bold"),width=27)
        txtMobile.grid(row=5,column=1)

        #Email
        lblEmail=Label(labelframeleft,font=("arial",12,"bold"),text="Email:",padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)
        txtEmail=ttk.Entry(labelframeleft,textvariable=self.var_email,font=("arial",12,"bold"),width=27)
        txtEmail.grid(row=6,column=1)

        #Nationality
        lblNationality=Label(labelframeleft,font=("arial",12,"bold"),text="Nationality:",padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)

        combo_Nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",12,"bold"),width=25,state="readonly")
        combo_Nationality["value"]=("Indian","American","Japanese")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7,column=1)

        #Id-proof type combobox
        lblIdProof=Label(labelframeleft,font=("arial",12,"bold"),text="Id Proof Type:",padx=2,pady=6)
        lblIdProof.grid(row=8,column=0,sticky=W)

        combo_Id=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("arial",12,"bold"),width=25,state="readonly")
        combo_Id["value"]=("AadharCard","DrivingLicense","Passport")
        combo_Id.current(0)
        combo_Id.grid(row=8,column=1)

        #Id Number
        lblIdNumber=Label(labelframeleft,font=("arial",12,"bold"),text="Id Number:",padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_id_number,font=("arial",13,"bold"),width=27)
        txtIdNumber.grid(row=9,column=1)

        #Address
        lblAddress=Label(labelframeleft,font=("arial",12,"bold"),text="Address:",padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)
        txtAddress=ttk.Entry(labelframeleft,textvariable=self.var_address,font=("arial",13,"bold"),width=27)
        txtAddress.grid(row=10,column=1)

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

        #Table Frame Search System
        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("times new roman",12,"bold"))
        Table_frame.place(x=435,y=50,width=860,height=490)

        lblSearchBy=Label(Table_frame,font=("arial",12,"bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)


 
        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_Search["value"]=("Mobile","Ref")
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
        details_table.place(x=0,y=50,width=840,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,columns=("ref","name","mother","gender","post","mobile",
                                                                    "email","nationality","idproof",
                                                                    "idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No.")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="Mother Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="PostCode")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id Proof")
        self.Cust_Details_Table.heading("idnumber",text="Id Number")
        self.Cust_Details_Table.heading("address",text="Address")

        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_management_system")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                               self.var_ref.get()  ,
                                                                                               self.var_cust_name.get(),
                                                                                               self.var_mother.get(),
                                                                                               self.var_gender.get(),
                                                                                               self.var_post.get(),
                                                                                               self.var_mobile.get(),
                                                                                               self.var_email.get(),
                                                                                               self.var_nationality.get(),
                                                                                               self.var_id_proof.get(),
                                                                                               self.var_id_number.get(),
                                                                                               self.var_address.get(),
                                                                                               ))
                conn.commit()
                self.fetch_data()
                conn.close()
                                                                                                                                                                           
                messagebox.showinfo("Success","Customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)
    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_management_system")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])


    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_management_system")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,IdProof=%s,IdNumber=%s,Address=%s where Ref=%s",(
                                                                                                                                                                                
                                                                                                                                                                                self.var_cust_name.get(),
                                                                                                                                                                                self.var_mother.get(),
                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                self.var_post.get(),
                                                                                                                                                                                self.var_mobile.get(),
                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                self.var_nationality.get(),
                                                                                                                                                                                self.var_id_proof.get(),
                                                                                                                                                                                self.var_id_number.get(),
                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                self.var_ref.get()
                                                                                                                                                                               ))
            
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated successfully",parent=self.root)


    def delete(self):
        delete=messagebox.askyesno("YesNo","Do you want to delete this customer",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_management_system")
            my_cursor=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
            
        conn.commit()
        self.fetch_data()
        conn.close()


    def reset(self):
        # self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        # self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        # self.var_nationality.set(""),
        # self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")

        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    
    def search(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="root",database="hotel_management_system")
         my_cursor=conn.cursor()
         
         
         my_cursor.execute("SELECT * FROM customer WHERE " + str(self.search_var.get()) + " LIKE '%" + str(self.txt_search.get()) + "%'")

         rows=my_cursor.fetchall()
         if len(rows)!=0:
             self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
             for i in rows:
                 self.Cust_Details_Table.insert("",END,values=i)

         conn.commit()
         conn.close()
                 





        



    
        


    





       


















        
        













if __name__ == "__main__":
    root=Tk()
    obj=Customer(root)
    root.mainloop()
