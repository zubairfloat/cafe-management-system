# cafe manaegemnt system buil in tkinter python gui frame work by Zubair rizwan
#zubairfloat@gmail.com



from tkinter import *
import tkinter.messagebox
from time import strftime
import random
import time

root=Tk()

root.geometry("1300x750+0+0")
root.title("cafe management system ")
root.configure(background= "black")

#================= Make Frames Ajustment =====================
top = Frame(root, width=1650,height=180,bd=15, relief= GROOVE, bg= "#336D9C" )
top.pack()

frameLeft=Frame(root,width=1050,height=640,bd=10,relief=GROOVE,bg= "#336D9C")
frameLeft.place(x=0,y=200)

frameRight=Frame(root,width=550,height=640,bd=10,relief=GROOVE)
frameRight.place(x=1050,y=200)

frameLeft1=Frame(frameLeft,width=1030,height=370,bd=10,relief=GROOVE,bg="#E3E4E5")
frameLeft1.place(x=0,y=0)

frameLeft2=Frame(frameLeft,width=1030,height=255,bd=10,relief=GROOVE,bg="#E3E4E5")
frameLeft2.place(x=0,y=368)



#================= Title ======================================
titlelabel=Label(top, font= ('arial',92,'bold'),text= "Cafe Management System ",bd=10,fg="#336D9C",bg="#E3E4E5")
titlelabel.grid(row=0,column=0)

#================= Variabels using to calculation ==================
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27= IntVar()

DateofOrder= StringVar()
ReceiptRef = StringVar()
Paidtext = StringVar()
subtotal = StringVar()
Totalcost= StringVar()
CostofBurger= StringVar()
Costofdrinks = StringVar()
CostofPizza= StringVar()
CostofOthers = StringVar()
servicecharge = StringVar()
RandomRef= StringVar()


E_drinksLare = StringVar()
E_drinksSmall= StringVar()
E_chocolate = StringVar()
E_moltenlava = StringVar()
E_bbqRunch  = StringVar()
E_juicemix = StringVar()
E_gardensalad = StringVar()
E_pickelpizza= StringVar()
E_chickenfajita = StringVar()
E_vegitablePizza= StringVar()
E_chickenChapli= StringVar()
E_pepporonipizza = StringVar()
E_mughlaipizza = StringVar()
E_zingerburger= StringVar()
E_cripsyburger = StringVar()
E_krizmaburger = StringVar()
E_Grillburger = StringVar()
E_friedsrl = StringVar()

E_drinksLare.set("0")
E_drinksSmall.set("0")
E_chocolate.set("0")
E_moltenlava.set("0")
E_bbqRunch.set("0")
E_juicemix.set("0")
E_gardensalad.set("0")
E_pickelpizza.set("0")
E_chickenfajita.set("0")
E_vegitablePizza.set("0")
E_chickenChapli.set("0")
E_pepporonipizza.set("0")
E_mughlaipizza.set("0")
E_zingerburger.set("0")
E_cripsyburger.set("0")
E_krizmaburger.set("0")
E_Grillburger.set("0")
E_friedsrl.set("0")
#=============== Set value for variables =====================
var1.set("0")
var2.set("0")
var3.set("0")
var4.set("0")
var5.set("0")
var6.set("0")
var7.set("0")
var8.set("0")
var9.set("0")
var10.set("0")
var11.set("0")
var12.set("0")
var13.set("0")
var14.set("0")
var15.set("0")
var16.set("0")
var17.set("0")
var18.set("0")
var19.set("0")
var20.set("0")
var21.set("0")
var22.set("0")
var23.set("0")
var24.set("0")
var25.set("0")
var26.set("0")
var27.set("0")

DateofOrder.set(time.strftime("%d/%m/%y"))

#============================= Items Sections Stock ========================
                       #------ Large Drinks --------
dlarge = Checkbutton(frameLeft1, text="Drinks Large",bg="#E3E4E5", variable=var1,onvalue=1,offvalue=0,font=('arial',18,'bold'))
dlarge.place(x=0,y=0)
dlargentry =Entry(frameLeft1, font=('arial',16,'bold'), bg="#E3E4E5",textvariable=E_drinksLare, bd=8,width=6)
dlargentry.place(x=230,y=2)
                       #------ Small Drinks ---------
