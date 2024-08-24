from tkinter import *
import mysql.connector as mc
from tkinter.font import Font
from tkinter import ttk

win = Tk()
win.title('Billing Software')
win.geometry('1366x768+0+0')
#win.iconbitmap('billingicon.ico')
win.config(bg ='gray')
win.state('zoomed')
myfont = Font(family='Calibri')
headfont = Font(family='times',slant='italic',weight='bold',size=10)
entryfont = Font(family='CourierNewBaltic',weight='normal',size=8,slant='roman')
dbc = mc.connect(host = 'localhost',user = 'root',password = '',db = 'billproject')
#Heading:
headframe = LabelFrame(win,text='Customer',font=(headfont),bg='black',fg='yellow',relief='groove',padx='2',pady='3')
headframe.pack(fill=X)
title = Label(headframe,text='Billing Software',font=(myfont,14,'bold'),bg='black',bd=5,fg='darkorange3')
title.pack(pady=15)

#Body:
name = StringVar()
number = IntVar()
bill = IntVar()
prname = StringVar()
prate = IntVar()
tqty = IntVar()

lblname = LabelFrame(win,text='Customer Details',font=(headfont),fg='red',bg='black',relief='raised')
lblname.pack(pady=3)
l1 = Label(lblname,text='Name',font=(myfont),fg='wheat',bg='black')
l1.grid(row=0,column=0,sticky='w',padx=20,pady=10)
e1 = Entry(lblname,textvariable=name,font=(entryfont),width=20,bd=5)
e1.grid(row=0,column=1,sticky='w',padx=20,pady=10)

l2 = Label(lblname,text='Phone',font=(myfont),fg='khaki',bg='black')
l2.grid(row=0,column=2,sticky='w',padx=20,pady=10)
e2 = Entry(lblname,textvariable=number,font=(entryfont),width=20,bd=5)
e2.grid(row=0,column=3,sticky='w',padx=20,pady=10)

lblnum = LabelFrame(win,text='Bill',font=(headfont),fg='salmon3',bg='black',relief='groove')
lblnum.pack()
l3 = Label(lblnum,text='Number',font=(myfont),fg='Darkorchid2',bg='black')
l3.grid(row=1,column=0,padx=20,sticky='w')
e3 = Entry(lblnum,textvariable=bill,font=(entryfont),width=20,bd=5)
e3.grid(row=0,column=1,sticky='w',padx=20,pady=4,rowspan=2)

#Button create
def search(*args):
    addbill = bill.get()
    mycur = dbc.cursor()
    mycur.execute("select * from customer where Billnum = %s" % addbill)
    output = mycur.fetchone()
    return lblbilarea.insert(END,output)
searchbt = Button(lblnum,text='SEARCH',font=(headfont),fg='old lace',bg='brown4',bd=6,activebackground='chocolate4',command= search,activeforeground='aquamarine')
searchbt.grid(row=0,column=2,sticky='w',padx=20,pady=4,rowspan=3)


qty1 = IntVar()
lblitems = LabelFrame(win,text='Products',font=(headfont),fg='purple1',background='black')
lblitems.pack(fill='both',pady=4)

lbitem1 = Label(lblitems,text='Bath soap',font=(myfont),fg='Steelblue1',bg='black')
lbitem1.grid(row=0,column=0,sticky='w',padx=10,pady=20)

entruitem1  = Entry(lblitems,textvariable=qty1,font=(entryfont),width=10,bd=5)
entruitem1.grid(row=0,column=1,sticky='w',padx=20,pady=20)

qty2 = IntVar()
lbitem2 = Label(lblitems,text='Face Cream',font=(myfont),fg='Steelblue1',bg='black')
lbitem2.grid(row=1,column=0,sticky='w',padx=10,pady=20)

entruitem2  = Entry(lblitems,textvariable=qty2,font=(entryfont),width=10,bd=5)
entruitem2.grid(row=1,column=1,sticky='w',padx=20,pady=20)

qty3 = IntVar()
lbitem3 = Label(lblitems,text='Shampoo',font=(myfont),fg='Steelblue1',bg='black')
lbitem3.grid(row=2,column=0,sticky='w',padx=10,pady=20)

