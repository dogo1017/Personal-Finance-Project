#IC 1st income and expense 
#remember to import csv and os
import csv 
import os

#define the file name for expense and income 
FILE_income = "finance_data.csv"
FILE_expense = "expense_data.csv"


#Function to initialize the CSV file with headers if it doesn't exist
def initialize_file():
    if not os.path.exists(FILE_expense):
        with open(FILE_expense, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Type", "Date", "Amount", "Source"])

# Function to add entry (Income or Expense)
def add_entry(entry_type):
    date = input("Enter date (YYYY-MM-DD): ")
    amount = input("Enter amount: ")
    source = input("Enter source: ")
    
    with open(FILE_expense, newline='') as file:
        writer = csv.writer(file)
        writer.writerow([entry_type, date, amount, source])
    print(f"{entry_type} added successfully!")


# all of this gets defined into a function called income and expense 
#asking user if they want to 1.d income/expense or 2. view total or 3 return to menu
def income_expense():
        initialize_file()
        print("Expense or income")
        print("[1] add income/expense ")
        print("[2] View total ")
        print("[3] return to menu")
#Trying to see if they brought in the correct input and if not kick them out of it
        while True:
                try:
                        #givingg the user opuions 
                        choice = int(input("Enter shape type (1-3): "))
                        #If the number they chouice not in range then raise error 
                        if choice not in range(1, 4):
                                raise ValueError
                                break
                except ValueError:
                        print("Please enter 1, 2, or 3 .")
                #If user inputs an 1 then take them to
                if choice == 1: 
                        add_entry()
              
                        # would they like to add 1.income or 2.expese or 3. Return menu
                             #If one then add income taking in date,amount and source 
                                #after add it to the csv called ......(idk the name yet)
                                #Else if two then add an expense taking in also date amount and source
                                #else if 3 then return them to main menu
                                #else SHOW THE USER incorrect input 
                                #after all of this return them to the menu 
        #else if user inputs 2 take them to 
                        #asking them 1. The entire CSV 2. One Date 3. A spefic month 
                        #if they choose 1 then just print out entire csv in reader mode and writer mode 
                        # else if they choose two ask them which date and print all of the info for specific date and 
                        #make sure that the date actually exist and that they can edit it
                        #else if they choose three then ask the user which month they want and check if month is vaild
                                #if the month is not vaild tell them
                                #And send them back up to asking which month
                                # if the month is vaild print the month and make sure they can edit if they so wish to do so
        #else if inputs 3
                        #then return them to the main main menu and tell them thanks 
                #else 
                        #tell the user that the input is inncorrect and that they need to try again




# Function to initialize the CSV file with headers if it doesn't exist


income_expense()
      


