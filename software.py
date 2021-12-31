from tkinter import *
from tkinter import ttk,messagebox
import time
import os

class File_App:
    def __init__(self):
        self.root=Tk()
        self.root.title('File Based Record System')
        self.root.geometry('1350x700+0+0')
        self.root.config(bg='black')

        title=Label(self.root,text='File Based record System',
                    font=('times new roman',35,'bold'),bd=10,bg='black',
                    fg='pink',pady=10,relief=GROOVE).pack(fill=X)
        student_Frame=Frame(self.root,bd=10,bg='black',relief=GROOVE)
        student_Frame.place(x=20,y=100,height=450)

        stitle=Label(student_Frame,text='Students Details',font=('times new roman',30,'bold'),
                     fg='pink',bg='black').grid(row=0,columnspan=4,pady=20)

        # All Variables
        self.s_id=StringVar()
        self.name=StringVar()
        self.course=StringVar()
        self.address=StringVar()
        self.city=StringVar()
        self.contact=StringVar()
        self.date=StringVar()
        self.degree=StringVar()
        self.proof=StringVar()
        self.payment=StringVar()



        label_std_id=Label(student_Frame,text='Students ID:',font=('times new roman',20,'bold'),
                           fg='white',bg='black').grid(row=1,column=0,pady=10,padx=20,sticky='w')
        text_std_id=Entry(student_Frame,textvariable=self.s_id,bd=7,relief=GROOVE,
                          width=22,font='arial 15 bold').grid(row=1,column=1,padx=10,pady=10)

        label_std_contact=Label(student_Frame,text='Contact No:',font=('times new roman',20,'bold'),
                                fg='white',bg='black').grid(row=1,column=2,pady=10,padx=20)
        text_std_contact=Entry(student_Frame,textvariable=self.contact,bd=7,relief=GROOVE,
                               width=22,font='arial 15 bold').grid(row=1,column=3,padx=10,pady=10)

        label_std_name=Label(student_Frame,text='Name:',font=('times new roman',20,'bold'),
                             fg='white',bg='black').grid(row=2,column=0,pady=10,padx=20)
        text_std_name=Entry(student_Frame,textvariable=self.name,bd=7,relief=GROOVE,
                            width=22,font='arial 15 bold').grid(row=2,column=1,padx=10,pady=10)

        label_std_date=Label(student_Frame,text='Date(dd/mm/yyyy)',font=('times new roman',20,'bold'),
                             fg='white',bg='black').grid(row=2,column=2,pady=10,padx=20)
        text_std_date=Entry(student_Frame,textvariable=self.date,bd=7,relief=GROOVE,
                            width=22,font='arial 15 bold').grid(row=2,column=3,padx=10,pady=10)

        label_std_course=Label(student_Frame,text='Course:',font=('times new roman',20,'bold'),
                               fg='white',bg='black').grid(row=3,column=0,pady=10,padx=20)
        text_std_course=Entry(student_Frame,textvariable=self.course,bd=7,relief=GROOVE,
                              width=22,font='arial 15 bold').grid(row=3,column=1,padx=10,pady=10)

        label_std_degree=Label(student_Frame,text='Select Degree:',font=('times new roman',20,'bold'),
                               fg='white',bg='black').grid(row=3,column=2,pady=10,padx=20)
        degree_combo=ttk.Combobox(student_Frame,textvariable=self.degree,
                                  width=20,state='readonly',font='arial 15 bold')
        degree_combo['values']=("BCA","MCA","BTech","MBA","MTech")
        degree_combo.grid(row=3,column=3,padx=10,pady=10)

        label_std_address=Label(student_Frame,text='Address:',font=('times new roman',20,'bold'),
                                fg='white',bg='black').grid(row=4,column=0,pady=10,padx=20)
        text_std_address=Entry(student_Frame,textvariable=self.address,bd=7,relief=GROOVE,
                               width=22,font='arial 15 bold').grid(row=4,column=1,padx=10,pady=10)

        label_std_id_proof=Label(student_Frame,text='ID Proof:',font=('times new roman',20,'bold'),
                                 fg='white',bg='black').grid(row=4,column=2,pady=10,padx=20)
        id_proff_combo=ttk.Combobox(student_Frame,textvariable=self.proof,
                                    width=20,state='readonly',font='arial 15 bold')
        id_proff_combo['values']=("PAN Card","Driving License","Students ID Card")
        id_proff_combo.grid(row=4,column=3,padx=10,pady=10)

        label_std_city=Label(student_Frame,text='City:',font=('times new roman',20,'bold'),
                             fg='white',bg='black').grid(row=5,column=0,pady=10,padx=20)
        text_std_city=Entry(student_Frame,textvariable=self.city,bd=7,relief=GROOVE,width=22,
                            font='arial 15 bold').grid(row=5,column=1,padx=10,pady=10)

        label_std_payment_method=Label(student_Frame,text='Payment Method:',font=('times new roman',20,'bold'),
                                       fg='white',bg='black').grid(row=5,column=2,pady=10,padx=20)
        pament_methode_combo=ttk.Combobox(student_Frame,textvariable=self.payment,
                                          width=20,state='readonly',font='arial 15 bold')
        pament_methode_combo['values']=("Cash","MEFT","Iternet Banking","Credit Card")
        pament_methode_combo.grid(row=5,column=3,padx=10,pady=10)

        btnFrame=Frame(self.root,bd=10,relief=GROOVE)
        btnFrame.place(x=10,y=570)
        btnFrame.config(bg='black')

        btnSave=Button(btnFrame,text='Save',font=('arial',15,'bold'),bd=7,width=18,bg='black',
                       fg='pink',command=self.save_data).grid(row=0,column=0,padx=12,pady=10)
        btnDelete=Button(btnFrame,text='Delete',font=('arial',15,'bold'),bd=7,width=18,bg='black',
                         fg='pink',command=self.delete).grid(row=0,column=1,padx=12,pady=10)
        btnClear=Button(btnFrame,text='Clear',font=('arial',15,'bold'),bd=7,width=18,bg='black',
                        fg='pink',command=self.clear).grid(row=0,column=2,padx=12,pady=10)
        btnLogout=Button(btnFrame,text='Logout',font=('arial',15,'bold'),bd=7,width=18,bg='black',
                         fg='pink',command=self.logout).grid(row=0,column=3,padx=12,pady=10)
        btnExit=Button(btnFrame,text='Exit',font=('arial',15,'bold'),bd=7,width=18,bg='black',
                       fg='pink',command=self.exit).grid(row=0,column=4,padx=12,pady=10)


        file_Frame=Frame(self.root,bd=10,relief=GROOVE,bg='black')
        file_Frame.place(x=1040,y=100,width=300,height=450)
        ftitle=Label(file_Frame,text='All Files',font=('arial',20,'bold'),
                     bd=5,bg='black',fg='white',relief=GROOVE).pack(side=TOP,fill=X)

        scroll_y=Scrollbar(file_Frame,orient=VERTICAL)
        self.file_List=Listbox(file_Frame,yscrollcommand=scroll_y.set)
        self.file_List.config(font=('arial',15,'bold'))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.file_List.yview)
        self.file_List.pack(fill=BOTH,expand=1)
        self.file_List.bind('<ButtonRelease-1>',self.get_data)
        self.show_files()
        self.root.mainloop()

    def save_data(self):
        present='no'
        if self.s_id.get()=='':
            messagebox.showerror('Error','Students ID must be required!!')
        else:
            f=os.listdir('files/')
            if self.s_id.get()=='':
                messagebox.showerror('Error','student ID must be required')
            else:
                f=os.listdir('files/')
                if len(f)>0:
                    for i in f:
                        if i.split('.')[0]==self.s_id.get():
                            present='yes'
                    if present=='yes':
                        ask=messagebox.askyesno('Update','File already present \nDo you really want to update??')
                        if ask>0:
                            self.save_file()
                            messagebox.showinfo('Update','Record has updated successfully!!')
                            self.show_files()
                    else:
                        self.save_file()
                        messagebox.showinfo('Saved', 'Record has saved successfully!!')
                        self.show_files()
                else:
                    self.save_file()
                    messagebox.showinfo('Saved', 'Record has saved successfully!!')
                    self.show_files()

    def save_file(self):
        f = open('files/' + str(self.s_id.get()) + ".txt", "w")
        f.write(
            str(self.s_id.get()) + ',' +
            str(self.name.get()) + ',' +
            str(self.course.get()) + ',' +
            str(self.address.get()) + ',' +
            str(self.city.get()) + ',' +
            str(self.contact.get()) + ',' +
            str(self.date.get()) + ',' +
            str(self.degree.get()) + ',' +
            str(self.proof.get()) + ',' +
            str(self.payment.get())
        )
        f.close()


    def show_files(self):
        files=os.listdir('files/')
        self.file_List.delete(0, END)
        if len(files)>0:
            for i in files:
                self.file_List.insert(END,i)
                self.s_id.set('')
                self.name.set('')
                self.course.set('')
                self.address.set('')
                self.city.set('')
                self.contact.set('')
                self.date.set('')
                self.degree.set('')
                self.proof.set('')
                self.payment.set('')

    def get_data(self,event):
        get_cursor=self.file_List.curselection()
        # print(self.file_List.get(get_cursor))
        f1=open('files/'+self.file_List.get(get_cursor))
        value=[]
        for f in f1:
            value=f.split(',')

        self.s_id.set(value[0])
        self.name.set(value[1])
        self.course.set(value[2])
        self.address.set(value[3])
        self.city.set(value[4])
        self.contact.set(value[5])
        self.date.set(value[6])
        self.degree.set(value[7])
        self.proof.set(value[8])
        self.payment.set(value[9])

    def clear(self):
        self.s_id.set('')
        self.name.set('')
        self.course.set('')
        self.address.set('')
        self.city.set('')
        self.contact.set('')
        self.date.set('')
        self.degree.set('')
        self.proof.set('')
        self.payment.set('')

    def delete(self):
        present='no'
        if self.s_id.get()=='':
            messagebox.showerror('Error','Students ID must be required!!')
        else:
            f=os.listdir('files/')
            if len(f)>0:
                for i in f:
                    if i.split('.')[0]==self.s_id.get():
                        present='yes'
                if present=='yes':
                    ask=messagebox.askyesno('Delete','Do you really want to delete??')
                    if ask>0:
                        os.remove('files/'+self.s_id.get()+'.txt')
                        messagebox.showinfo('Success','deleted Successfully!!')
                        self.show_files()
                        self.s_id.set('')
                        self.name.set('')
                        self.course.set('')
                        self.address.set('')
                        self.city.set('')
                        self.contact.set('')
                        self.date.set('')
                        self.degree.set('')
                        self.proof.set('')
                        self.payment.set('')
                else:
                    messagebox.showerror('Error','File not found!!')

    def exit(self):
        ask=messagebox.askyesno('Exit','Do you really want to exit??')
        if ask>0:
            self.root.destroy()

    def logout(self):
        self.root.destroy()
        import login


# root=Tk()
# ob=File_App(root)
# root.mainloop()