entruitem3  = Entry(lblitems,textvariable=qty3,font=(entryfont),width=10,bd=5)
entruitem3.grid(row=2,column=1,sticky='w',padx=20,pady=20)

qty4 = IntVar()
lbitem4 = Label(lblitems,text='Hair Oil',font=(myfont),fg='Steelblue1',bg='black')
lbitem4.grid(row=3,column=0,sticky='w',padx=10,pady=20)

entruitem4  = Entry(lblitems,textvariable=qty4,font=(entryfont),width=10,bd=5)
entruitem4.grid(row=3,column=1,sticky='w',padx=20,pady=20)

qty5 = IntVar()
lbitem5 = Label(lblitems,text='Maaza',font=(myfont),fg='Steelblue1',bg='black')
lbitem5.grid(row=0,column=2,sticky='w',padx=50,pady=20)

entruitem5  = Entry(lblitems,textvariable=qty5,font=(entryfont),width=10,bd=5)
entruitem5.grid(row=0,column=3,sticky='w',padx=5,pady=20)

qty6 = IntVar()
lbitem6 = Label(lblitems,text='Sprite',font=(myfont),fg='Steelblue1',bg='black')
lbitem6.grid(row=1,column=2,sticky='w',padx=50,pady=20)

entruitem6  = Entry(lblitems,textvariable=qty6,font=(entryfont),width=10,bd=5)
entruitem6.grid(row=1,column=3,sticky='w',padx=5,pady=20)

qty7 = IntVar()
lbitem7 = Label(lblitems,text='Bovonto',font=(myfont),fg='Steelblue1',bg='black')
lbitem7.grid(row=2,column=2,sticky='w',padx=50,pady=20)

entruitem7  = Entry(lblitems,textvariable=qty7,font=(entryfont),width=10,bd=5)
entruitem7.grid(row=2,column=3,sticky='w',padx=5,pady=20)

qty8 = IntVar()
lbitem8 = Label(lblitems,text='Cocacola',font=(myfont),fg='Steelblue1',bg='black')
lbitem8.grid(row=3,column=2,sticky='w',padx=50,pady=20)

entruitem8  = Entry(lblitems,textvariable=qty8,font=(entryfont),width=10,bd=5)
entruitem8.grid(row=3,column=3,sticky='w',padx=5,pady=20)

qty9 = IntVar()
lbitem9 = Label(lblitems,text='Ice Cream',font=(myfont),fg='Steelblue1',bg='black')
lbitem9.grid(row=0,column=4,sticky='w',padx=50,pady=20)

entruitem9  = Entry(lblitems,textvariable=qty9,font=(entryfont),width=10,bd=5)
entruitem9.grid(row=0,column=5,sticky='w',padx=5,pady=20)

qty10 = IntVar()
lbitem10 = Label(lblitems,text='Cupcake',font=(myfont),fg='Steelblue1',bg='black')
lbitem10.grid(row=1,column=4,sticky='w',padx=50,pady=20)

entruitem10  = Entry(lblitems,textvariable=qty10,font=(entryfont),width=10,bd=5)
entruitem10.grid(row=1,column=5,sticky='w',padx=5,pady=20)

qty11 = IntVar()
lbitem11 = Label(lblitems,text='Chocolate',font=(myfont),fg='Steelblue1',bg='black')
lbitem11.grid(row=2,column=4,sticky='w',padx=50,pady=20)

entruitem11  = Entry(lblitems,textvariable=qty11,font=(entryfont),width=10,bd=5)
entruitem11.grid(row=2,column=5,sticky='w',padx=5,pady=20)

qty12 = IntVar()
lbitem12 = Label(lblitems,text='Biscuit',font=(myfont),fg='Steelblue1',bg='black')
lbitem12.grid(row=3,column=4,sticky='w',padx=50,pady=20)

entruitem12  = Entry(lblitems,textvariable=qty12,font=(entryfont),width=10,bd=5)
entruitem12.grid(row=3,column=5,sticky='w',padx=5,pady=20)


lblbillbox = LabelFrame(lblitems,text='Bill Box',font=(headfont),fg='blue2',bg='black',relief="raised")
lblbillbox.grid(row=0,column=6,padx=200,rowspan=20)