dsmall = Checkbutton(frameLeft1, text="Drinks Small",bg="#E3E4E5", variable=var2,onvalue=1,offvalue=0,font=('arial',18,'bold'))
dsmall.place(x=0,y=60)
dsmallentry =Entry(frameLeft1, font=('arial',16,'bold'),bg="#E3E4E5", textvariable=E_drinksSmall,bd=8,width=6)
dsmallentry.place(x=230,y=60)
                       #------ Choco Malt ------------
chocmalt = Checkbutton(frameLeft1, text="Chocolate Malt", bg="#E3E4E5",variable=var3,onvalue=1,offvalue=0,font=('arial',18,'bold'))
chocmalt.place(x=0,y=120)
chocmaltentry =Entry(frameLeft1, font=('arial',16,'bold'),bg="#E3E4E5",textvariable=E_chocolate, bd=8,width=6)
chocmaltentry.place(x=230,y=120)
                       #------- Molten Malt -------------
molten= Checkbutton(frameLeft1, text="Molten Lava", bg="#E3E4E5",variable=var4,onvalue=1,offvalue=0,font=('arial',18,'bold'))
molten.place(x=0,y=180)
moletnEntry =Entry(frameLeft1, font=('arial',16,'bold'), bg="#E3E4E5",textvariable=E_moltenlava, bd=8,width=6)
moletnEntry.place(x=230,y=180)
                       #------- Bar-b-Q Ranch  -----------------
bbq = Checkbutton(frameLeft1, text="Bbq Ranch", bg="#E3E4E5",variable=var5,onvalue=1,offvalue=0,font=('arial',18,'bold'))
bbq.place(x=0,y=240)
bbqEntry =Entry(frameLeft1, font=('arial',16,'bold'), bg="#E3E4E5",textvariable=E_bbqRunch, bd=8,width=6)
bbqEntry.place(x=230,y=240)
                       #-------- Juice Small --------------------
sjuice = Checkbutton(frameLeft1, text="Juice Mix", bg="#E3E4E5",variable=var6,onvalue=1,offvalue=0,font=('arial',18,'bold'))
sjuice.place(x=0,y=300)
sjuiceEntry=Entry(frameLeft1, font=('arial',16,'bold'), bg="#E3E4E5",textvariable=E_juicemix, bd=8,width=6)
sjuiceEntry.place(x=230,y=300)

                       #--------- Garden Salad ------------------
salad= Checkbutton(frameLeft1, text="Garden Salad ",bg="#E3E4E5", variable=var8,onvalue=1,offvalue=0,font=('arial',18,'bold'))
salad.place(x=350,y=2)
saladEntry=Entry(frameLeft1, font=('arial',16,'bold'),bg="#E3E4E5", textvariable=E_gardensalad, bd=8,width=6)
saladEntry.place(x=580,y=2)
                      #--------- Pickel Pizza -------------------
pickelpizza= Checkbutton(frameLeft1, text="Pickel Pizza",bg="#E3E4E5", variable=var10,onvalue=1,offvalue=0,font=('arial',18,'bold'))
pickelpizza.place(x=350,y=60)
pickelpizzaEntry=Entry(frameLeft1, font=('arial',16,'bold'),bg="#E3E4E5", textvariable=E_pickelpizza, bd=8,width=6)
pickelpizzaEntry.place(x=580,y=60)
                      #--------- Chicken Pizza ------------------
chikenfajita = Checkbutton(frameLeft1, text="Chicken Fajita",bg="#E3E4E5", variable=var11,onvalue=1,offvalue=0,font=('arial',18,'bold'))
chikenfajita.place(x=350,y=120)
chikenfajitaEntry=Entry(frameLeft1, font=('arial',16,'bold'),bg="#E3E4E5", textvariable= E_chickenfajita,bd=8,width=6)
chikenfajitaEntry.place(x=580,y=120)
                      #--------- Vegitaable Pizaa ---------------
vegetablepizza= Checkbutton(frameLeft1, text="Vegitable Pizza",bg="#E3E4E5", variable=var12,onvalue=1,offvalue=0,font=('arial',18,'bold'))
vegetablepizza.place(x=350,y=180)
vegetablepizzaEntry=Entry(frameLeft1, font=('arial',16,'bold'),bg="#E3E4E5", textvariable=E_vegitablePizza, bd=8,width=6)
vegetablepizzaEntry.place(x=580,y=180)
                      #--------- Chicken Chappli Pizza ----------
