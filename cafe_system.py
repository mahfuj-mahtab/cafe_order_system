from tkinter import *
import random
import time
import datetime
root=Tk()
root.geometry("1350x750+0+0")
root.title("cafe Management System")

#=====================================function===============================================
def totalbtn():
    coffee1=float(coffee1_entry.get())
    coffee2=float(coffee2_entry.get())
    coffee3=float(coffee3_entry.get())
    coffee4=float(coffee4_entry.get())
    coffee5=float(coffee5_entry.get())
    coffee6=float(coffee6_entry.get())
    coffee7=float(coffee7_entry.get())
    coffee8=float(coffee8_entry.get())
    coffee9=float(coffee9_entry.get())
    coffee10=float(coffee10_entry.get())
    coffee11=float(coffee11_entry.get())
    coffee12=float(coffee12_entry.get())
    coffee13=float(coffee13_entry.get())
    coffee14=float(coffee14_entry.get())
    coffee15=float(coffee15_entry.get())
    coffee16=float(coffee16_entry.get())
    coffee17=float(coffee17_entry.get())
    coffee18=float(coffee18_entry.get())
    coffee19=float(coffee19_entry.get())
    coffee20=float(coffee20_entry.get())
    coffee21=float(coffee21_entry.get())
    coffee22=float(coffee22_entry.get())
    total1=(coffee1 * 1.0)
    total2=(coffee2 * 1.0)
    total3=(coffee3 * 1.0)
    total4=(coffee4 * 1.0)
    total5=(coffee5 * 1.0)
    total6=(coffee6 * 1.0)
    total7=(coffee7 * 1.0)
    total8=(coffee8 * 1.0)
    total9=(coffee9 * 1.0)
    total10=(coffee10 * 1.0)
    total11=(coffee11 * 1.0)
    total12=(coffee12 * 1.0)
    total13=(coffee13 * 1.0)
    total14=(coffee14 * 1.0)
    total15=(coffee15 * 1.0)
    total16=(coffee16 * 1.0)
    total17=(coffee17 * 1.0)
    total18=(coffee18 * 1.0)
    total19=(coffee19 * 1.0)
    total20=(coffee20 * 1.0)
    total21=(coffee21 * 1.0)
    total22=(coffee22 * 1.0)
    
    total=(total1)
    print(total)

def chkbtn1():
    if var1.get() == 1:
        coffee1_entry.configure(state=NORMAL)
    elif var1.get() ==0:
        coffee1_entry.configure(state=DISABLED)


def chkbtn2():
    if var2.get() == 1:
        coffee2_entry.configure(state=NORMAL)
    elif var2.get() ==0:
        coffee2_entry.configure(state=DISABLED)

def chkbtn3():
    if var3.get() == 1:
        coffee3_entry.configure(state=NORMAL)
    elif var3.get() ==0:
        coffee3_entry.configure(state=DISABLED)

def chkbtn4():
    if var4.get() == 1:
        coffee4_entry.configure(state=NORMAL)
    elif var4.get() ==0:
        coffee4_entry.configure(state=DISABLED)

def chkbtn5():
    if var5.get() == 1:
        coffee5_entry.configure(state=NORMAL)
    elif var5.get() ==0:
        coffee5_entry.configure(state=DISABLED)

def chkbtn6():
    if var6.get() == 1:
        coffee6_entry.configure(state=NORMAL)
    elif var6.get() ==0:
        coffee6_entry.configure(state=DISABLED)

def chkbtn7():
    if var7.get() == 1:
        coffee7_entry.configure(state=NORMAL)
    elif var7.get() ==0:
        coffee7_entry.configure(state=DISABLED)

def chkbtn8():
    if var8.get() == 1:
        coffee8_entry.configure(state=NORMAL)
    elif var8.get() ==0:
        coffee8_entry.configure(state=DISABLED)

def chkbtn9():
    if var9.get() == 1:
        coffee9_entry.configure(state=NORMAL)
    elif var9.get() ==0:
        coffee9_entry.configure(state=DISABLED)

def chkbtn10():
    if var10.get() == 1:
        coffee10_entry.configure(state=NORMAL)
    elif var10.get() ==0:
        coffee10_entry.configure(state=DISABLED)

def chkbtn11():
    if var11.get() == 1:
        coffee11_entry.configure(state=NORMAL)
    elif var11.get() ==0:
        coffee11_entry.configure(state=DISABLED)

