from expense_tracker import *

class CLI:
    @staticmethod
    def display_menu():
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Edit Expense")
        print("4. Delete Expense")
        print("5. Filter by Category")
        print("6. Exit")

    @staticmethod
    def run():
        while True:
            CLI.display_menu()
            choice = input("\nChoose an option: ")
            if choice == "1":
                CLI.add_expense()
            elif choice == "2":
                CLI.view_expenses()
            elif choice == "3":
                CLI.edit_expense()
            elif choice == "4":
                CLI.delete_expense()
            elif choice == "5":
                CLI.filter_expenses()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    @staticmethod
    def add_expense():
        date = input("Enter date (DD/MM/YYYY): ")
        description = input("Enter description: ").strip()
        amount = float(input("Enter amount: ").strip())
        category = input("Enter category: ").title().strip()
        new_record = Record(date, description, amount, category)
        Storage.store(new_record.details())
        print("Expense added successfully!")

    @staticmethod
    def view_expenses():
        print("\nAll Expenses:")
        Report.display()

    @staticmethod
    def edit_expense():
        CLI.view_expenses()
        index = int(input("Enter the index of the record to edit: "))
        date = input("Enter new date (DD/MM/YYYY): ")
        description = input("Enter new description: ")
        amount = float(input("Enter new amount: "))
        category = input("Enter new category: ").title()
        new_record = {"date": date, "description": description, "amount": amount, "category": category}
        Edit.modify_record(index, new_record)

    @staticmethod
    def delete_expense():
        CLI.view_expenses()
        index = int(input("Enter the index of the record to delete: "))
        Edit.delete_record(index)

    @staticmethod
    def filter_expenses():
        category = input("Enter category to filter: ").title()
        Retrieval.display_filtered(category)

if __name__=="__main__":
    CLI.run()