chapli= Checkbutton(frameLeft1, text="Chiken Chapli",bg="#E3E4E5", variable=var13,onvalue=1,offvalue=0,font=('arial',18,'bold'))
chapli.place(x=350,y=240)
chapliEntry=Entry(frameLeft1, font=('arial',16,'bold'),bg="#E3E4E5", textvariable= E_chickenChapli, bd=8,width=6)
chapliEntry.place(x=580,y=240)
                      #--------- Pepperoni Pizza ----------------
pepperonipizza= Checkbutton(frameLeft1, text="Pepperoni Pizza",bg="#E3E4E5", variable=var14,onvalue=1,offvalue=0,font=('arial',18,'bold'))
pepperonipizza.place(x=350,y=300)
pepperonipizzaEntry=Entry(frameLeft1, font=('arial',16,'bold'),bg="#E3E4E5", textvariable=E_pepporonipizza, bd=8,width=6)
pepperonipizzaEntry.place(x=580,y=300)
                      #--------- Mughlai Pizza -------------------
mughalai = Checkbutton(frameLeft1, text="Mughlai Pizza",bg="#E3E4E5", variable=var15,onvalue=1,offvalue=0,font=('arial',18,'bold'))
mughalai.place(x=700,y=2)
mughalaiEntry=Entry(frameLeft1, font=('arial',16,'bold'),bg="#E3E4E5", textvariable=E_mughlaipizza, bd=8,width=6)
mughalaiEntry.place(x=918,y=2)
                      #--------- Zinger Burger -------------------
zingerburger = Checkbutton(frameLeft1, text="Zinger Burger",bg="#E3E4E5", variable=var19,onvalue=1,offvalue=0,font=('arial',18,'bold'))
zingerburger.place(x=700,y=60)
zingerburgerEntry=Entry(frameLeft1, font=('arial',16,'bold'),bg="#E3E4E5", textvariable= E_zingerburger,bd=8,width=6)
zingerburgerEntry.place(x=918,y=60)
                      #---------- Crispy Burger ------------------
crispyb = Checkbutton(frameLeft1, text="Crispy Burger", bg="#E3E4E5",variable=var20,onvalue=1,offvalue=0,font=('arial',18,'bold'))
crispyb.place(x=700,y=120)
crispybEntry=Entry(frameLeft1, font=('arial',16,'bold'), bg="#E3E4E5",textvariable= E_cripsyburger, bd=8,width=6)
crispybEntry.place(x=918,y=120)
                      #---------- Krizma Burger ------------------
krizmaburger = Checkbutton(frameLeft1, text="Krizma Burger",bg="#E3E4E5", variable=var21,onvalue=1,offvalue=0,font=('arial',18,'bold'))
krizmaburger.place(x=700,y=180)
krizmaburgerEntry=Entry(frameLeft1, font=('arial',16,'bold'),bg="#E3E4E5", textvariable=E_krizmaburger, bd=8,width=6)
krizmaburgerEntry.place(x=918,y=180)
                      #---------- Grill Burger -------------------
grillb= Checkbutton(frameLeft1, text="Grill Burger", bg="#E3E4E5",variable=var22,onvalue=1,offvalue=0,font=('arial',18,'bold'))
grillb.place(x=700,y=240)
grillbEntry=Entry(frameLeft1, font=('arial',16,'bold'),bg="#E3E4E5",textvariable=E_Grillburger, bd=8,width=6)
grillbEntry.place(x=918,y=240)
                      #-------------- Fries ----------------------
fries= Checkbutton(frameLeft1, text="Fries S/R/L",bg="#E3E4E5", variable=var16,onvalue=1,offvalue=0,font=('arial',18,'bold'))
fries.place(x=700,y=300)
friesEntry=Entry(frameLeft1, font=('arial',16,'bold'),bg="#E3E4E5", textvariable= E_friedsrl, bd=8,width=6)
friesEntry.place(x=918,y=300)
#============================ Information ===============================
recieptLabe=Label(frameRight, font=('arial',12,'bold'),text="Reciept:",bd=6,bg="black", fg="white",width=15)
recieptLabe.place(x=0,y=0)
texReciept=Text(frameRight, width=64, height=27,bg="white",bd=8,font = ('arial',11,'bold'))
texReciept.place(x=0,y=35)

