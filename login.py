from tkinter import *
from tkinter import messagebox
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title('File Based Record System')
        self.root.geometry('1350x700+0+0')
        self.root.config(bg='black')
        F1=Frame(self.root,bd=10,relief=GROOVE)
        F1.place(x=450,y=150,height=350)
        F1.config(bg='black',bd=5)

        self.user=StringVar()
        self.password=StringVar()

        title=Label(F1,text='Login System',bg='black',fg='pink',
                    font=('times new roman',30,'bold')).grid(row=0,columnspan=2,pady=20)

        labelUserName=Label(F1,text='User Name',bg='black',
                            fg='pink',font=('times new roman',25,'bold')).grid(row=1,column=0,pady=10,padx=10)
        textUserEntry=Entry(F1,bd=7,relief=GROOVE,textvariable=self.user,
                            width=25,font=('arial',15,'bold')).grid(row=1,column=1,padx=10,pady=10)

        labelPass=Label(F1,text='Password',bg='black',fg='pink',
                        font=('times new roman',25,'bold')).grid(row=2,column=0,pady=10,padx=10)
        textPass=Entry(F1,bd=7,show='*',relief=GROOVE,textvariable=self.password,
                       width=25,font=('arial',15,'bold')).grid(row=2,column=1,padx=10,pady=10)

        btnLog=Button(F1,text='Login',font='aria 15 bold',bd=7,
                      width=10,bg='black',fg='pink',command=self.logFunc).place(x=10,y=250)
        btnReset=Button(F1,text='Reset',font='aria 15 bold',bd=7,
                        width=10,bg='black',fg='pink',command=self.resetFunc).place(x=176,y=250)
        btnExit=Button(F1,text='Exit',font='aria 15 bold',bd=7,
                       width=10,bg='black',fg='pink',command=self.exitFunc).place(x=340,y=250)

    def logFunc(self):
        if self.user.get()=='Taaha' and self.password.get()=='123456':
            self.root.destroy()
            import software
            software.File_App()
        else:
            messagebox.showerror('Error','invalid username or password')

    def resetFunc(self):
        self.user.set('')
        self.password.set('')

    def exitFunc(self):
        option=messagebox.askyesno('Exit','Do you really want to exit??')
        if option>0:
            self.root.destroy()
        else:
            pass


root=Tk()
ob=Login(root)
root.mainloop()