def chkbtn12():
    if var12.get() == 1:
        coffee12_entry.configure(state=NORMAL)
    elif var12.get() ==0:
        coffee12_entry.configure(state=DISABLED)

def chkbtn13():
    if var13.get() == 1:
        coffee13_entry.configure(state=NORMAL)
    elif var13.get() ==0:
        coffee13_entry.configure(state=DISABLED)

def chkbtn14():
    if var14.get() == 1:
        coffee14_entry.configure(state=NORMAL)
    elif var14.get() ==0:
        coffee14_entry.configure(state=DISABLED)

def chkbtn15():
    if var15.get() == 1:
        coffee15_entry.configure(state=NORMAL)
    elif var15.get() ==0:
        coffee15_entry.configure(state=DISABLED)

def chkbtn16():
    if var16.get() == 1:
        coffee16_entry.configure(state=NORMAL)
    elif var16.get() ==0:
        coffee16_entry.configure(state=DISABLED)

def chkbtn17():
    if var17.get() == 1:
        coffee17_entry.configure(state=NORMAL)
    elif var17.get() ==0:
        coffee17_entry.configure(state=DISABLED)

def chkbtn18():
    if var18.get() == 1:
        coffee18_entry.configure(state=NORMAL)
    elif var18.get() ==0:
        coffee18_entry.configure(state=DISABLED)

def chkbtn19():
    if var19.get() == 1:
        coffee19_entry.configure(state=NORMAL)
    elif var19.get() ==0:
        coffee19_entry.configure(state=DISABLED)

def chkbtn20():
    if var20.get() == 1:
        coffee20_entry.configure(state=NORMAL)
    elif var20.get() ==0:
        coffee20_entry.configure(state=DISABLED)

def chkbtn21():
    if var21.get() == 1:
        coffee21_entry.configure(state=NORMAL)
    elif var21.get() ==0:
        coffee21_entry.configure(state=DISABLED)

def chkbtn22():
    if var22.get() == 1:
        coffee22_entry.configure(state=NORMAL)
    elif var22.get() ==0:
        coffee22_entry.configure(state=DISABLED)


def exitbtn():
    
    root.destroy()


def resetbtn():
        strvar1.set("0")
        strvar2.set("0")
        strvar3.set("0")
        strvar4.set("0")
        strvar5.set("0")
        strvar6.set("0")
        strvar7.set("0")
        strvar8.set("0")
        strvar9.set("0")
        strvar10.set("0")
        strvar11.set("0")
        strvar12.set("0")
        strvar13.set("0")
        strvar14.set("0")
        strvar15.set("0")
        strvar16.set("0")
        strvar17.set("0")
        strvar18.set("0")
        strvar19.set("0")
        strvar20.set("0")
        strvar21.set("0")
        strvar22.set("0")
        coffee1_entry.configure(state=DISABLED)
        coffee2_entry.configure(state=DISABLED)
        coffee3_entry.configure(state=DISABLED)
        coffee4_entry.configure(state=DISABLED)
        coffee5_entry.configure(state=DISABLED)
        coffee6_entry.configure(state=DISABLED)
        coffee7_entry.configure(state=DISABLED)
        coffee8_entry.configure(state=DISABLED)
        coffee9_entry.configure(state=DISABLED)
        coffee10_entry.configure(state=DISABLED)
        coffee11_entry.configure(state=DISABLED)
        coffee12_entry.configure(state=DISABLED)
        coffee13_entry.configure(state=DISABLED)
        coffee14_entry.configure(state=DISABLED)
        coffee15_entry.configure(state=DISABLED)
        coffee16_entry.configure(state=DISABLED)
        coffee17_entry.configure(state=DISABLED)
        coffee18_entry.configure(state=DISABLED)
        coffee19_entry.configure(state=DISABLED)
        coffee20_entry.configure(state=DISABLED)
        coffee21_entry.configure(state=DISABLED)
        coffee22_entry.configure(state=DISABLED)
        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
        var7.set(0)
        var8.set(0)
        var9.set(0)
        var10.set(0)
        var11.set(0)
        var12.set(0)
        var13.set(0)
        var14.set(0)
        var15.set(0)
        var16.set(0)
        var17.set(0)
        var18.set(0)
        var19.set(0)
        var20.set(0)
        var21.set(0)
        var22.set(0)


#=============frame=========================

