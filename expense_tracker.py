import json

expenses = []


def load_expenses():
    global expenses

    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)

    except FileNotFoundError:
        expenses = []


def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense():
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    expense = {
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(expense)
    save_expenses()

    print("Expense added successfully!")


def view_expenses():

    if not expenses:
        print("No expenses recorded.")
        return
    
    print("=== All Expenses ===")

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['category']} | ₹{expense['amount']} | {expense['description']}")


def search_expense():

    category = input("Enter category to search: ").strip().lower()

    found = False

    for expense in expenses:

        if expense['category'].lower() == category:
            print(f"{expense['category']} | ₹{expense['amount']} | {expense['description']}")
            found = True

    if not found:
        print("no matching expenses found.")


def delete_expense():

    view_expenses()

    if not expenses:
        return
    
    try:
        choice = int(input("Enter expense number to delete:"))

        del expenses[choice - 1]

        save_expenses()

    except (ValueError, IndexError):
        print("Invalid expense number.")

def show_menu():

    load_expenses()

    while True:

        print("=== Expence Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expense")
        print("4. Save Expenses")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()
        
        elif choice == "3":
            search_expense()

        elif choice == "4":
            save_expenses()

        elif choice == "5":
            delete_expense()

        elif choice == "6":
            print("Good Bye!")
            break

        else:
            print("inavalid choice. Please try again.")

if __name__ == "__main__":
    show_menu()