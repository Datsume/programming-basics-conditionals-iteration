#A particular zoo determines the price of admission based on the age of the guest.   
#- Guests 2 years of age and less are admitted without charge. 
#- Children between 3 and 12 years of age cost $14.00.
#- Seniors aged 65 years and over cost $18.00. 
#- Admission for all other guests is $23.00.  

#Create a program that begins by **reading the ages of all the guests in a group from the user**, 
#with one age entered on each line.   
#The user will enter a **blank line** (a newline character) to indicate that there are no more guests in the group.    
#Then your program should display the admission cost for the group with an appropriate message.   
#The cost should be displayed using **two decimal places**.

total_price= 0.0
print("Enter the ages")
print("Enter to end the insertion")

agein= input("Enter the ages:")


while agein != "":


    ages= int(agein)

    if ages <=2:
        price= 0.00
    elif ages <=12:
        price= 14.00
    elif ages >=65:
        price= 18.00
    else:
        price= 23.00

    total_price+= price
    print(f"Total price:{total_price:.2f}")
    agein= input("Enter the ages:")