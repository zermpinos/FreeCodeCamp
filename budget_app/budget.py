class Category:
    # Initialize a Category object.
    def __init__(self, name):
        self.name = name
        self.records = []

    # Generates a string representation of the category and returns formatted string with the category name,
    # a list of items in the records, and the total balance of the category.
    def __str__(self):
        # Create a 30 character wide * line
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.records:
            """
            I use [:23]:23 because I need to display the first 23 characters
            and the 7.2f for two decimals, maximum of 7 characters.
            """
            items += f"{item['description'][:23]:23}" + f"{item['amount']:>7.2f}\n"
            total += item['amount']
        output = title + items + "Total: " + str(total)
        return output

    # Add a deposit transaction to the category records.
    def deposit(self, amount, description=""):
        self.records.append({"amount": amount, "description": description})

    # Add withdrawal transaction to the records, if funds are sufficient. True if successful, False otherwise.
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.records.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    # Calculates the current balance of the category and returns the current balance of the category.
    def get_balance(self):
        balance = 0
        for item in self.records:
            balance += item['amount']
        return balance

    # Transfer funds from this category to another, if funds are sufficient. True if successful, False otherwise.
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    # Check if there are sufficient funds in the category for a transaction. True if successful, False otherwise.
    def check_funds(self, amount):
        return amount <= self.get_balance()


# Create the asked chart
def create_spend_chart(categories):
    total_spent = 0
    category_spent = []
    # Append how much you have spent
    for category in categories:
        spent = 0
        for item in category.records:
            if item['amount'] < 0:
                spent += abs(item['amount'])
        total_spent += spent
        category_spent.append(spent)

    # Calculate the percentages of each category and round the result to the nearest int
    percentages = []
    for spent in category_spent:
        # Example of the following is 46.4% by the first multiplication will become 464 and round it becomes 470
        # The second multiplication will give us 4700 which can be displayed on the chart
        percentage = int(spent / total_spent * 10) * 10
        percentages.append(percentage)

    output = "Percentage spent by category\n"

    # Create the body of the chart. The i:3 part is because we have 3 categories
    for i in range(100, -10, -10):
        output += f"{i:3}| "
        for percentage in percentages:
            if percentage >= i:
                output += "o  "
            else:
                output += "   "
        output += "\n"
    output += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Create the labels on the bottom of the chart
    max_len = max([len(category.name) for category in categories])
    for i in range(max_len):
        output += "     "
        for category in categories:
            if i < len(category.name):
                output += f"{category.name[i]}  "
            else:
                output += "   "
        output += "\n"

    # Use slicing to remove the final newline character from the output.The last line of the chart doesn't need it,
    # since it is the end of the string.
    return output[:-1]