#=========================================== Timer Function =================================================
def time():
    string = strftime('%H:%M:%S %p')
    timerfunc.config(text=string)
    timerfunc.after(1000, time)

#================================== Timer ============================================
timerfunc = Label(frameRight, font=('calibri', 18, 'bold'),bg='#F5F5F5',foreground='black',width = 28)
timerfunc.place(x=160,y=0)
time()
#============================ Cost Items Information ========================
labelcostofdrinks = Label(frameLeft2, font= ('arial',16,'bold' ), text="Cost of Drinks ",bd=8,bg="#E3E4E5",)
labelcostofdrinks.place(x=0,y=0)
costofdrinksEntry = Entry(frameLeft2,bg="#E3E4E5", font=('arial',16,'bold'), bd=8,justify =LEFT,textvariable=Costofdrinks)
costofdrinksEntry.place(x=250,y=0)


labelcostofburgers = Label(frameLeft2,bg="#E3E4E5", font= ('arial',16,'bold' ), text="Cost of Burgers",bd=8)
labelcostofburgers.place(x=0,y=60)
costofburgersEntry = Entry(frameLeft2,bg="#E3E4E5",font= ('arial',16,'bold'), bd=8,justify =LEFT,textvariable=CostofBurger)
costofburgersEntry.place(x=250,y=60)

labelcostofPizza = Label(frameLeft2,bg="#E3E4E5", font= ('arial',16,'bold' ), text="Cost of Pizza",bd=8)
labelcostofPizza.place(x=0,y=120)
costofPizzaEntry = Entry(frameLeft2,bg="#E3E4E5",font= ('arial',16,'bold'), bd=8,justify =LEFT,textvariable=CostofPizza)
costofPizzaEntry.place(x=250,y=120)

labelcostofothers = Label(frameLeft2,bg="#E3E4E5", font= ('arial',16,'bold' ), text="Cost of Others",bd=8)
labelcostofothers.place(x=0,y=180)
costofotherEntry = Entry(frameLeft2,bg="#E3E4E5",font= ('arial',16,'bold'), bd=8,justify =LEFT,textvariable=CostofOthers)
costofotherEntry.place(x=250,y=180)


#============================ Payments Methods ==================================
labelsurvicecharges  = Label(frameLeft2,bg="#E3E4E5", font= ('arial',16,'bold' ), text=" Survice charges ",bd=8)
labelsurvicecharges.place(x=520,y=0)
survicechargesEntry = Entry(frameLeft2, bg="#E3E4E5",font=('arial',16,'bold'), bd=8,justify =LEFT,textvariable=servicecharge)
survicechargesEntry.place(x=720,y=0)

labelTex = Label(frameLeft2, bg="#E3E4E5",font= ('arial',16,'bold' ), text="Tax ",bd=8)
labelTex.place(x=520,y=60)
texEntry = Entry(frameLeft2, bg="#E3E4E5",font=('arial',16,'bold'), bd=8,justify =LEFT,textvariable=Paidtext)
texEntry.place(x=720,y=60)

subtotalLabel = Label(frameLeft2,bg="#E3E4E5", font= ('arial',16,'bold' ), text=" Sub Total  ",bd=8)
subtotalLabel.place(x=520,y=120)
subtotalEntry = Entry(frameLeft2,bg="#E3E4E5", font=('arial',16,'bold'), bd=8,justify =LEFT,textvariable=subtotal)
subtotalEntry.place(x=720,y=120)

totalCost = Label(frameLeft2,bg="#E3E4E5", font= ('arial',16,'bold' ), text="Total Cost ",bd=8)
totalCost.place(x=520,y=180)
totalCOstEntry = Entry(frameLeft2,bg="#E3E4E5", font=('arial',16,'bold'), bd=8,justify =LEFT,textvariable=Totalcost)
totalCOstEntry.place(x=720,y=180)
#========================== Methods Defination ====================
def qExit():
    qExit=tkinter.messagebox.askyesno("Quick Question","Do You Want To Quit?")

    if qExit>0:
        root.destroy()
        return

