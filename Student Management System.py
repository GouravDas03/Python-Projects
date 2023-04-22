#Create the working part first
from tkinter import *
from tkinter import ttk
import csv
root=Tk()
root.geometry("1200x650")
root.configure(background='White')
root.title("Student Management System")
Label1=Label(root, text="Student Management System", font=('calliber', 40, "bold"), relief=GROOVE, bg="green", fg="red")
Label1.pack(side=TOP)
Label2=Label(root, text="Here you can enter, read and delete record of students", font=('Time New Roman', 28), fg="yellow", bg="blue") 
Label2.pack()
#Working for btn1
def Write():
    wx=Tk()
    wx.geometry("900x700")
    wx.title("Students Add")
    Label1=Label(wx, text="Please add the details of student", font=('times new roman', 25, "bold"), bg="orange", fg="white", padx=35, pady=20)
    Label1.grid(row=0, column=0, columnspan=20)
    p1=Label(wx, text="Roll No.", font=('calliber', 20, 'bold'), bg='crimson', fg='yellow')
    p1.grid(row=1, column=0, padx=10, pady=10)
    p2=Label(wx, text="Name", font=('calliber', 20, 'bold'),  bg='crimson', fg='yellow')
    p2.grid(row=2, column=0, padx=30, pady=30)
    p3=Label(wx, text="Date of Birth", font=('calliber', 20, 'bold'),  bg='crimson', fg='yellow')
    p3.grid(row=3, column=0, padx=30, pady=30)
    p4=Label(wx, text="Gender", font=('calliber', 20, 'bold'),  bg='crimson', fg='yellow')
    p4.grid(row=4, column=0, padx=30, pady=30)
    p5=Label(wx, text="Phone no.", font=('calliber', 20, 'bold'),  bg='crimson', fg='yellow')
    p5.grid(row=5, column=0, padx=30, pady=30)
    p6=Label(wx, text="Email", font=('calliber', 20, 'bold'),  bg='crimson', fg='yellow')
    p6.grid(row=6, column=0, padx=30, pady=30)
    txt1=Entry(wx, font=('calliber', 20, 'bold'), bd=6, relief=GROOVE)
    txt1.grid(row=1, column=1, padx=20, pady=10)
    txt2=Entry(wx, font=('calliber', 20, 'bold'), bd=6, relief=GROOVE)
    txt2.grid(row=2, column=1, padx=20, pady=10)
    txt3=Entry(wx, font=('calliber', 20, 'bold'), bd=6, relief=GROOVE)
    txt3.grid(row=3, column=1, padx=20, pady=10)
    combo_gender=ttk.Combobox(wx, font=('calliber', 20, 'bold'))
    combo_gender["values"]=["Male", "Female"]
    combo_gender.grid(row=4, column=1, padx=20, pady=10)
    txt4=Entry(wx, font=('calliber', 20, 'bold'), bd=6, relief=GROOVE)
    txt4.grid(row=5, column=1, padx=20, pady=10)
    txt5=Entry(wx, font=('calliber', 20, 'bold'), bd=6, relief=GROOVE)
    txt5.grid(row=6, column=1, padx=20, pady=10)
    #Now I have to create a function which will take these inputs and add them
    f=open("E:\Filehandling\Studentdata.csv", "a")
    L=[ ]
    S=[ ]
    L1=[ ]
    b=csv.writer(f)
    def ADD():
        L=[txt1.get(), txt2.get(), txt3.get(), combo_gender.get(), txt4.get(), txt5.get()]
        S.append(L)
    Add_btn=Button(wx, text="Add",  bg="orange", fg="white", font=('arial', 25, "bold"), width=10, height=2, command=ADD)
    Add_btn.grid(row=7, column=1)


    def Submit():
        for rec in S:
            if len(rec)!=0:
                L1.append(rec)
        b.writerows(L1)
        f.close()
    Sub_btn=Button(wx, text="Submit",  bg="green", fg="white", font=('arial', 25, "bold"), width=10, height=2, command=Submit)
    Sub_btn.grid(row=7, column=2)

    #Coding OP-Successful(Almost)


    
    


    
#Buttons and their workings
BTN1=Button(root, text="Add", bg="orange", fg="white", font=('arial', 25, "bold"), width=15, height=2, command=Write)
BTN1.pack(side=LEFT)


#Button2 for reading
def Read():
    f=open("E:\Filehandling\Studentdata.csv", "r")
    c=csv.reader(f)
    for row in c:
        if len(row)!=0:
            print(row)
    f.close()
#Working
BTN2=Button(root, text="Read",bg="turquoise", fg="red", font=('arial', 25, "bold"), width=15, height=2, command=Read)
BTN2.pack(side=LEFT)


def Delete():
    dx=Tk()
    dx.geometry("900x700")
    dx.title("Students record delete")
    Label1=Label(dx, text="Please enter the roll no. of student you want to delete", font=('times new roman', 25, "bold"), bg="orange", fg="white", padx=35, pady=20)
    Label1.grid(row=0, column=0, columnspan=20)
    tr1=Label(dx, text="Roll No.", font=('calliber', 20, 'bold'), bg='orange', relief=GROOVE)
    tr1.grid(row=1, column=0, padx=30, pady=30)
    En1=Entry(dx, font=('calliber', 20, 'bold'), bd=6, relief=GROOVE)
    En1.grid(row=1, column=1, padx=20, pady=10)
    L2=[ ]
    def deletedata():
        f=open("E:\Filehandling\Studentdata.csv", "r")
        L=csv.reader(f)
        found=0
        for rec in L:
            if len(rec)!=0:
                if rec[0]==En1.get():
                    del rec
                else:
                    L2.append(rec)
        f.close()
    delete_btn=Button(dx, text="Delete",  bg="white", fg="green", font=('arial', 25, "bold"), width=10, height=2, command=deletedata)
    delete_btn.grid(row=2, column=0)
    def adddata():
        f=open("E:\Filehandling\Studentdata.csv", "w")
        ls=csv.writer(f)
        ls.writerows(L2)
        f.close()
    add_btn=Button(dx, text="Add",  bg="blue", fg="white", font=('arial', 25, "bold"), width=10, height=2, command=adddata)
    add_btn.grid(row=2, column=1)
        

#Button 4
BTN4=Button(root, text="Delete", bg="white", fg="green", font=('arial', 25, "bold"), width=15, height=2, command=Delete)
BTN4.pack(side=LEFT)



root.mainloop()

    
                
                

            
                
        
