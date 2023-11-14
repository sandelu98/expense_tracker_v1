# Sandelus98's Expense Tracker v. 1.0

## Recent added:
Added programfiles to the repository. This includes the files:

- expense.py
- expense_tracker.py
- expense.cpython-312.pyc

## Description:

When running the program as intended it will:

1. The program will ask for a name of your expense, input the name and press "ENTER" to proceed. (if you input wrong requirements, there will be a error message that will make you try another input). Your input will then be saved into the file "expenses.csv".

2. When you've hit "ENTER" the program will proceed and will ask you for the cost of the expense, input the cost and hit "ENTER" to proceed further (wrong input will make the program will send a error message and will ask for you to try again). Your input will then be saved into the file "expenses.csv".

3. When you proceed from the cost, you will see a list of 5 (1-5) different categories. The program will ask you to choose a category to put your expense in. (wrong input = error). Your input will then be saved into the file "expenses.csv".

4. The program will now do calculations based on your input to give out information about:
           
           - User's total spent per. category (based of the sums of expenses divided by the different categories)
           - User's total spendings (based of x.amount in the expenses.csv file)
           - User's remaining budget (based of the budget - total_spent)
           - User's daily budget (based of how many days are left in the month)

5. If you want to highlight some of these outputs in the color green, i've made a "color green" function as used in printing my daily budget (line 99).

Note that the documentation + some of the variables are written in Norwegian. 
I might add documentation in english at a later point of time.
Hopefully this will help you navigate and understand the program better.

### - Sandelu98


