# TE 2nd Personal Financial Calculator (True's Part)
#Import Libraries


#Savings Goal Function
def savings_goal():
    #While True
    while True:
        #Print 1. Set new savings goal
        print("[1] Set New Savings Goal")
        #Print 2. View savings goal
        print("[2] View Savings Goal")
        #Print 3. Return to menu
        print("[3] Return to menu")
        #savings_choice is set to an input asking the user to choose 1-3
        savings_choice = input("Choose 1-3: ")
        #If savings_choice is set to 1
        if savings_choice == "1":
            #savings_goal is set to a user float input asking them to enter a savings goal
            savings_goal = float(input("Enter a savings goal: "))
            #monthly is set to a user integer input asking them how much money they want to save per month
            monthly = int(input("How much money do you want to save per month: "))
            #length = savings_goal/monthly
            length = savings_goal/monthly
            #Print It will take you {length} months to reach your savings goal.
            content = print(f"\nYour savings goal is {savings_goal}.\nYou want to save {monthly} per month.\nIt will take you {length} months to reach your savings goal.\n")
            print(content)
                #save savings_goal, monthly, and length into CSV file
            with open("docs\\data.csv", "a") as file:
                file.write(content)
        #Also If savings_goal is set to 2
        elif savings_goal == "2":
            #If savings_goal == None
            if savings_goal == None:
                #Print You need to make a savings goal first
                print("You need to make a savings goal first.")
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
        #Print 1. Set Budget Limits & Set Expenses
        #Print 2. Compare Expenses to Purchases
        #Print 3. Return to Menu
        #budget is set to a user input asking to choose 1-3
        #IF budget is set to 1
            #budget_limit is set to a user input asking them to enter their budget limit
            #expenses is set to an input asking the user to enter their expenses
            #save budget_limit and expeneses in CSV file
        #Also If budget is set to 2
            #IF budget_limit or expenses == None
                #Print you need to set your budget limits and expenses
            #Else
                #Print expeneses and budget_limits
        #Also If
                #Run menu

