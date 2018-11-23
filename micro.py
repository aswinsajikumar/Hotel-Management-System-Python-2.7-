#python 2.7
# -*- coding: utf-8 -*-
import sys
print sys.getdefaultencoding()
import random
class hotelfarecal:

    def __init__(self,rt='',s=0,p=0,r=0,t=0,a=1800,name='',address='',cindate='',coutdate='',rno=random.randint(101,115)):

        print ("*****WELCOME TO AªG HOTELS*****")

        self.rt=rt

        self.r=r

        self.t=t

        self.p=p

        self.s=s
        self.a=a
        self.name=name
        self.address=address
        self.cindate=cindate
        self.coutdate=coutdate
        self.rno=rno
    def inputdata(self):
        self.name=raw_input("Enter your name:")
        self.address=raw_input("Enter your address:")
        self.cindate=raw_input("Enter your check in date:")
        self.coutdate=raw_input("Enter your checkout date:")
        print '\n'
        
    def roomrent(self):

        print "We have the following rooms for you:-"

        print "1.  Without AC---->rs 1000 PN\-"

        print "2.  Family---->rs 1500 PN\-"

        print "3.  Deluxe---->rs 2500 PN\-"

        print "4.  Suite---->rs 4000 PN\-"

        x=input("Enter Your Choice Please->")

        n=input("For How Many Nights Did You Stay:")

        if(x==1):

            print "you have opted room Without AC"

            self.s=1000*n

        elif (x==2):

            print "you have opted room Family"

            self.s=1500*n

        elif (x==3):

            print "you have opted room Deluxe"

            self.s=2500*n

        elif (x==4):
            print "you have opted room Suite"

            self.s=4000*n

        else:

            print ("please choose a room")
	print "Your room no.:",self.rno,"\n"
        print "Your room rent is =",self.s,"\n"

    def restaurentbill(self):

        print("*****RESTAURANT MENU*****")

        print "1.water----->Rs20",'\n',"2.tea----->Rs10",'\n',"3.breakfast combo--->Rs90",'\n',"4.lunch---->Rs110",'\n',"5.dinner--->Rs150",'\n',"6.Exit"


        while (1):

            c=input("Enter your choice:")


            if (c==1):
                d=input("Enter the quantity:")
                self.r=self.r+20*d

            elif (c==2):
                 d=input("Enter the quantity:")
                 self.r=self.r+10*d

            elif (c==3):
                 d=input("Enter the quantity:")
                 self.r=self.r+90*d

            elif (c==4):
                 d=input("Enter the quantity:")
                 self.r=self.r+110*d

            elif (c==5):
                 d=input("Enter the quantity:")
                 self.r=self.r+150*d

            elif (c==6):
                break;
            else:
                print("Invalid option")

        print "Total food Cost=Rs",self.r,"\n"

    def	laundrybill(self):
        print ("******LAUNDRY MENU*******")

        print "1.Shorts----->Rs3",'\n',"2.Trousers----->Rs4",'\n',"3.Shirt--->Rs5",'\n',"4.Jeans---->Rs6",'\n',"5.Girlsuit--->Rs8",'\n',"6.Exit"

        while (1):

            e=input("Enter your choice:")

            if (e==1):
                f=input("Enter the quantity:")
                self.t=self.t+3*f

            elif (e==2):
                f=input("Enter the quantity:")
                self.t=self.t+4*f

            elif (e==3):
                f=input("Enter the quantity:")
                self.t=self.t+5*f

            elif (e==4):
                f=input("Enter the quantity:")
                self.t=self.t+6*f

            elif (e==5):
                f=input("Enter the quantity:")
                self.t=self.t+8*f
            elif (e==6):
                break;
            else:

                print ("Invalid option")


        print "Total Laundary Cost=Rs",self.t,"\n"

    def gamebill(self):
        print ("******GAME MENU*******")

        print "1.Table tennis----->Rs60",'\n',"2.Bowling----->Rs80",'\n',"3.Snooker--->Rs70",'\n',"4.Video games---->Rs90",'\n',"5.Pool--->Rs50",'\n',"6.Exit"



        while (1):

            
            g=input("Enter your choice:")


            if (g==1):
                h=input("No. of hours:")
                self.p=self.p+60*h

            elif (g==2):
                h=input("No. of hours:")
                self.p=self.p+80*h

            elif (g==3):
                h=input("No. of hours:")
                self.p=self.p+70*h

            elif (g==4):
                h=input("No. of hours:")
                self.p=self.p+90*h

            elif (g==5):
                h=input("No. of hours:")
                self.p=self.p+50*h
            elif (g==6):
                break;

            else:

                print ("Invalid option")



        print "Total Game Bill=Rs",self.p,"\n"

    def display(self):
        print ("******HOTEL BILL******")
        print "Customer details:"
        print "Customer name:",self.name
        print "Customer address:",self.address
        print "Check in date:",self.cindate
        print "Check out date",self.coutdate
        print "Room no.",self.rno
        print "Your Room rent is:",self.s
        print "Your Food bill is:",self.r
        print "Your laundary bill is:",self.t
        print "Your Game bill is:",self.p

        self.rt=self.s+self.t+self.p+self.r

        print "Your sub total bill is:",self.rt
        print "Additional Service Charges is",self.a
        print "Your grandtotal bill is:",self.rt+self.a,"\n"
        self.rno+=1

            

        

        

def main():

    a=hotelfarecal()
    

    while (1):
        print("1.Enter Customer Data")
        
        print("2.Calculate room rent")

        print("3.Calculate restaurant bill")

        print("4.Calculate laundry bill")

        print("5.Calculate game bill")

        print("6.Show total cost")

        print("7.EXIT")

        b=input("enter your choice:")
        if (b==1):
            a.inputdata()

        if (b==2):

            a.roomrent()

        if (b==3):

            a.restaurentbill()

        if (b==4):

            a.laundrybill()

        if (b==5):

            a.gamebill()

        if (b==6):

            a.display()

        if (b==7):

            quit()
main()


