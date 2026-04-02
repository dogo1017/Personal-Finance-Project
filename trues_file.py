# TE 2nd Personal Financial Calculator (True's Part)
#Import Libraries


#Savings Goal Function
def savings_goal():
    #While True
        #Display 1. Set new savings goal
        #Display 2. View savings goal
        #Display 3. Return to menu
        #savings_choice is set to an input asking the user to choose 1-3
        savings_choice = input("Choose 1-3: ")
        #If savings_choice is set to 1
        if savings_choice == "1":
            #savings_goal is set to a user float input asking them to enter a savings goal
            savings_goal = float(input("Enter a savings goal: "))
            #monthly is set to a user integer input asking them how much money they want to save per month
            monthly = int(input("How much money do you want to save per month: "))
            #length = savings_goal/monthly
            #Display It will take you {length} months to reach your savings goal.
                #save savings_goal, monthly, and length into CSV file
            with open("docs\\data.csv", "a") as file:
                file.write(content)
        #Also If savings_goal is set to 2
        elif savings_goal == "2":
            #If savings_goal == None
                #Display You need to make a savings goal first
            #Else:
            else:
                #Open savings_goal from CSV file
                print("File opened (add this later).")
        #Also If savings_goal is set to 3
        elif savings_goal == "3":
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