def reset():
    Paidtext.set("")
    subtotal.set("")
    Totalcost.set("")
    Costofdrinks.set("")
    CostofBurger.set("")
    CostofPizza.set("")
    CostofOthers.set("")
    servicecharge.set("")
    texReciept.delete("1.0", END)



    E_drinksLare.set("0")
    E_drinksSmall.set("0")
    E_chocolate.set("0")
    E_moltenlava.set("0")
    E_bbqRunch.set("0")
    E_juicemix.set("0")
    E_gardensalad.set("0")
    E_pickelpizza.set("0")
    E_chickenfajita.set("0")
    E_vegitablePizza.set("0")
    E_chickenChapli.set("0")
    E_pepporonipizza.set("0")
    E_mughlaipizza.set("0")
    E_zingerburger.set("0")
    E_krizmaburger.set("0")
    E_Grillburger.set("0")
    E_friedsrl.set("0")
    E_cripsyburger.set("0")


    var1.set("0")
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")
    var7.set("0")
    var8.set("0")
    var9.set("0")
    var10.set("0")
    var11.set("0")
    var12.set("0")
    var13.set("0")
    var14.set("0")
    var15.set("0")
    var16.set("0")
    var17.set("0")
    var18.set("0")
    var19.set("0")
    var20.set("0")
    var21.set("0")
    var22.set("0")
    var23.set("0")
    var24.set("0")
    var25.set("0")
    var26.set("0")
    var27.set("0")

""" dlargentry.configure(state = DISABLED)
    dsmallentry.configure(state = DISABLED)
    chocmaltentry.configure(state= DISABLED)
    moletnEntry.configure(state= DISABLED)
    bbqEntry.configure(state= DISABLED)
    sjuiceEntry.configure(state = DISABLED)
    saladEntry.configure(state= DISABLED)
    pickelpizzaEntry.configure(state=DISABLED)
    chikenfajitaEntry.configure(state = DISABLED)
    vegetablepizzaEntry.configure(state= DISABLED)
    chapliEntry.configure(state=DISABLED)
    pepperonipizzaEntry.configure(state=DISABLED)
    mughalaiEntry.configure(state=DISABLED)
    zingerburgerEntry.configure(state=DISABLED)
    crispybEntry.configure(state=DISABLED)
    krizmaburgerEntry.configure(state=DISABLED)
    grillbEntry.configure(state=DISABLED)
    friesEntry.configure(state=DISABLED)

"""

#=============================== Check Buttons ===============
def checkButton_value():

    if(var1.get() == 1):
        dlarge.configure(state = NORMAL)
    elif var1.get() == 0:
        dlarge.configure(state=DISABLED)
        E_drinksLare.set("0")

    if (var2.get() == 1):
        dsmall.configure(state=NORMAL)
    elif var2.get() == 0:
        dsmall.configure(state=DISABLED)
        E_drinksSmall.set("0")
    if (var3.get() == 1):
        chocmalt.configure(state=NORMAL)
    elif var3.get() == 0:
        chocmalt.configure(state=DISABLED)
        E_chocolate.set("0")
    if (var4.get() == 1):
        molten.configure(state=NORMAL)
    elif var4.get() == 0:
        molten.configure(state=DISABLED)
        E_moltenlava.set("0")
    if (var5.get() == 1):
        bbq.configure(state=NORMAL)
    elif var5.get() == 0:
        bbq.configure(state=DISABLED)
        E_bbqRunch.set("0")
    if (var6.get() == 1):
        sjuice.configure(state=NORMAL)
    elif var6.get() == 0:
        sjuice.configure(state=DISABLED)
        E_juicemix.set("0")
    if (var7.get() == 1):
        salad.configure(state=NORMAL)
    elif var7.get() == 0:
        salad.configure(state=DISABLED)
        E_gardensalad.set("0")
    if (var8.get() == 1):
        pickelpizza.configure(state=NORMAL)
    elif var8.get() == 0:
        pickelpizza.configure(state=DISABLED)
        E_pickelpizza.set("0")
    if (var9.get() == 1):
        chikenfajita.configure(state=NORMAL)
    elif var9.get() == 0:
        chikenfajita.configure(state=DISABLED)
        E_chickenfajita.set("0")
    if (var10.get() == 1):
        vegetablepizza.configure(state=NORMAL)
    elif var10.get() == 0:
        vegetablepizza.configure(state=DISABLED)
        E_vegitablePizza.set("0")
    if (var11.get() == 1):
        chapli.configure(state=NORMAL)
    elif var11.get() == 0:
        chapli.configure(state=DISABLED)
        E_chickenChapli.set("0")
    if (var12.get() == 1):
        pepperonipizza.configure(state=NORMAL)
    elif var12.get() == 0:
        pepperonipizza.configure(state=DISABLED)
        E_pepporonipizza.set("0")
    if (var13.get() == 1):
        mughalai.configure(state=NORMAL)
    elif var13.get() == 0:
        mughalai.configure(state=DISABLED)
        E_mughlaipizza.set("0")
    if (var14.get() == 1):
        zingerburger.configure(state=NORMAL)
    elif var14.get() == 0:
        zingerburger.configure(state=DISABLED)
        E_zingerburger.set("0")
    if (var15.get() == 1):
        crispyb.configure(state=NORMAL)
    elif var15.get() == 0:
        crispyb.configure(state=DISABLED)
        E_cripsyburger.set("0")
    if (var16.get() == 1):
        krizmaburger.configure(state=NORMAL)
    elif var16.get() == 0:
        krizmaburger.configure(state=DISABLED)
        E_krizmaburger.set("0")
    if (var17.get() == 1):
        grillb.configure(state=NORMAL)
    elif var17.get() == 0:
        grillb.configure(state=DISABLED)
        E_Grillburger.set("0")
    if (var18.get() == 1):
        fries.configure(state=NORMAL)
    elif var18.get() == 0:
        fries.configure(state=DISABLED)
        E_friedsrl.set("0")
