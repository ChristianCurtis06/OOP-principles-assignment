# Task 1: Define Budget Category Class
class BudgetCategory:
    def __init__(self, name, budget):
        self.__name = name
        self.__budget = budget
        self.__total_budget = budget

# Task 2: Implement Getters and Setters
    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_budget(self):
        return self.__budget

    def set_budget(self, new_budget):
        if new_budget >= 0:
            self.__budget = new_budget
        else:
            print("Invalid budget amount. Please enter a positive total.")
    
    def get_total_budget(self):
        return self.__total_budget

# Task 3: Add Budget Functionality
    def add_expense(self, expense):
        if expense <= self.__budget:
            self.__budget -= expense
            print("Expense added to budget category.")
        else:
            print("Invalid expense amount. Please ensure expense does not exceed budget total.")

# Task 4: Display Budget Details
    def display_category_summary(self):
        print(f"Category Name: {self.get_name()}, Allotted Budget Amount: ${self.get_total_budget()}, Remaining Budget Amount: ${self.get_budget()}")

# Defining a function to create a category and add it to the 'categories' list
def create_category(categories, name, budget):
    found = False
    for category in categories:
        if category.get_name() == name:
            found = True
            break
    
    if not found:
        category = BudgetCategory(name, budget)
        categories.append(category)
        print(f"Budget category '{name}' added.")
    else:
        print(f"Budget category '{name}' already exists.")

# Creating the 'categories' list to store budget categories
categories = [BudgetCategory("Food", 80), BudgetCategory("Entertainment", 50), BudgetCategory("Utilities", 200)]

# Creating the main user interface for the 'Personal Budget Management System' using input functions and conditionals
print("Personal Budget Management System")
while True:
    print("\n1. Create budget category\n2. Add expense to budget category\n3. Display budget category summaries\n4. Exit")
    user_input = input("Enter your choice: ")
    if user_input == "1":
        name_input = input("Enter name of budget category name: ").title()
        budget_input = float(input("Enter allotted amount for budget category: $"))
        create_category(categories, name_input, budget_input)
    elif user_input == "2":
        name_input = input("Enter name of budget category name: ").title()
        found = False
        for category in categories:
            if category.get_name() == name_input:
                found = True
                expense_input = float(input("Enter expense amount: $"))
                category.add_expense(expense_input)
                break

        if not found:
            print(f"Budget category '{name_input}' not found. Please try again.")
    elif user_input == "3":
        for category in categories:
            category.display_category_summary()
    elif user_input == "4":
        print("Exiting the system...")
        break
    else:
        print("Invalid input. Please try again.")