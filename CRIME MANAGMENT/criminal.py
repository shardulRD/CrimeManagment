from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox

class Criminal:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title("CRIMINAL MANAGMENT SYSTEM")
        
        #variables
        self.var_case_id=StringVar()
        self.var_criminal_no=StringVar()
        self.var_name=StringVar()  
        self.var_nickname=StringVar()  
        self.var_arrestDate=StringVar()
        self.var_crimeDate=StringVar()
        self.var_address=StringVar()
        self.var_age=StringVar()
        self.var_occupation=StringVar()
        self.var_birthmark=StringVar()
        self.var_Crimetype=StringVar()
        self.var_fathersname=StringVar()
        self.var_gedner=StringVar()
        self.var_mostwanted=StringVar()
        
        lbl_title=Label(self.root,text='CRIMINAL MANAGMENT SYSTEM SOFTWARE',font=('times new roman',40,'bold'),bg='black',fg='gold')
        lbl_title.place(x=0,y=0,width=1530,height=70)
       
       #cid logo
        img_logo=Image.open('images/logo.png')
        img_logo = img_logo.resize((60, 60), Image.LANCZOS)
        self.photo_image=ImageTk.PhotoImage(img_logo)
        
        self.logo=Label(self.root,image=self.photo_image)
        self.logo.place(x=80,y=5,width=60,height=60)
        
        #image frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=70,width=1530,height=130)
        
        #police 1
        img1=Image.open('images/police1.png')
        img1=img1.resize((540,160),Image.LANCZOS)
        self.photo1=ImageTk.PhotoImage(img1)
        
        self.img1=Label(img_frame,image=self.photo1)
        self.img1.place(x=0,y=0,width=540,height=160)
        
        # Police 2
        img2=Image.open('images/police2.png')
        img2=img2.resize((540,160),Image.LANCZOS)
        self.photo2=ImageTk.PhotoImage(img2)
        
        self.img2=Label(img_frame,image=self.photo2)
        self.img2.place(x=540,y=0,width=540,height=160)
        
        # Police 3
        img3=Image.open('images/police3.png')
        img3=img3.resize((540,160),Image.LANCZOS)
        self.photo3=ImageTk.PhotoImage(img3)
        
        self.img3=Label(img_frame,image=self.photo3)
        self.img3.place(x=1000,y=0,width=540,height=160)
       
        #Main Frame 
        Main_frame = Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=200,width=1500,height=560)
        
        #upper frame
        upper_frame = LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Criminal Information',font=('times new roman',11,'bold'),fg='red',bg='white')
        upper_frame.place(x=10,y=10,width=1480,height=270)
        
        # Labels Entry
        
        # CASE id
        caseid=Label(upper_frame,text='case ID:',font=('arial',11,'bold'),bg='white')
        caseid.grid(row=0,column=0,padx=2,sticky=W)
        
        caseentry = ttk.Entry(upper_frame,textvariable=self.var_case_id,width=22,font=('arial',11,'bold'))
        caseentry.grid(row=0,column=1,padx=2,sticky=W)
        
        #Criminal NO
        lbl_criminal_no=Label(upper_frame,font=('arial',12,'bold'),text="Crime No:",bg='white')
        lbl_criminal_no.grid(row=0,column=2,sticky=W,padx=2,pady=7)
        
        txt_criminal_no=ttk.Entry(upper_frame,textvariable=self.var_criminal_no,width=22,font=('arial',11,'bold'))
        txt_criminal_no.grid(row=0,column=3,padx=2,pady=7)

        # Criminal Name
        lbl_name=Label(upper_frame,text='Criminal Name:',font=('arial',12,'bold'),bg='white')
        lbl_name.grid(row=1,column=0,sticky=W,padx=2,pady=7)
        
        txt_Name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=('arial',11,'bold'))
        txt_Name.grid(row=1,column=1,sticky=W,padx=2,pady=7)
        
        # NickName
        lbl_nickname=Label(upper_frame,text='Nickname:',font=('arial',12,'bold'),bg='white')
        lbl_nickname.grid(row=1,column=2,sticky=W,padx=2,pady=7)
        
        txt_nickname=ttk.Entry(upper_frame,textvariable=self.var_nickname,width=22,font=('arial',11,'bold'))
        txt_nickname.grid(row=1,column=3,padx=2,pady=7)
        
        # Arrest date
        lbl_arrestDate=Label(upper_frame,text='Arrest Date:',font=('arial',12,'bold'),bg='white')
        lbl_arrestDate.grid(row=2,column=0,sticky=W,padx=2,pady=7)
        
        txt_arrestDate=ttk.Entry(upper_frame,textvariable= self.var_arrestDate,width=22,font=('arial',11,'bold'))
        txt_arrestDate.grid(row=2,column=1,padx=2,pady=7)
        
        #DATE of Crime 
        lbl_crimeDate=Label(upper_frame,text='Crime Date:',font=('arial',12,'bold'),bg='white')
        lbl_crimeDate.grid(row=2,column=2,sticky=W,padx=2,pady=7)
        
        txt_crimeDate=ttk.Entry(upper_frame,textvariable= self.var_crimeDate,width=22,font=('arial',11,'bold'))
        txt_crimeDate.grid(row=2,column=3,sticky=W,padx=2,pady=7)
        
        # address
        lbl_address=Label(upper_frame,text='Address:',font=('arial',12,'bold'),bg='white')
        lbl_address.grid(row=3,column=0,sticky=W,padx=2,pady=7)
        
        txt_address=ttk.Entry(upper_frame,textvariable= self.var_address,width=22,font=('arial',11,'bold'))
        txt_address.grid(row=3,column=1,sticky=W,padx=2,pady=7)
        
        #Age
        lbl_age=Label(upper_frame,text='Age :',font=('arial',12,'bold'),bg='white')
        lbl_age.grid(row=3,column=2,sticky=W,padx=2,pady=7)
      
        txt_age=ttk.Entry(upper_frame,textvariable=self.var_age,width=22,font=('arial',11,'bold'))
        txt_age.grid(row=3,column=3,sticky=W,padx=2,pady=7)
        
        #occupation
        lbl_occupation=Label(upper_frame,text='Occupation:',font=('arial',12,'bold'),bg='white')
        lbl_occupation.grid(row=4,column=0,sticky=W,padx=2,pady=7)
        
        txt_occupation=ttk.Entry(upper_frame,textvariable=self.var_occupation,width=22,font=('arial',11,'bold'))
        txt_occupation.grid(row=4,column=1,sticky=W,padx=2,pady=7)
        
        #birth mark
        lbl_birthmark=Label(upper_frame,text='Birth Mark:',font=('arial',12,'bold'),bg='white')
        lbl_birthmark.grid(row=4,column=2,sticky=W,padx=2,pady=7)
        
        txt_birthmark=ttk.Entry(upper_frame,textvariable= self.var_birthmark,width=22,font=('arial',11,'bold'))
        txt_birthmark.grid(row=4,column=3,sticky=W,padx=2,pady=7)
        
        #Crime type 
        lbl_lbl_Crimetype=Label(upper_frame,text='Crime Type:',font=('arial',12,'bold'),bg='white')
        lbl_lbl_Crimetype.grid(row=0,column=4,sticky=W,padx=2,pady=7)
    
        txt_lbl_Crimetype=ttk.Entry(upper_frame,textvariable=self.var_Crimetype, width=22,font=('arial',11,'bold'))
        txt_lbl_Crimetype.grid(row=0,column=5,sticky=W,padx=2,pady=7)
        
        #father Name
        lbl_fathersname=Label(upper_frame,text='Father Name:',font=('arial',12,'bold'),bg='white')
        lbl_fathersname.grid(row=1,column=4,sticky=W,padx=2,pady=7)
        
        txt_fathersname=ttk.Entry(upper_frame,textvariable=self.var_fathersname,width=22,font=('arial',11,'bold'))
        txt_fathersname.grid(row=1,column=5,sticky=W,padx=2,pady=7)
        
        # gender  
        lbl_gedner=Label(upper_frame,text='Gender:',font=('arial',12,'bold'),bg='white')
        lbl_gedner.grid(row=2,column=4,sticky=W,padx=2,pady=7)
        
        # most wanted
        lbl_mostwanted=Label(upper_frame,text='Most Wanted :',font=('arial',12,'bold'),bg='white')
        lbl_mostwanted.grid(row=3,column=4,sticky=W,padx=2,pady=7)
        
        #radio button for Gender 
        radio_frame_gender=Frame(upper_frame,bd=2,relief=RIDGE,bg="white")
        radio_frame_gender.place(x=730,y=90,width=190,height=30)
        
        lbl_gedner=Label(upper_frame,font=('arial',12,'bold'),bg='white',text='Gender')
        lbl_gedner.grid(row=2,column=4,sticky=W,padx=2,pady=7)
        
        male=Radiobutton(radio_frame_gender,variable=self.var_gedner,text='Male',value='male',font=('arial',9,'bold'),bg='white')
        male.grid(row=0,column=0,padx=5,pady=2,sticky=W)
        
        female=Radiobutton(radio_frame_gender,variable=self.var_gedner,text='Female',value='female',font=('arial',9,'bold'),bg='white')
        female.grid(row=0,column=1,padx=5,pady=2,sticky=W)
        
        #radio btn wanted
        lbl_mostwanted=Label(upper_frame,font=('arial',12,'bold'),bg='white',text='Most Wanted')
        lbl_mostwanted.grid(row=3,column=4,sticky=W,padx=2,pady=7)
        
        radio_frame_wanted=Frame(upper_frame,bd=2,relief=RIDGE,bg="white")
        radio_frame_wanted.place(x=730,y=130,width=190,height=30)
        
        yes=Radiobutton(radio_frame_wanted,variable=self.var_mostwanted,text='Yes',value='yes',font=('arial',9,'bold'),bg='white')
        yes.grid(row=0,column=0,padx=5,pady=2,sticky=W)
        
        no=Radiobutton(radio_frame_wanted,variable=self.var_mostwanted,text='No',value='no',font=('arial',9,'bold'),bg='white')
        no.grid(row=0,column=1,padx=5,pady=2,sticky=W)

        
        # BUTTONS
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=5,y=200,width=620,height=45)
        
        #add Button
        btn_add=Button(button_frame,command=self.add_data,text="Record Save",font=('arial',13,'bold'),width=14,fg='white',bg='blue')
        btn_add.grid(row=0,column=0,padx=3,pady=5)
        
        btn_update=Button(button_frame,command=self.update_data,text="Update",font=('arial',13,'bold'),width=14,fg='white',bg='blue')
        btn_update.grid(row=0,column=1,padx=3,pady=5)
        
        btn_delete=Button(button_frame,command=self.delete_data,text="Delete",font=('arial',13,'bold'),width=14,fg='white',bg='blue')
        btn_delete.grid(row=0,column=2,padx=3,pady=5)
        
        btn_clear=Button(button_frame,command=self.clear_data,text="Clear",font=('arial',13,'bold'),width=14,fg='white',bg='blue')
        btn_clear.grid(row=0,column=3,padx=3,pady=5)
        
        # background Side Image
        img_crime=Image.open('images/background.png')
        img_crime=img_crime.resize((470,245),Image.LANCZOS)
        self.photocrime=ImageTk.PhotoImage(img_crime)
        
        self.img_crime=Label(upper_frame,image=self.photocrime)
        self.img_crime.place(x=1000,y=0,width=470,height=245)
        
        
        # Down Frame 
        down_frame = LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Criminal Information Table',font=('times new roman',11,'bold'),fg='red',bg='white')
        down_frame.place(x=10,y=280,width=1480,height=270)
        
        #SEARCH FRAME
        search_frame = LabelFrame(down_frame,bd=2,relief=RIDGE,text='Search Criminal Record',font=('times new roman',11,'bold'),fg='red',bg='white')
        search_frame.place(x=0,y=0,width=1470,height=60)
        
        search_by=Label(search_frame,text='Search By:',font=('arial',11,'bold'),bg='red',fg='white')
        search_by.grid(row=0,column=0,sticky=W,padx=2)
        
        self.var_com_search=StringVar()
        combo_search_box=ttk.Combobox(search_frame,font=('arial',11,'bold'),textvariable=self.var_com_search,width=18,state='readonly')
        combo_search_box['value'] = ('Select Option',"Case_id",'Criminal_no')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,sticky=W,padx=2)
        
        self.var_search=StringVar()
        search_txt=ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=('arial',11,'bold'))
        search_txt.grid(row=0,column=2,sticky=W,padx=5)
        
        btn_search=Button(search_frame,command=self.search_data,text="Search",font=('arial',13,'bold'),width=14,fg='white',bg='blue')
        btn_search.grid(row=0,column=3,padx=3,pady=5)
        
        btn_all=Button(search_frame,command=self.fetch_data,text="Show All",font=('arial',13,'bold'),width=14,fg='white',bg='blue')
        btn_all.grid(row=0,column=4,padx=3,pady=5)
        
        lbl_crimeagency=Label(search_frame,text='NATIONAL CRIME AGENCY',font=('arial',30,'bold'),bg='white',fg='crimson')
        lbl_crimeagency.grid(row=0,column=5,sticky=W,padx=50,pady=0)
        
        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)
        
        #Scrollbar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.criminal_table=ttk.Treeview(table_frame,columns=("1","2","3","4","5","6","7","8","9","10","11","12","13","14"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)
        
        self.criminal_table.heading('1',text='Case_id')
        self.criminal_table.heading('2',text='Crime No')
        self.criminal_table.heading('3',text='Criminal Name')
        self.criminal_table.heading('4',text='Nickname')
        self.criminal_table.heading('5',text='Arrest Date')
        self.criminal_table.heading('6',text='Crime Date')
        self.criminal_table.heading('7',text='Address')
        self.criminal_table.heading('8',text='Age ')
        self.criminal_table.heading('9',text='Occupation')
        self.criminal_table.heading('10',text='Birth Mark')
        self.criminal_table.heading('11',text='Crime Type')
        self.criminal_table.heading('12',text='Father Name')
        self.criminal_table.heading('13',text='Gender')
        self.criminal_table.heading('14',text='Most Wanted')
        
        self.criminal_table['show']='headings'
        
        self.criminal_table.column('1',width=100)
        self.criminal_table.column('2',width=100)
        self.criminal_table.column('3',width=100)
        self.criminal_table.column('4',width=100)
        self.criminal_table.column('5',width=100)
        self.criminal_table.column('6',width=100)
        self.criminal_table.column('7',width=100)
        self.criminal_table.column('8',width=100)
        self.criminal_table.column('9',width=100)
        self.criminal_table.column('10',width=100)
        self.criminal_table.column('11',width=100)
        self.criminal_table.column('12',width=100)
        self.criminal_table.column('13',width=100)
        self.criminal_table.column('14',width=100)
        
        
        self.criminal_table.pack(fill=BOTH,expand=1)
        
        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)
        
        self.fetch_data()
    
    #ADD FUNTION
    
    def add_data(self):
        
        if self.var_case_id.get() == "":
            messagebox.showerror('Error', 'Please enter case id')
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="123456789", database="crimemanagment")
                my_cursor = conn.cursor()
            
             # Define the SQL query with placeholders for each column
                sql_query = 'INSERT INTO criminal1 (case_id, criminal_no, name, nickname, arrestDate, crimeDate, address, age, occupation, birthmark, Crimetype, fathersname, gender, mostwanted) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            
            # Provide values for each placeholder
                values=(self.var_case_id.get(),
                        self.var_criminal_no.get(),
                        self.var_name.get(),
                        self.var_nickname.get(),
                        self.var_arrestDate.get(),
                        self.var_crimeDate.get(),
                        self.var_address.get(),
                        self.var_age.get(),
                        self.var_occupation.get(),
                        self.var_birthmark.get(),
                        self.var_Crimetype.get(),
                        self.var_fathersname.get(),
                        self.var_gedner.get(),
                        self.var_mostwanted.get())
            
                # Execute the query with the provided values
                my_cursor.execute(sql_query, values)
            
                # Commit the transaction and close the connection
                conn.commit()
                conn.close()
            
                # Show success message
                messagebox.showinfo('Success', 'Criminal record has been added')
            
                # Refresh the displayed data
                self.fetch_data()
                self.clear_data()
            
            except Exception as es:
                messagebox.showerror('Error', f'Due To {str(es)}')

          
               
           

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="crimemanagment")    
        my_cursor=conn.cursor()
        my_cursor.execute("select * from criminal1")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert('',END,values=i)
            conn.commit()
        conn.close()                   
        
    
    # get cursor
    
    def get_cursor(self,event=""):
        cursor_row=self.criminal_table.focus()
        content=self.criminal_table.item(cursor_row)
        data=content['values']
        
        self.var_case_id.set(data[0])
        self.var_criminal_no.set(data[1])
        self.var_name.set(data[2])
        self.var_nickname.set(data[3])
        self.var_arrestDate.set(data[4])
        self.var_crimeDate.set(data[5])
        self.var_address.set(data[6])
        self.var_age.set(data[7])
        self.var_occupation.set(data[8])
        self.var_birthmark.set(data[9])    
        self.var_Crimetype.set(data[10])
        self.var_fathersname.set(data[11])  
        self.var_gedner.set(data[12])
        self.var_mostwanted.set(data[13])                 
        
        
    #update    
    def update_data(self):
        if self.var_case_id.get() == "":
            messagebox.showerror('Error', 'Please enter case id')
        else:
            try:
                update=messagebox.askyesno('Update','Are you sure to update this criminal record')
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="crimemanagment")    
                    my_cursor=conn.cursor()
                    my_cursor.execute('UPDATE criminal1 SET criminal_no=%s,name=%s,nickname=%s,arrestdate=%s,crimeDate=%s,address=%s,age=%s,occupation=%s,birthmark=%s,Crimetype=%s,fathersname=%s,gender=%s,mostwanted=%s where case_id=%s',(
                                                                                                                                                                                                                                             self.var_criminal_no.get(), 
                                                                                                                                                                                                                                             self.var_name.get(),
                                                                                                                                                                                                                                             self.var_nickname.get(),
                                                                                                                                                                                                                                             self.var_arrestDate.get(),
                                                                                                                                                                                                                                             self.var_crimeDate.get(),
                                                                                                                                                                                                                                             self.var_address.get(),
                                                                                                                                                                                                                                             self.var_age.get(),
                                                                                                                                                                                                                                             self.var_occupation.get(),
                                                                                                                                                                                                                                             self.var_birthmark.get(),
                                                                                                                                                                                                                                             self.var_Crimetype.get(),
                                                                                                                                                                                                                                             self.var_fathersname.get(),
                                                                                                                                                                                                                                             self.var_gedner.get(),
                                                                                                                                                                                                                                             self.var_mostwanted.get(),
                                                                                                                                                                                                                                             self.var_case_id.get(),  
                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                             ))    
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal Record has been updated')
            except Exception as es:
                messagebox.showerror('Error', f'Due To {str(es)}')        
    
    
    # DELete
    def delete_data(self):
        if self.var_case_id.get() == "":
            messagebox.showerror('Error', 'Please enter case id')
        else:
            try:
                delete=messagebox.askyesno('Delete','Are you sure to Delete this criminal record')
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="crimemanagment")    
                    my_cursor=conn.cursor()
                    sql='DELETE FROM criminal1 WHERE case_id=%s'
                    value=(self.var_case_id.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not delete:
                        return    
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal Record has been Deleted')
            except Exception as es:
                messagebox.showerror('Error', f'Due To {str(es)}')        
    
    
    
    # CLEAR
    def clear_data(self):
        self.var_case_id.set("")
        self.var_criminal_no.set("")
        self.var_name.set("")
        self.var_nickname.set("")
        self.var_arrestDate.set("")
        self.var_crimeDate.set("")
        self.var_address.set("")
        self.var_age.set("")
        self.var_occupation.set("")
        self.var_birthmark.set("")    
        self.var_Crimetype.set("")
        self.var_fathersname.set("")  
        self.var_gedner.set("")
        self.var_mostwanted.set("") 
        
    #SEARCH
    def search_data(self):
        if self.var_com_search.get()=="":
             messagebox.showerror('Error', 'Please enter case id')
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="123456789",database="crimemanagment")    
                my_cursor=conn.cursor()
                my_cursor.execute('SELECT * FROM criminal1 WHERE ' +str(self.var_com_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert('',END,values=i)
                conn.commit()
                conn.close()                   
            except Exception as es:
                 messagebox.showerror('Error', f'Due To {str(es)}')
                    
            
        
        
        
        
        
        
        
        
    
       
            
                    



if __name__=="__main__":
    root=Tk()
    obj = Criminal(root)
    root.mainloop()    
    
    
    