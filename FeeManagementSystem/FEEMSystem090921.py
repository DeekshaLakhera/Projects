import pymysql as sq
from tkinter import *
import datetime
hname='localhost'
dbuser='root'
dbpass='shri krishna'
portno=3306
dbname='feemanagementsystem'
newn=''
rinste=''
regide=''
paye=''
newnp=''
blfee=''
bifee=''
con=sq.connect(host=hname,user=dbuser,password=dbpass, port=portno,db=dbname)
cur=con.cursor()
def installmentup():
    regid=int(regide.get().strip())
    querybal=f"select balancefee from fees where regid={regid}"
    cur.execute(querybal)
    fee=cur.fetchone()[0]
    queryinst=f"select remain_inst from fees where regid={regid}"
    cur.execute(queryinst)
    inst=cur.fetchone()[0]
    date=datetime.date.today()
    fquery=f"insert into installmentinfo (regid, balfee, inst, trdate) values ({regid},{fee},{inst},'{date}')";
    cur.execute(fquery)
    con.commit()
    print("Tables are updated")
    
def FinalPayment():
    global blfee,bifee,rinst
    regid=int(regide.get().strip())
    pay=int(paye.get().strip())
    print(blfee)
    finbal=blfee-pay
    inst=rinst-1
    balup=f"update fees set balancefee={finbal} where regid={regid}"
    cur.execute(balup)
    con.commit()
    instup=f"update fees set  remain_inst={inst} where regid={regid}"
    cur.execute(instup)
    con.commit()
    print("Paid")
    installmentup()
def paynow(self):
##    #Details of student
    global newnp 
    global blfee,bifee,rinst
    regid = int(regide.get().strip())
    print(type(regid))
    biquery= f"select balancefee,remain_inst from fees where regid={regid}"
    cur.execute(biquery)
    bifee=cur.fetchall()
    blfee=bifee[0][0]
    rinst=bifee[0][1]
    print(rinst)
    bllabel=Label(newnp,text="Balance Fee: "+str(blfee)).grid(row=2,column=0)
    instlabel=Label(newnp,text="Remaining installments: "+str(rinst)).grid(row=2,column=1)
    
def payment():
    global regide,paye
    global newnp
    newnp=Toplevel()
    regidl=Label(newnp,text="Enter Registration Id: ").grid(row=0,column=0)
    regide=Entry(newnp)
    regide.grid(row=0,column=1)
    payl=Label(newnp,text="Enter Amount to pay: ").grid(row=1,column=0)
    paye=Entry(newnp)
    paye.grid(row=1,column=1)
    payb=Button(newnp,text='Pay',command=FinalPayment).grid(row=4,column=1)
    regide.bind("<Return>",paynow)
def NewDetails():
    #things will save first in database"
    global newn
    crs=coursee.get().strip()
    mob=mobe.get().strip()
    fquery=f"select crsfee from courses where crsname='{crs}'"
    cur.execute(fquery)
    crsfee=cur.fetchone()[0]
    rquery=f"select regid from students where mobile='{mob}'"
    cur.execute(rquery)
    regid=cur.fetchone()[0]
    rinst=int(rinste.get())
    fequery=f"insert into fees (totalfee, balancefee, regid, remain_inst) values({crsfee}, {crsfee}, {regid}, {rinst})"
    cur.execute(fequery)
    con.commit()
    ridl=Label(newn,text="Student registration ID : "+str(regid)).grid(row=2,column=1)
    totalfeel=Label(newn,text="Total fee: "+str(crsfee)).grid(row=3,column=1)
    balancefeel=Label(newn,text="Balance Fee: "+str(crsfee)).grid(row=4,column=1)
    remainistl=Label(newn,text="Remained installments: "+str(rinst)).grid(row=5,column=1)
    finall=Label(newn,text="Student registered").grid(row=6,column=1)
def RegistrationWin():
    global newn,rinste
    names=namee.get().strip()
    crs=coursee.get().strip()
    mob=mobe.get().strip()
    mail=emaile.get().strip()
    clg=clge.get().strip()
    date=datetime.date.today()
    if names!=None and crs!=None and len(mob)>=10 and len(mob)<=12 and mail.find('@')!=-1 and clg!=None:
        iquery=f"insert into students (sname,course,mobile,email,college,regdate) values('{names}','{crs}','{mob}','{mail}','{clg}','{date}')"
        cur.execute(iquery)
        con.commit()
        newn=Toplevel()
        rinstl=Label(newn,text="Number of installments in you want to pay: ").grid(row=0,column=0)
        rinste=Entry(newn)
        rinste.grid(row=0,column=1)
        savebtn=Button(newn,text='Save',width=10,bg='green',fg='white',activebackground='blue',command=NewDetails).grid(row=0,column=2,padx=10)
    
if con!=None:
    print("connected")
    master=Tk()
    master.title('Registration')
    master.geometry('600x600')
    title=Label(master,text="REGISTRATION",fg='blue',font=('Times new roman',30)).grid(row=0,column=1)
    namel=Label(master,text="Student name ",font=('arial',20)).grid(row=2,column=0)
    namee=Entry(master,font=20)
    namee.grid(row=2,column=1)
    coursel=Label(master,text="Course ",font=('arial',20)).grid(row=3,column=0)
    coursee=Entry(master,font=20)
    coursee.grid(row=3,column=1)
    mobl=Label(master,text="Mobile Number ",font=('arial',20)).grid(row=4,column=0)
    mobe=Entry(master,font=20)
    mobe.grid(row=4,column=1)
    emaill=Label(master,text="Email ",font=('arial',20)).grid(row=5,column=0)
    emaile=Entry(master,font=20)
    emaile.grid(row=5,column=1)
    clgl=Label(master,text="College ",font=('arial',20)).grid(row=6,column=0)
    clge=Entry(master,font=20)
    clge.grid(row=6,column=1)
    regisbtn=Button(master,text='Register',font=20,fg='white',bg='green',activebackground='blue',command=RegistrationWin).grid(row=7,column=1,pady=20)
    paybtn=Button(master,text='Installment Pay',font=20,fg='white',bg='green',activebackground='blue',command=payment).grid(row=8,column=1,pady=20)
else:
    print("Failed")
    
