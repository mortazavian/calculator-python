from tkinter import *

global math

root = Tk()

root.title("Calculator")

e = Entry(root,width=60,borderwidth=5)
e.grid(columnspan=3)

def button_click(number):
	#e.delete(0, END)
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))

def button_clear():
	e.delete(0, END)


def button_add():
	first_number = e.get()
	global f_num
	global math
	math = "addition"
	f_num = int(first_number)
	e.delete(0, END)

def button_equal():
	second_number = e.get()
	e.delete(0, END)
	
	if math == "addition":
		e.insert(0, f_num + int(second_number))

	if math == "subtraction":
		e.insert(0, f_num - int(second_number))

	if math == "multiplication":
		e.insert(0, f_num * int(second_number))

	if math == "division":
		e.insert(0, f_num / int(second_number))

def button_subtract():
	first_number = e.get()
	global f_num
	global math
	math = "subtraction"
	f_num = int(first_number)
	e.delete(0, END)

def button_multiply():
	first_number = e.get()
	global f_num
	global math
	math = "multiplication"
	f_num = int(first_number)
	e.delete(0, END)

def button_divide():
	first_number = e.get()
	global f_num
	global math
	math = "division"
	f_num = int(first_number)
	e.delete(0, END)



buttonClear = Button(root,width=52,height=8,text="Clear",command=button_clear)
buttonClear.grid(row=1,column=0,columnspan=3)

button7 = Button(root,width=16,height=8,text="7",command=lambda: button_click(7)).grid(row=3,column=0)
button8 = Button(root,width=16,height=8,text="8",command=lambda: button_click(8)).grid(row=3,column=1)
button9 = Button(root,width=16,height=8,text="9",command=lambda: button_click(9)).grid(row=3,column=2)

button4 = Button(root,width=16,height=8,text="4",command=lambda: button_click(4)).grid(row=4,column=0)
button5 = Button(root,width=16,height=8,text="5",command=lambda: button_click(5)).grid(row=4,column=1)
button6 = Button(root,width=16,height=8,text="6",command=lambda: button_click(6)).grid(row=4,column=2)

button1 = Button(root,width=16,height=8,text="1",command=lambda: button_click(1)).grid(row=5,column=0)
button2 = Button(root,width=16,height=8,text="2",command=lambda: button_click(2)).grid(row=5,column=1)
button3 = Button(root,width=16,height=8,text="3",command=lambda: button_click(3)).grid(row=5,column=2)


button0 = Button(root,width=16,height=8,text="0",command=lambda: button_click(0)).grid(row=6,column=0)
buttonEqual = Button(root,width=34,height=8,text="=",command=button_equal).grid(row=6,column=1,columnspan=2)

buttonPlus = Button(root,width=16,height=8,text="+",command=button_add).grid(row=7,column=0)
buttonSubtract = Button(root,width=16,height=8,text="-",command=button_subtract).grid(row=7,column=1)
buttonMul = Button(root,width=16,height=8,text="*",command=button_multiply).grid(row=7,column=2)

root.mainloop()