#=============================== Design of Cost ==============
def costofitems():
    Item1= float(E_drinksLare.get())
    Item2 = float(E_drinksSmall.get())
    Item3 = float(E_chocolate.get())
    Item4 = float(E_moltenlava.get())
    Item5 = float(E_bbqRunch.get())
    Item6 = float(E_juicemix.get())
    Item7 = float(E_gardensalad.get())
    Item8 = float(E_pickelpizza.get())
    Item9 = float(E_chickenfajita.get())
    Item10 = float(E_vegitablePizza.get())
    Item11 = float(E_chickenChapli.get())
    Item12 = float(E_pepporonipizza.get())
    Item13 = float(E_mughlaipizza.get())
    Item14= float(E_zingerburger.get())
    Item15 = float(E_cripsyburger.get())
    Item16 = float(E_krizmaburger.get())
    Item17 = float(E_Grillburger.get())
    Item18 = float(E_friedsrl.get())

    PriceofDrinks = (Item1 * 80)+ (Item2 *40 )+(Item4 * 100)+(Item6*60)
    PriceofBurgers =(Item14 *140)+(Item15 * 150)+(Item16 *180)+(Item17*220)
    PriceofPizzaz = (Item8 * 300)+(Item9 * 340)+(Item10 *250)+(Item11 * 400)+(Item12*420)+(Item13 *360)
    Priceofothers =(Item7 * 80)+(Item18 * 50)+(Item3 * 120)+(Item5 * 150)

    Drinksprices = "Rs", str('%2f' % PriceofDrinks)
    PizzaPrice = "Rs", str('%2f' % PriceofPizzaz )
    BurgerPrice = "Rs", str('%2f'% PriceofBurgers )
    OthersPrice = "Rs", str('%2f' % Priceofothers)

    Costofdrinks.set(Drinksprices)
    CostofBurger.set(BurgerPrice)
    CostofPizza.set(PizzaPrice)
    CostofOthers.set(OthersPrice)


    SC = "Rs" ,str('%2f' % (30))
    servicecharge.set(SC)

    subtotalofitems = "Rs",str('%2f' % (PriceofDrinks+PriceofBurgers+PriceofPizzaz+Priceofothers+ 30))
    subtotal.set(subtotalofitems)

    Tax= "Rs", str('%2f' % ((PriceofDrinks+PriceofBurgers+PriceofPizzaz+Priceofothers+30)*0.15))
    Paidtext.set(Tax)

    IT = ((PriceofDrinks + PriceofBurgers+PriceofPizzaz+Priceofothers+30)*0.15)
    TC = "Rs", str('%2f' % (PriceofDrinks + PriceofBurgers +PriceofPizzaz+Priceofothers+30 +IT))
    Totalcost.set(TC)
