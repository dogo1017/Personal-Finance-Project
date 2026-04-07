# TE 2nd Personal Financial Calculator (True's Part)
#Import Libraries
import os

#Notes
# 1. Define the folder path and file name
#Code:
folder = "docs"
filename = "data.csv"

#Notes:
# 2. Ensure the directory exists
#if not os.path.exists(folder):
    #os.makedirs(folder)

# 3. Join the path and write the file
#full_path = os.path.join(folder, filename)
#with open(full_path, "w") as f:
    #f.write("Writing to a specific folder.")

#Code:
#Savings Goal Function
def savings_goal():
    #While True
    while True:
        #Display 1. Set new savings goal
        print("1. Set new savings goal")
        #Display 2. View savings goal
        print("2. View savings goal")
        #Display 3. Return to menu
        print("3. Return to menu")
        #savings_choice is set to an input asking the user to choose 1-3
        savings_choice = input("Choose 1-3: ")
        #If savings_choice is set to 1
        if savings_choice == "1":
            #savings_goal is set to a user float input asking them to enter a savings goal
            savings_goal = float(input("Enter a savings goal: "))
            #monthly is set to a user integer input asking them how much money they want to save per month
            monthly = float(input("How much money do you want to save per month: "))
            #length = savings_goal/monthly
            length = savings_goal/monthly
            #Display It will take you {length} months to reach your savings goal.
            print(f"It will take you {length} months to reach your savings goal.")
                #save savings_goal, monthly, and length into CSV file
            if not os.path.exists(folder):
                os.makedirs(folder)
            full_path = os.path.join(folder, filename)
            with open(full_path, "a") as f:
                f.write(f"\nSavings Goal: ${savings_goal}, Monthly Savings: ${monthly}, Time it Will Take to Reach Goal: {length} Months\n")

        #Also If savings_goal is set to 2
        elif savings_choice == "2":
            #If savings_goal == None
            if savings_goal == "":
                #Display You need to make a savings goal first
                print("You need to make a savings goal first.")
            #Else:
            else:
                #Open savings_goal from CSV file
                print("File opened (add this later).")
        #Also If savings_goal is set to 3
        elif savings_choice == "3":
                #Run menu
            print("Running Menu, add this later.")

savings_goal()

#Budget Function
    #While True
        #Display 1. Set Budget Limits & Set Expenses
        #Display 2. Compare Expenses to Purchases
        #Display 3. Return to Menu
        #budget is set to a user input asking to choose 1-3
        #IF budget is set to 1
            #budget_limit is set to a user input asking them to enter their budget limit
            #expenses is set to an input asking the user to enter their expenses
            #save budget_limit and expeneses in CSV file
        #Also If budget is set to 2
            #IF budget_limit or expenses == None
                #Display you need to set your budget limits and expenses
            #Else
                #Display expeneses and budget_limits
        #Also If
                #Run menu