top=Frame(root,width=1350,height=100,bd=5,relief="raise")
top.pack(side=TOP)
main_frm=Frame(root,width=1350,height=650,relief="raise")
main_frm.pack(side=BOTTOM)
left=Frame(main_frm,width=850,height=650,bd=5,relief="raise")
left.pack(side=LEFT)
right=Frame(main_frm,width=500,height=650,bd=5,relief="raise")
right.pack(side=RIGHT)
left_top=Frame(left,width=850,height=450,relief="raise")
left_top.pack(side=TOP)
left_bottom=Frame(left,width=860,height=250,relief="raise",bg='white',bd=2)
left_bottom.pack(side=TOP)
left_left=Frame(left_top,width=400,height=450,bd=2,relief="raise")
left_left.pack(side=LEFT)
left_right=Frame(left_top,width=450,height=450,bd=2,relief="raise")
left_right.pack(side=RIGHT)

#==================right bottom frame==================================
right_top=Frame(right,width=500,height=100,bd=2,relief="raise",bg='red')
right_top.pack(side=TOP)
right_bottom=Frame(right,width=500,height=550,bd=2,relief="raise")
right_bottom.pack(side=BOTTOM)
right_bottom1=Frame(right_bottom,width=500,height=450,relief="raise")
right_bottom1.pack(side=TOP)

right_bottom2=Frame(right_bottom,width=500,height=100,relief="raise",bd=3)
right_bottom2.pack(side=BOTTOM)
lbl1=Label(top,text="   Cafe management system    ",font=('arial',70,'bold'),fg='red')
lbl1.grid(row=0,column=0)
lbl2=Label(right_top,text="Recipt",font=('arial',19,'bold'),bg='red',fg='white')
lbl2.place(x=200,y=30)
#=========frame end============
#=================================variable=================
strvar1=StringVar()
strvar2=StringVar()
strvar3=StringVar()
strvar4=StringVar()
strvar5=StringVar()
strvar6=StringVar()
strvar7=StringVar()
strvar8=StringVar()
strvar9=StringVar()
strvar10=StringVar()
strvar11=StringVar()
strvar12=StringVar()
strvar13=StringVar()
strvar14=StringVar()
strvar15=StringVar()
strvar16=StringVar()
strvar17=StringVar()
strvar18=StringVar()
strvar19=StringVar()
strvar20=StringVar()
strvar21=StringVar()
strvar22=StringVar()
strvar1.set("0")
strvar2.set("0")
strvar3.set("0")
strvar4.set("0")
strvar5.set("0")
strvar6.set("0")
strvar7.set("0")
strvar8.set("0")
strvar9.set("0")
strvar10.set("0")
strvar11.set("0")
strvar12.set("0")
strvar13.set("0")
strvar14.set("0")
strvar15.set("0")
strvar16.set("0")
strvar17.set("0")
strvar18.set("0")
strvar19.set("0")
strvar20.set("0")
strvar21.set("0")
strvar22.set("0")
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()

var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)
var12.set(0)
var13.set(0)
var14.set(0)
var15.set(0)
var16.set(0)
var17.set(0)
var18.set(0)
var19.set(0)
var20.set(0)
var21.set(0)
var22.set(0)
#===========================variable end==============================
coffee1=Checkbutton(left_left,text="coffee1\t\t\t2$",font=('arial',18,'bold'),variable=var1,onvalue=1,offvalue=0,command=chkbtn1)
coffee1.grid(row=0,column=0)
coffee2=Checkbutton(left_left,text="coffee1\t\t\t3$",font=('arial',18,'bold'),variable=var2,onvalue=1,offvalue=0,command=chkbtn2)
coffee2.grid(row=1,column=0)
coffee3=Checkbutton(left_left,text="coffee1\t\t\t4$",font=('arial',18,'bold'),variable=var3,onvalue=1,offvalue=0,command=chkbtn3)
coffee3.grid(row=2,column=0)
coffee4=Checkbutton(left_left,text="coffee1\t\t\t5$",font=('arial',18,'bold'),variable=var4,onvalue=1,offvalue=0,command=chkbtn4)
coffee4.grid(row=3,column=0)
coffee5=Checkbutton(left_left,text="coffee1\t\t\t2$",font=('arial',18,'bold'),variable=var5,onvalue=1,offvalue=0,command=chkbtn5)
coffee5.grid(row=4,column=0)
coffee6=Checkbutton(left_left,text="coffee1\t\t\t7$",font=('arial',18,'bold'),variable=var6,onvalue=1,offvalue=0,command=chkbtn6)
coffee6.grid(row=5,column=0)
coffee7=Checkbutton(left_left,text="coffee1\t\t\t28$",font=('arial',18,'bold'),variable=var7,onvalue=1,offvalue=0,command=chkbtn7)
coffee7.grid(row=6,column=0)
coffee8=Checkbutton(left_left,text="coffee1\t\t\t2$",font=('arial',18,'bold'),variable=var8,onvalue=1,offvalue=0,command=chkbtn8)
coffee8.grid(row=7,column=0)
coffee9=Checkbutton(left_left,text="coffee1\t\t\t24$",font=('arial',18,'bold'),variable=var9,onvalue=1,offvalue=0,command=chkbtn9)
coffee9.grid(row=8,column=0)
coffee10=Checkbutton(left_left,text="coffee1\t\t\t12$",font=('arial',18,'bold'),variable=var10,onvalue=1,offvalue=0,command=chkbtn10)
coffee10.grid(row=9,column=0)
coffee11=Checkbutton(left_left,text="coffee1\t\t\t42$",font=('arial',18,'bold'),variable=var11,onvalue=1,offvalue=0,command=chkbtn11)
coffee11.grid(row=10,column=0)