#============================== Reciept Functions ======================================
def receiptf():
    texReciept.delete("1.0",END)
    x = random.randint(10908 , 500876)
    randomref = str(x)
    RandomRef.set("Bill     "+ randomref)
    texReciept.insert(END, 'Bill\t\t\t\t\t' + randomref+"\n")
    texReciept.insert(END, 'Rciept Ref:\t\t\t'  + ReceiptRef.get()+'\t\t'+ DateofOrder.get() +"\n")
    texReciept.insert(END, 'Items\t\t\t\t\t' + "Cost of Items \n\n")
    texReciept.insert(END,  'Drinks Large \t\t\t\t\t' + E_drinksLare.get()+"\n")
    texReciept.insert(END, 'Chocolste Malte\t\t\t\t\t' + E_chocolate.get() + "\n")
    texReciept.insert(END, 'Molten Lava\t\t\t\t\t' + E_moltenlava.get() + "\n")
    texReciept.insert(END, 'Bar B.Q \t\t\t\t\t' + E_bbqRunch.get() + "\n")
    texReciept.insert(END, 'Juice Mix \t\t\t\t\t' + E_juicemix.get() + "\n")
    texReciept.insert(END, 'Garden Salad \t\t\t\t\t' + E_gardensalad.get() + "\n")
    texReciept.insert(END, 'Pickel Pizza \t\t\t\t\t' + E_pickelpizza.get() + "\n")
    texReciept.insert(END, 'Chicken Fajita \t\t\t\t\t' + E_chickenfajita.get() + "\n")
    texReciept.insert(END, 'Vegetable Pizza \t\t\t\t\t' + E_vegitablePizza.get() + "\n")
    texReciept.insert(END, 'Chicken Chapli \t\t\t\t\t' + E_chickenChapli.get() + "\n")
    texReciept.insert(END, 'Pepporoni Pizza \t\t\t\t\t' + E_pepporonipizza.get() + "\n")
    texReciept.insert(END, 'Mughlai Pizza\t\t\t\t\t' + E_mughlaipizza.get() + "\n")
    texReciept.insert(END, 'Zinger Burger \t\t\t\t\t' + E_zingerburger.get() + "\n")
    texReciept.insert(END, 'Crispy Burger \t\t\t\t\t' + E_cripsyburger.get() + "\n")
    texReciept.insert(END, 'Krizma Burger \t\t\t\t\t' + E_krizmaburger.get() + "\n")
    texReciept.insert(END, 'Grill Burger \t\t\t\t\t' + E_Grillburger.get() + "\n")
    texReciept.insert(END, 'Fries S/R/L \t\t\t\t\t' + E_friedsrl.get() + "\n")


    texReciept.insert(END , "Cost of Drinks :\t\t"+ Costofdrinks.get()+ "\tSub Total:\t\t"+ subtotal.get()+" \n")
    texReciept.insert(END , "Cost of Burgers :\t\t"+ CostofBurger.get()+ "\tSub Total:\t\t"+ subtotal.get()+" \n")
    texReciept.insert(END , "Cost of Pizza :\t\t"+ CostofPizza.get()+ "\tSub Total:\t\t"+ subtotal.get()+" \n")
    texReciept.insert(END , "Cost of Others  :\t\t"+ CostofOthers.get()+ "\tSub Total:\t\t"+ subtotal.get()+" \n")


    texReciept.insert(END , "Survice Charge  :\t\t"+ servicecharge.get()+ "\t Total Cost:\t\t"+ Totalcost.get()+" \n")

#========================== Buttons ============================
buttontotal= Button(frameRight,text="Total",bg="black",fg="white", font=('arial',16,'bold'),bd=4,relief=GROOVE, command= costofitems, width=9,height=2)
buttontotal.place(x=2,y=543)

buttontotal= Button(frameRight, text="Reciept",bg="black",fg="white", command = receiptf, font=('arial',16,'bold'),bd=4,relief=GROOVE,width=9,height=2)
buttontotal.place(x=133,y=543)

buttontotal= Button(frameRight, text="Reset",bg="black",fg="white",command=reset, font=('arial',16,'bold'),bd=4,relief=GROOVE,width=9,height=2)
buttontotal.place(x=263,y=543)

buttontotal= Button(frameRight, text="Exit",command= qExit,bg="black",fg="white", font=('arial',16,'bold'),bd=4,relief=GROOVE,width=9,height=2)
buttontotal.place(x=393,y=543)

root.mainloop()