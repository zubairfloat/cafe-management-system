# login system of my cafe managemnet system its help you to connect any project a login system
#zubairfloat@gmail.com


from tkinter import *
import tkinter .messagebox
root1= Tk()
root1.geometry("500x300+600+300")

nameInput = StringVar()
passwordinput = StringVar()


def enter():
	if nameInput.get() == "zubair" and passwordinput.get() == "1234":
		root1.destroy()
		import main
	else:
		tkinter.messagebox.showinfo('Error','Authentication Failed')
		nameInput.set("")
		passwordinput.set("")

def destroy():
	root1.destroy()


logintitle = Label(root1, font = ('arial',50,'bold'), text ="Login", fg = "#336D9C", bd = 10)
logintitle.grid(row = 0, column=0 )

labelname = Label(root1,font = ('arial',20,'bold'), text= " Name" ,fg="#336D9C")
labelname.place(x=30,y=100)
labelnameentry = Entry(root1, fg="#B63A52", textvariable= nameInput, font = ("arial", 15, "bold") )
labelnameentry.place(x=180,y=100)


labelpassword = Label(root1,font = ('arial',20,'bold'), text= " Password" ,fg="#336D9C")
labelpassword.place(x=30,y=150)
labelpasswordentry = Entry(root1, fg="#B63A52",show= "*", textvariable= passwordinput,font = ("arial", 15, "bold") )
labelpasswordentry.place(x=180,y=150)

enterbtn = Button(root1, text="Enter", font = ('arial',10,'bold'),width=10,height=2, fg="#721C52", bg= "#E3E4E5", command= enter)
enterbtn.place(x=180,y=200)

exitbtn = Button(root1, text="Exit",font = ('arial',10,'bold'), fg="#721C52",width=10,height=2, bg= "#E3E4E5", command= destroy)
exitbtn.place(x=360,y=200)

root1.mainloop()

