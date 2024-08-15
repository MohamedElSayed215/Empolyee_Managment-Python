#!/usr/bin/python3
from Options import *
from time import *
Input_ID=int(input("Enter your ID : "))
Password=1234
tem=0 ; end = 0
while(tem<3):
    if end == 1 : 
        break
    GivenPassword=int(input("Enter the Password ! :"))
    if (Password==GivenPassword):
        while(True):
            Choice=int(input("1.Display your Information\n2.Get your Bonus\n3.Get your Discount\n4.Get your Holidays\n5.Exit\n"))
            if(Choice==1):
                print("=========================")
                DisplayInformation(Input_ID)  
                print("=========================")
                sleep(3)     
            elif(Choice==2):
                print("=========================")
                GetBonus(Input_ID)
                print("=========================")
                sleep(3)     
            elif(Choice==3):
                print("=========================")
                GetDiscount(Input_ID)
                print("=========================")
                sleep(3)     
            elif(Choice==4):
                print("=========================")
                GetHolidays(Input_ID)
                print("=========================")
                sleep(3)     
            elif (Choice == 5) :
                print("=========================")
                print("Thanks alot for your usage ! \nGoodBye !")
                print("=========================")
                sleep(3)     
                end+=1 
                break
    else :
        print("WRONG !")
        tem+=1

else:
    print("Restart the Program ! ")    