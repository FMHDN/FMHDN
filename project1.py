#پاییز 1402

from tkinter import *

def submit1():
    
    operator2= e2.get()
    operator3= e3.get()
    operator4= e4.get()
    operator5= e5.get()
    operator6= e6.get()
    operator7= e7.get()
    operator8= e8.get()
    v.set(operator1+' '+operator2)
    a1.set(operator3)
    a2.set(operator4)
    c.set(operator5)
    s.set(operator6)
    p.set(operator7)
    co.set(operator8)

#------------------------------------------------------------------------------------------------------------------------------------------------------

def clear1():
    global operator1, operator2, operator3, operator4, operator5, operator6, operator7, operator8
    operator1= ''
    operator2= ''
    operator3= ''
    operator4= ''
    operator5= ''
    operator6= ''
    operator7= ''
    operator8= ''
    v.set(operator1+' '+operator2)
    a1.set(operator3)
    a2.set(operator4)
    c.set(operator5)
    s.set(operator6)
    p.set(operator7)
    co.set(operator8)
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
    e4.delete(0, 'end')
    e5.delete(0, 'end')
    e6.delete(0, 'end')
    e7.delete(0, 'end')
    e8.delete(0, 'end')

#-------------------------------------------------------------------------------------------------------------------------------------------------------

root=Tk()
root.title("Adress Entry Field")
Label(root, text='First Name    :', bg='light blue').grid(row=0)
Label(root, text='Last Name     :', bg='light green').grid(row=1)
Label(root, text='Adress Line 1 :', bg='yellow').grid(row=2)
Label(root, text='Adress Line 2 :', bg='pink').grid(row=3)
Label(root, text='City                  :', bg='light blue').grid(row=4)
Label(root, text='State/Province:', bg='orange').grid(row=5)
Label(root, text='Postal Code     :', bg='light green').grid(row=6)
Label(root, text='Country           :', bg='pink').grid(row=7)
e1= Entry(root)
e2= Entry(root)
e3= Entry(root)
e4= Entry(root)
e5= Entry(root)
e6= Entry(root)
e7= Entry(root)
e8= Entry(root)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)
e7.grid(row=6, column=1)
e8.grid(row=7, column=1)
v=StringVar()
a1=StringVar()
a2=StringVar()
c=StringVar()
s=StringVar()
p=IntVar()
co=StringVar()
operator1= ''
operator2= ''
operator3= ''
operator4= ''
operator5= ''
operator6= ''
operator7= ''
operator8= ''

label=Label(root, textvariable=v).grid(row=10)
label=Label(root, textvariable=a1).grid(row=11)
label=Label(root, textvariable=a2).grid(row=12)
label=Label(root, textvariable=c).grid(row=13)
label=Label(root, textvariable=s).grid(row=14)
label=Label(root, textvariable=p).grid(row=15)
label=Label(root, textvariable=co).grid(row=16)


button1=Button(root, text='SUBMIT', command=submit1, bg='light yellow').grid(row=9, column=4)
button2=Button(root, text='CLEAR', command=clear1, bg='light yellow').grid(row=9, column=3)

root.mainloop()









