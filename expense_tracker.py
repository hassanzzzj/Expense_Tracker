import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        try:
            with open('expenses.json', 'r') as file:
                self.expenses = json.load(file)
        except FileNotFoundError:
            self.expenses = []

    def save_expenses(self):
        with open('expenses.json', 'w') as file:
            json.dump(self.expenses, file)

    def add_expense(self, amount, category, description=""):
        expense = {
            'amount': amount,
            'category': category,
            'description': description,
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.expenses.append(expense)
        self.save_expenses()
        print(f"Added expense: {expense}")

    def generate_report(self):
        report = {}
        for expense in self.expenses:
            category = expense['category']
            if category not in report:
                report[category] = 0
            report[category] += expense['amount']

        print("\nExpense Summary Report:")
        for category, total in report.items():
            print(f"{category}: ${total:.2f}")

    def show_expenses(self):
        print("\nAll Expenses:")
        for expense in self.expenses:
            print(f"{expense['date']} - {expense['category']}: ${expense['amount']:.2f} ({expense['description']})")

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. Show All Expenses")
        print("3. Generate Summary Report")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description (optional): ")
            tracker.add_expense(amount, category, description)
        
        elif choice == '2':
            tracker.show_expenses()
        
        elif choice == '3':
            tracker.generate_report()
        
        elif choice == '4':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()