coffee12=Checkbutton(left_right,text="coffee1\t\t\t20$",font=('arial',18,'bold'),variable=var12,onvalue=1,offvalue=0,command=chkbtn12)
coffee12.grid(row=0,column=0)
coffee13=Checkbutton(left_right,text="coffee1\t\t\t9$",font=('arial',18,'bold'),variable=var13,onvalue=1,offvalue=0,command=chkbtn13)
coffee13.grid(row=1,column=0)
coffee14=Checkbutton(left_right,text="coffee1\t\t\t2$",font=('arial',18,'bold'),variable=var14,onvalue=1,offvalue=0,command=chkbtn14)
coffee14.grid(row=2,column=0)
coffee15=Checkbutton(left_right,text="coffee1\t\t\t1$",font=('arial',18,'bold'),variable=var15,onvalue=1,offvalue=0,command=chkbtn15)
coffee15.grid(row=3,column=0)
coffee16=Checkbutton(left_right,text="coffee1\t\t\t2$",font=('arial',18,'bold'),variable=var16,onvalue=1,offvalue=0,command=chkbtn16)
coffee16.grid(row=4,column=0)
coffee17=Checkbutton(left_right,text="coffee1\t\t\t7$",font=('arial',18,'bold'),variable=var17,onvalue=1,offvalue=0,command=chkbtn17)
coffee17.grid(row=5,column=0)
coffee18=Checkbutton(left_right,text="coffee1\t\t\t9$",font=('arial',18,'bold'),variable=var18,onvalue=1,offvalue=0,command=chkbtn18)
coffee18.grid(row=6,column=0)
coffee19=Checkbutton(left_right,text="coffee1\t\t\t5$",font=('arial',18,'bold'),variable=var19,onvalue=1,offvalue=0,command=chkbtn19)
coffee19.grid(row=7,column=0)
coffee20=Checkbutton(left_right,text="coffee1\t\t\t3$",font=('arial',18,'bold'),variable=var20,onvalue=1,offvalue=0,command=chkbtn20)
coffee20.grid(row=8,column=0)
coffee21=Checkbutton(left_right,text="coffee1\t\t\t2$",font=('arial',18,'bold'),variable=var21,onvalue=1,offvalue=0,command=chkbtn21)
coffee21.grid(row=9,column=0)
coffee22=Checkbutton(left_right,text="coffee1\t\t\t21$",font=('arial',18,'bold'),variable=var22,onvalue=1,offvalue=0,command=chkbtn22)
coffee22.grid(row=10,column=0)



