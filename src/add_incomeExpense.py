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
    
    # BUG FIX: changed open() to use mode='a' (append) so data isn't overwritten
    with open(FILE_expense, mode='a', newline='') as file:
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
                        # BUG FIX: removed unreachable 'break' after raise, added break here for valid input
                        break
                except ValueError:
                        print("Please enter 1, 2, or 3 .")
                #If user inputs an 1 then take them to
                if choice == 1:
                        # would they like to add 1.income or 2.expese or 3. Return menu
                        print("\n[1] Income")
                        print("[2] Expense")
                        print("[3] Return to menu")
                        while True:
                                try:
                                        sub_choice = int(input("Enter choice (1-3): "))
                                        if sub_choice not in range(1, 4):
                                                raise ValueError
                                        break
                                except ValueError:
                                        print("Please enter 1, 2, or 3.")
                                #If one then add income taking in date,amount and source 
                                #after add it to the csv called FILE_expense
                        if sub_choice == 1:
                                add_entry("Income")
                                #Else if two then add an expense taking in also date amount and source
                        elif sub_choice == 2:
                                add_entry("Expense")
                                #else if 3 then return them to main menu
                        elif sub_choice == 3:
                                print("Returning to menu...")
                                income_expense()
                                return
                                #else SHOW THE USER incorrect input 
                        else:
                                print("Incorrect input, please try again.")
                                #after all of this return them to the menu 
                        income_expense()
                        return
 
        #else if user inputs 2 take them to 
                elif choice == 2:
                        #asking them 1. The entire CSV 2. One Date 3. A spefic month 
                        print("\n[1] View entire CSV")
                        print("[2] View by specific date")
                        print("[3] View by specific month")
                        while True:
                                try:
                                        view_choice = int(input("Enter choice (1-3): "))
                                        if view_choice not in range(1, 4):
                                                raise ValueError
                                        break
                                except ValueError:
                                        print("Please enter 1, 2, or 3.")
                        #if they choose 1 then just print out entire csv
                        if view_choice == 1:
                                with open(FILE_expense, newline='') as file:
                                        reader = csv.DictReader(file)
                                        rows = list(reader)
                                if not rows:
                                        print("No entries found.")
                                else:
                                        print(f"\n{'Type':<10} {'Date':<12} {'Amount':<10} {'Source'}")
                                        print("-" * 45)
                                        for row in rows:
                                                print(f"{row['Type']:<10} {row['Date']:<12} {row['Amount']:<10} {row['Source']}")
                        # else if they choose two ask them which date and print all of the info for specific date
                        # make sure that the date actually exist and that they can edit it
                        elif view_choice == 2:
                                date = input("Enter date (YYYY-MM-DD): ")
                                with open(FILE_expense, newline='') as file:
                                        reader = csv.DictReader(file)
                                        rows = [row for row in reader if row['Date'] == date]
                                if not rows:
                                        print(f"No entries found for {date}.")
                                else:
                                        print(f"\n{'Type':<10} {'Date':<12} {'Amount':<10} {'Source'}")
                                        print("-" * 45)
                                        for row in rows:
                                                print(f"{row['Type']:<10} {row['Date']:<12} {row['Amount']:<10} {row['Source']}")
                        #else if they choose three then ask the user which month they want and check if month is vaild
                        elif view_choice == 3:
                                while True:
                                        month_input = input("Enter month (YYYY-MM): ")
                                        parts = month_input.split("-")
                                        #if the month is not vaild tell them
                                        #And send them back up to asking which month
                                        if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit() and 1 <= int(parts[1]) <= 12:
                                                break
                                        print("Invalid month. Please enter in YYYY-MM format (e.g. 2024-03).")
                                # if the month is vaild print the month and make sure they can edit if they so wish to do so
                                with open(FILE_expense, newline='') as file:
                                        reader = csv.DictReader(file)
                                        rows = [row for row in reader if row['Date'].startswith(month_input)]
                                if not rows:
                                        print(f"No entries found for {month_input}.")
                                else:
                                        print(f"\n{'Type':<10} {'Date':<12} {'Amount':<10} {'Source'}")
                                        print("-" * 45)
                                        for row in rows:
                                                print(f"{row['Type']:<10} {row['Date']:<12} {row['Amount']:<10} {row['Source']}")
                        income_expense()
                        return
 
        #else if inputs 3
                elif choice == 3:
                        #then return them to the main main menu and tell them thanks 
                        print("Thanks, returning to main menu!")
                        return
                #else 
                else:
                        #tell the user that the input is inncorrect and that they need to try again
                        print("Incorrect input, please try again.")
                        income_expense()
                        return
 
# Function to initialize the CSV file with headers if it doesn't exist
income_expense()