lblbilarea = Text(lblbillbox,font=('Calibri',10,'bold'),fg='black',bg='white',width=45,height=20)
lblbilarea.grid(row=0,column=8 ,padx=10,pady=10)


lblbilmenu = LabelFrame(win,text = 'Bill Menu',font=(headfont),bg='black',fg ='deeppink4',relief='sunken')
lblbilmenu.pack(fill=X)

lblproduct = Label(lblbilmenu,text='Product Name',font=(myfont),bg='black',fg='lightblue3')
lblproduct.grid(row=0,column=0,padx=10,pady=10)

proname = StringVar()
productname  = Entry(lblbilmenu,textvariable=proname,font=(entryfont),width=20,bd=3)
productname.grid(row=0,column=1,sticky='w',padx=5,pady=20)

lblQty= Label(lblbilmenu,text='Total Qty',font=(myfont),bg='black',fg='lightblue3')
lblQty.grid(row=0,column=2,padx=10,pady=10)

tqty = IntVar()
productqty  = Entry(lblbilmenu,textvariable=tqty,font=(entryfont),width=20,bd=3)
productqty.grid(row=0,column=3,sticky='w',padx=5,pady=20)

lblprice = Label(lblbilmenu,text='Total Amount',font=(myfont),bg='black',fg='lightblue3')
lblprice.grid(row=0,column=4,padx=10,pady=10)

tamount = IntVar()
productamount  = Entry(lblbilmenu,textvariable=tamount,font=(entryfont),width=20,bd=3)
productamount.grid(row=0,column=5,sticky='w',padx=5,pady=20)
def add(*args):
    productamount.delete(0,END)
    num1 =qty1.get()
    num2 = qty2.get()
    num3 = qty3.get()
    num4 = qty4.get()
    num5 = qty5.get()
    num6 = qty6.get()
    num7 = qty7.get()
    num8 = qty8.get()
    num9 = qty9.get()
    num10 = qty10.get()
    num11 = qty11.get()
    num12 = qty12.get()
    result = (num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10 + num11 + num12)
    addname= name.get()
    addnum = number.get()
    addbill = bill.get()
    addprname = proname.get()
    addtqty = tqty.get()
    output = result     
    cur = dbc.cursor()
    cur.execute ("insert into customer values('"+addname+"',%s,%s,'" +addprname+"',%s,%s)",(addnum,addbill,output,addtqty))
    dbc.commit()
    return   lblbilarea.insert(END,'Save Successfully :',cur),productamount.insert(END,output)
    
b1 = Button(lblbilmenu,text = 'Add',font =(myfont),fg ='cyan3',width=10,bg ='firebrick3',bd='6',relief='groove',command=add,activebackground='lightblue3',activeforeground='tomato')
b1.grid(row=0,column=6,padx=80,pady=30,sticky='w')

def print(*args):
    mycursor = dbc.cursor()
    sql = ("select * from customer")
    mycursor.execute(sql)
    result = mycursor.fetchall()
    output = result
    return lblbilarea.insert(END,output)

b2 = Button(lblbilmenu,text = 'Print',font =(myfont),fg ='dark orchid',width=10,bg ='saddle brown',bd='5',relief='groove',command=print,activebackground='orange2',activeforeground='cyan4')
b2.grid(row=0,column=7,padx=20,pady=30,sticky='w')

def clear():
    name.set("")
    number.set("")
    bill.set("")
    qty1.set("")
    qty2.set("")
    qty3.set("")
    qty4.set("")
    qty5.set("")
    qty6.set("")
    qty7.set("")
    qty8.set("")
    qty9.set("")
    qty10.set("")
    qty11.set("")
    qty12.set("")
    tqty.set("")
    tamount.set("")
    proname.set("")
    lblbilarea.delete(1.0,END)
    

    
b2 = Button(lblbilmenu,text = 'Clear',font =(myfont),fg ='blue4',width=10,bg ='medium purple4',bd='5',relief='groove',command=clear,activebackground='brown4',activeforeground='gold')
b2.grid(row=0,column=8,padx=80,pady=30,sticky='w')



win.mainloop()