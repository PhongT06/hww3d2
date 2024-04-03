class BudgetCategory:
    # Constructor and private attributes
    def __init__(self, category, budget):
        self.__category = category
        self.__budget = budget

    # Getters and setters for category name and budget
    def get_category(self):
        return self.__category
    def set_category(self, category):
        self.__category = category
    def get_budget(self):
        return self.__budget
    def set_budget(self):
        if budget >= 0:
            self.__budget = budget
        else:
            print("Must have some money to budget!")

    def add_expense(self, amount):
        # Method to add an expense to the category
        if amount > 0:
            if amount <= self.__budget:
                self.__budget -= amount
                print(f"${amount} expense added to {self.__category} category.")
            else:
                print(f"Can't add ${amount} expense to the budget. You need to earn more money or save for a higher budget!")
        else:
            print("You need more money in order to budget!")
    
    def display_category_summary(self):
        # Method to display the budget category details
        print(f"Category: {self.__category}")
        print(f"Budget: ${self.__budget}")

# Example usage
food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()
entertainment_category = BudgetCategory("Video games", 500)
entertainment_category.add_expense(450)
entertainment_category.display_category_summary()
vacation_category = BudgetCategory("Vacation", 500)
vacation_category.add_expense(1200)
vacation_category.display_category_summary()