coffee1_entry=Entry(left_left,font=('arial',13,'bold'),textvariable=strvar1,width=6,state=DISABLED)
coffee1_entry.grid(row=0,column=1)
coffee2_entry=Entry(left_left,font=('arial',13,'bold'),textvariable=strvar2,width=6,state=DISABLED)
coffee2_entry.grid(row=1,column=1)
coffee3_entry=Entry(left_left,font=('arial',13,'bold'),state=DISABLED,textvariable=strvar3,width=6)
coffee3_entry.grid(row=2,column=1)
coffee4_entry=Entry(left_left,font=('arial',13,'bold'),state=DISABLED,textvariable=strvar4,width=6)
coffee4_entry.grid(row=3,column=1)
coffee5_entry=Entry(left_left,font=('arial',13,'bold'),state=DISABLED,textvariable=strvar5,width=6)
coffee5_entry.grid(row=4,column=1)
coffee6_entry=Entry(left_left,font=('arial',13,'bold'),state=DISABLED,textvariable=strvar6,width=6)
coffee6_entry.grid(row=5,column=1)
coffee7_entry=Entry(left_left,font=('arial',13,'bold'),state=DISABLED,textvariable=strvar7,width=6)
coffee7_entry.grid(row=6,column=1)
coffee8_entry=Entry(left_left,font=('arial',13,'bold'),state=DISABLED,textvariable=strvar8,width=6)
coffee8_entry.grid(row=7,column=1)
coffee9_entry=Entry(left_left,font=('arial',13,'bold'),state=DISABLED,textvariable=strvar9,width=6)
coffee9_entry.grid(row=8,column=1)
coffee10_entry=Entry(left_left,font=('arial',13,'bold'),state=DISABLED,textvariable=strvar10,width=6)
coffee10_entry.grid(row=9,column=1)
coffee11_entry=Entry(left_left,font=('arial',13,'bold'),state=DISABLED,textvariable=strvar11,width=6)
coffee11_entry.grid(row=10,column=1)


coffee12_entry=Entry(left_right,font=('arial',13,'bold'),state=DISABLED,textvariable=strvar1,width=6)
coffee12_entry.grid(row=0,column=1)
coffee13_entry=Entry(left_right,font=('arial',13,'bold'),state=DISABLED,textvariable=strvar2,width=6)
coffee13_entry.grid(row=1,column=1)
coffee14_entry=Entry(left_right,font=('arial',13,'bold'),state=DISABLED,textvariable=strvar3,width=6)
coffee14_entry.grid(row=2,column=1)
coffee15_entry=Entry(left_right,font=('arial',13,'bold'),state=DISABLED,textvariable=strvar4,width=6)
coffee15_entry.grid(row=3,column=1)
coffee16_entry=Entry(left_right,font=('arial',13,'bold'),state=DISABLED,textvariable=strvar5,width=6)
coffee16_entry.grid(row=4,column=1)
coffee17_entry=Entry(left_right,font=('arial',13,'bold'),state=DISABLED,textvariable=strvar6,width=6)
coffee17_entry.grid(row=5,column=1)
coffee18_entry=Entry(left_right,font=('arial',13,'bold'),state=DISABLED,textvariable=strvar7,width=6)
coffee18_entry.grid(row=6,column=1)
coffee19_entry=Entry(left_right,font=('arial',13,'bold'),state=DISABLED,textvariable=strvar8,width=6)
coffee19_entry.grid(row=7,column=1)
coffee20_entry=Entry(left_right,font=('arial',13,'bold'),state=DISABLED,textvariable=strvar9,width=6)
coffee20_entry.grid(row=8,column=1)
coffee21_entry=Entry(left_right,font=('arial',13,'bold'),state=DISABLED,textvariable=strvar10,width=6)
coffee21_entry.grid(row=9,column=1)
coffee22_entry=Entry(left_right,font=('arial',13,'bold'),state=DISABLED,textvariable=strvar11,bd=2,width=6)
coffee22_entry.grid(row=10,column=1)
#======================left bottom frame=======================
lbl3=Label(left_bottom,text="Welcome in my software",font=('arial',15,'bold'),fg='black',bg='white')
lbl3.place(x=0,y=0)
#=================================================right bottom frame==============================

txt1=Text(right_bottom1,font=('arial',11,'bold'))
txt1.grid(row=0,column=0)
#=================button=====================
b1=Button(right_bottom2,text="Total",font=('arial',18,'bold'),fg='white',bg='black',command=totalbtn)
b1.place(x=50,y=10)
b2=Button(right_bottom2,text="Reset",font=('arial',18,'bold'),fg='white',bg='black',command=resetbtn)
b2.place(x=130,y=10)
b3=Button(right_bottom2,text="  exit ",font=('arial',18,'bold'),fg='white',bg='black',command=exitbtn)
b3.place(x=210,y=10)
b4=Button(right_bottom2,text="credit",font=('arial',18,'bold'),fg='white',bg='black')
b4.place(x=290,y=10)
root.mainloop()
