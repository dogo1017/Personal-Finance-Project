# TE 2nd Personal Financial Calculator (True's Part)
#Import Libraries
import os
#Savings Goal Function
def savings_goal():

    #While True
    while True:
        #Display 1. Set new savings goal
        print("\n1. Set new savings goal")
        #Display 2. View savings goal
        print("2. View savings goal")
        #Display 3. Return to menu
        print("3. Return to menu")
        #savings_choice is set to an input asking the user to choose 1-3
        savings_choice = input("Choose 1-3: ")
        #If savings_choice is set to 1
        if savings_choice == "1":
            #savings_goal is set to a user float input asking them to enter a savings goal
            savings_amount = float(input("Enter a savings goal: "))
            #monthly is set to a user integer input asking them how much money they want to save per month
            monthly = float(input("How much money do you want to save per month: "))
            #length = savings_goal/monthly
            length = savings_amount/monthly
            #Display It will take you {length} months to reach your savings goal.
            print(f"It will take you {length:.2f} months to reach your savings goal.")
                #save savings_goal, monthly, and length into CSV file
                #Save data to CSV file
            with open("docs\\data.csv", "a") as f:
                f.write(f"\n{savings_amount}, {monthly}, {length}\n")
            
        #Also If savings_goal is set to 2
        elif savings_choice == "2":
            with open("docs\\data.csv", "r") as f:
                    try:
                    # Try to open savings_goal from CSV file
                        print("\n--- Saved Goals ---")
                        print(f.read())
                    except:
                        #Except to information
                        print("No savings goal made yet.")
                
                
        #Also If savings_goal is set to 3
        elif savings_choice == "3":
                #Run menu
            print("Running Menu, add this later.")
            break
        
        else:
            print("Invalid choice. Try again.")



#Budget Function
def budget():
    #While True
    while True:
        #Display 1. Set Budget Limits & Set Expenses
        print("\n1. Set Budget Limits & Expenses")
        #Display 2. Compare Expenses to Purchases
        print("2. Compare Expenses to Budget")
        #Display 3. Return to Menu
        print("3. Return to Menu")
        #budget is set to a user input asking to choose 1-3
        budget_choice = input("Choose 1-3: ")
        #IF budget is set to 1
        if budget_choice == "1":
             # Get inputs
            budget_limit = float(input("Enter your budget limit: "))
            expenses = float(input("Enter your expenses: "))
            #Save to CSV
            with open("docs\\budget.csv", "a") as f:
                f.write(f"\n{budget_limit}, {expenses}\n")

            print("Budget saved.")
        #Also If budget is set to 2
        elif budget_choice == "2":
            with open("docs\\budget.csv", "r") as f:
                    try:
                    # Try to open savings_goal from CSV file
                        print(f.read())
                    except:
                        #Except to information
                        print("No budget made yet.")


        #Also If budegt is set to 3
        elif budget_choice == "3":
            print("Returning to menu.")
            break

        else:
            print("Invalid choice. Try again.")