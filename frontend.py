from tkinter import*
import tkinter.messagebox
import stdDatabase

class Student:


    def __init__(self,root):
        self.root = root
        self.root.title("Students Database Management System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="dark orange")

        StdID = StringVar()
        Firstname = StringVar()
        Lastname = StringVar()
        DOB = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Branch = StringVar()
        Mobileno = StringVar()

        #function

        def iExit():
            iExit=tkinter.messagebox.askyesno("Students Database Management System","Confirm if you want to Exit")
            if iExit > 0:
                root.destroy()
                return

        def clearData():
            self.txtStdID.delete(0,END)
            self.txtfna.delete(0, END)
            self.txtSna.delete(0, END)
            self.txtDOB.delete(0, END)
            self.txtAge.delete(0, END)
            self.txtGender.delete(0, END)
            self.txtBranch.delete(0, END)
            self.txtMobile.delete(0, END)


        def addData():
            if(len(StdID.get())!=0):
                stdDatabase.addStdRec(StdID.get(), Firstname.get(), Lastname.get(),DOB.get(), Age.get(), Gender.get() ,Branch.get() ,Mobileno.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(StdID.get(), Firstname.get(), Lastname.get(),DOB.get(), Age.get(), Gender.get() ,Branch.get() ,Mobileno.get()))


        def displayData():
            studentlist.delete(0, END)
            for row in stdDatabase.viewData():
                studentlist.insert(END,row,str(""))

        def StudentRec(event):
            global sd
            searchStd=studentlist.curselection()[0]
            sd=studentlist.get(searchStd)

            self.txtStdID.delete(0, END)
            self.txtStdID.insert(END,sd[1])
            self.txtfna.delete(0, END)
            self.txtfna.insert(END, sd[2])
            self.txtSna.delete(0, END)
            self.txtSna.insert(END, sd[3])
            self.txtDOB.delete(0, END)
            self.txtDOB.insert(END, sd[4])
            self.txtAge.delete(0, END)
            self.txtAge.insert(END, sd[5])
            self.txtGender.delete(0, END)
            self.txtGender.insert(END, sd[6])
            self.txtBranch.delete(0, END)
            self.txtBranch.insert(END, sd[7])
            self.txtMobile.delete(0, END)
            self.txtMobile.insert(END, sd[8])

        def DeleteData():
            if (len(StdID.get()) != 0):
                stdDatabase.deleteRec(sd[0])
                clearData()
                displayData()

        def searchDatabase():
            studentlist.delete(0, END)
            for row in stdDatabase.searchData(StdID.get(), Firstname.get(), Lastname.get(),DOB.get(), Age.get(), Gender.get() ,Branch.get() ,Mobileno.get()):
                studentlist.insert(END, row, str(""))

        def update():
            if (len(StdID.get()) != 0):
                stdDatabase.deleteRec(sd[0])
            if (len(StdID.get()) != 0):
                stdDatabase.addStdRec(StdID.get(), Firstname.get(), Lastname.get(), DOB.get(), Age.get(), Gender.get(), Branch.get(), Mobileno.get())
                studentlist.delete(0, END)
                studentlist.insert(END, (StdID.get(), Firstname.get(), Lastname.get(), DOB.get(), Age.get(), Gender.get(), Branch.get(),Mobileno.get()))

        #frames

        MainFrame = Frame(self.root, bg="dark orange")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2 , padx=54 , pady=8 ,  bg="dark salmon" , relief =RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame , font=('arial',47 ,'bold'), text= "Student Database Management Systems", bg="Ghost White")
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, bd=2 , width=1350 , height=70, padx=18, pady=10, bg="Ghost White", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=1300 , height=400,  padx=20, pady=20, bg="Ghost White", relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000 , height=600,  padx=20, bg="Ghost White", relief=RIDGE ,font=('arial',20 ,'bold') ,text="Student Info\n")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, bg="Ghost White", relief=RIDGE ,font=('arial',20 ,'bold') ,text="Student Details\n")
        DataFrameRIGHT.pack(side=RIGHT)

        #labels

        self.lblStdID = Label(DataFrameLEFT,font=('arial', 20, 'bold'), text="Student ID:", padx=2, pady= 2,bg="Ghost White")
        self.lblStdID.grid(row=0,column=0,sticky=W)
        self.txtStdID = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=StdID,width=39)
        self.txtStdID.grid(row=0, column=1)



        self.lblfna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="First Name:", padx=2, pady= 2,bg="Ghost White")
        self.lblfna.grid(row=1, column=0, sticky=W)
        self.txtfna = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Firstname, width=39)
        self.txtfna.grid(row=1, column=1)



        self.lblSna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Last Name:", padx=2, pady=2,
                            bg="Ghost White")
        self.lblSna.grid(row=2, column=0, sticky=W)
        self.txtSna = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Lastname, width=39)
        self.txtSna.grid(row=2, column=1)



        self.lblDOB = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Date of Birth:", padx=2, pady=2,
                            bg="Ghost White")
        self.lblDOB.grid(row=3, column=0, sticky=W)
        self.txtDOB = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=DOB, width=39)
        self.txtDOB.grid(row=3, column=1)



        self.lblAge = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Age:", padx=2, pady=2,
                            bg="Ghost White")
        self.lblAge.grid(row=4, column=0, sticky=W)
        self.txtAge = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Age, width=39)
        self.txtAge.grid(row=4, column=1)



        self.lblGender = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Gender:", padx=2, pady=2,
                            bg="Ghost White")
        self.lblGender.grid(row=5, column=0, sticky=W)
        self.txtGender = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Gender, width=39)
        self.txtGender.grid(row=5, column=1)


        self.lblBranch = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Branch:", padx=2, pady=2,
                               bg="Ghost White")
        self.lblBranch.grid(row=6, column=0, sticky=W)
        self.txtBranch = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Branch, width=39)
        self.txtBranch.grid(row=6, column=1)


        self.lblMobile = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Mobile:", padx=2, pady=2,
                               bg="Ghost White")
        self.lblMobile.grid(row=7, column=0, sticky=W)
        self.txtMobile = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Mobileno, width=39)
        self.txtMobile.grid(row=7, column=1)


        #listbox and scrollbar


        scrollbar= Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1,sticky='ns')


        studentlist= Listbox(DataFrameRIGHT, width=41, height=16, font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set )
        studentlist.bind('<<ListboxSelect>>',StudentRec)
        studentlist.grid(row=0, column=0,sticky='ns')
        scrollbar.config(command = studentlist.yview)

        #button widget


        self.btnAddData= Button(ButtonFrame, text='Add New',font=('arial',20, 'bold'), height=1, width=10, bd=4, command=addData)
        self.btnAddData.grid(row=0,column=0)
        self.btnDisplayData = Button(ButtonFrame, text='Display', font=('arial', 20, 'bold'), height=1, width=10, bd=4 ,command=displayData)
        self.btnDisplayData.grid(row=0, column=1)
        self.btnClearData = Button(ButtonFrame, text='Clear', font=('arial', 20, 'bold'), height=1, width=10, bd=4 ,command=clearData)
        self.btnClearData.grid(row=0, column=2)
        self.btnDeleteData = Button(ButtonFrame, text='Delete', font=('arial', 20, 'bold'), height=1, width=10, bd=4,command=DeleteData)
        self.btnDeleteData.grid(row=0, column=3)
        self.btnSearchData = Button(ButtonFrame, text='Search', font=('arial', 20, 'bold'), height=1, width=10, bd=4,command=searchDatabase)
        self.btnSearchData.grid(row=0, column=4)
        self.btnUpdateData = Button(ButtonFrame, text='Update', font=('arial', 20, 'bold'), height=1, width=10, bd=4,command=update)
        self.btnUpdateData.grid(row=0, column=5)
        self.btnExit = Button(ButtonFrame, text='Exit', font=('arial', 20, 'bold'), height=1, width=10, bd=4 ,command=iExit)
        self.btnExit.grid(row=0, column=6)


if __name__=='__main__':
    root=Tk()
    application= Student(root)
    root.mainloop()
