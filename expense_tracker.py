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
    while True:
        category = input("Enter category: ").strip()

        if category:
            break

        print("❌ Category cannot be empty.")

    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("❌ Amount must be greater than 0.")
                continue

            break

        except ValueError:
            print("❌ Please enter a valid amount.")

    while True:
        description = input("Enter description: ").strip()

        if description:
            break

        print("❌ Description cannot be empty.")

    expense = {
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(expense)
    save_expenses()

    print("✅ Expense added successfully!")


def view_expenses():

    if not expenses:
        print("No expenses recorded.")
        return
    
    print("=== All Expenses ===")

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['category']} | ₹{expense['amount']} | {expense['description']}")


def search_expense():
    if not expenses:
        print("No expenses recorded.")
        return

    category = input("Enter category to search: ").strip().lower()

    if not category:
        print("❌ Category cannot be empty.")
        return

    found = False

    print(f"\n=== Search Results for '{category}' ===")

    for expense in expenses:
        if expense["category"].lower() == category:
            print(
                f"{expense['category']} | "
                f"₹{expense['amount']:.2f} | "
                f"{expense['description']}"
            )
            found = True

    if not found:
        print("❌ No matching expenses found.")

def delete_expense():
    view_expenses()

    if not expenses:
        return

    try:
        choice = int(input("Enter expense number to delete: "))

        if 1 <= choice <= len(expenses):
            deleted = expenses.pop(choice - 1)
            save_expenses()

            print(
                f"✅ Deleted expense: "
                f"{deleted['category']} | ₹{deleted['amount']} | "
                f"{deleted['description']}"
            )
        else:
            print("❌ Invalid expense number.")

    except ValueError:
        print("❌ Please enter a valid number.")

def show_summary():
    if not expenses:
        print("No expenses recorded.")
        return

    total_amount = sum(expense["amount"] for expense in expenses)

    print("\n=== Expense Summary ===")
    print(f"Total Expenses: {len(expenses)}")
    print(f"Total Amount  : ₹{total_amount:.2f}")

def show_menu():
    load_expenses()

    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expense")
        print("4. Delete Expense")
        print("5. Show Summary")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            search_expense()

        elif choice == "4":
            delete_expense()

        elif choice == "5":
            show_summary()

        elif choice == "6":
            print("Goodbye! 👋")
            break

        else:
            print("❌ Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    show_menu()
