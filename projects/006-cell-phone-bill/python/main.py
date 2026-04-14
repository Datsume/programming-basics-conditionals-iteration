#A particular cell phone plan includes for € 15.00 a month: 
#- 50 minutes of air time 
#- 50 text messages    
#- Each additional minute of air time costs € 0.25
#- Each additional text messages cost € 0.15  
#- All cell phone bills include an additional charge of € 0.44 to support 911 call centers

#The entire bill (including the 911 charge) is subject to **5 percent sales tax**.  

#Write a program that **reads the number of minutes and text messages used in a month** from the user.  
#Display:
#- Base charge,
#- Extra minutes charge (if any),
#- Extra text message charge (if any),
#- 911 fee, 
#- Tax,
#- Total bill amount.   

#Only display the additional minute and text message charges if the user incurred costs in these categories. 
#Ensure that all the charges are displayed **using 2 decimal places**.

#Example:   
#Input minutes: 500  
#Input messages: 55  

#Output:  
#Base charge: 15.00€  
#Extra minutes charge: 112.50€  
#Extra messages charge: 0.75€  
#911 fee: 0.44€  
#Tax: 6.43€  
#Total bill amount: 135.12€

messages= int(input("Messages used in a month: "))
minutes= int(input("Minutes used in a month: ")) 
base_charge= 15.00
extra_mes=messages-50
extra_min=minutes-50
extra_minutes_charge= extra_min *0.25
extra_messages_charge= extra_mes *0.15
fee_911= 0.44 
tax= (base_charge+max(0,extra_messages_charge)+max(0,extra_minutes_charge)+fee_911)*5/100  
total_bill_amount= base_charge+max(0,extra_messages_charge)+max(0,extra_minutes_charge)+fee_911+tax

print("Base charge:",f"{base_charge:.2f}","€")

if extra_mes>0:
   print("Extra messages charge:",f"{extra_messages_charge:.2f}","€")
else:
    print("Extra messages: 0 €")

if extra_min>0:
    print("Extra minutes charge:",f"{extra_minutes_charge:.2f}","€")
else:
    print("Extra minutes: 0 €")

print("911 fee:",fee_911,"€")
print("Tax:",f"{tax:.2f}","€")
print("Total bill amount:",f"{total_bill_amount:.2f}","€")

