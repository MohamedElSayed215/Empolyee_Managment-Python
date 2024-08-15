from DataList import *
BonusPercentage=0.5
DiscountPercentage=0.1
def DisplayInformation(Specific_ID):
        temp=1
        global Data      
        if Specific_ID <=len(Data) :
                print("Included !")
                for key,value in (Data[Specific_ID].items()):
                    if (temp <=5 ):
                        temp+=1
                        print("{} : {}".format(key,value))
                    else: 
                          break
        else :
                print("Not Included !") 
def GetBonus(Specific_ID):
      global Data 
      if Specific_ID < len(Data):
            print("The Bonus : " ,Data[Specific_ID]["Salary"]*BonusPercentage,"$" )
      else:
            print("Not Included !")       
def GetDiscount(Specific_ID):
      if Specific_ID < len(Data):
            print("The Discount : " ,Data[Specific_ID]["Salary"]*DiscountPercentage,"$" )
      else:
            print("Not Included !")        
def GetHolidays(Specific_ID):
      if Specific_ID < len(Data):
            print("The Legal Holidays : " ,Data[Specific_ID]["Legal Holidays"] )
      else:
            print("Not Included !")                                 