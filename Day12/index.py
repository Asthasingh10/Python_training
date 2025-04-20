# Global variable to track the number of transactions
transaction_count = 0

def add_expense(expenses: list[float], amount: float) -> None:
    """Adds a new expense and increments the transaction count."""
    global transaction_count
    expenses.append(amount)
    transaction_count += 1

def total_expense(expenses: list[float]) -> float:
    """Calculates the total of all expenses."""
    return sum(expenses)

def highest_expense(expenses: list[float]) -> float:
    """Finds the highest expense."""
    return max(expenses) if expenses else 0.0

def average_expense(expenses: list[float]) -> float:
    """Calculates the average expense."""
    return sum(expenses) / len(expenses) if expenses else 0.0

def expense_summary(expenses: list[float]) -> dict[str, float]:
    """Returns a summary of expenses."""
    return {
        'total': total_expense(expenses),
        'highest': highest_expense(expenses),
        'average': average_expense(expenses),
        'transactions': transaction_count
    }

def print_report(expenses: list[float]) -> None:
    summary = expense_summary(expenses)
    print("Expense Report")
    print("--------------")
    print(f"Total Expenses   : ₹{summary['total']:.2f}")
    print(f"Highest Expense  : ₹{summary['highest']:.2f}")
    print(f"Average Expense  : ₹{summary['average']:.2f}")
    print(f"Transactions Made: {summary['transactions']}")
expenses = []
add_expense(expenses, 250.0)
add_expense(expenses, 125.5)
add_expense(expenses, 320.75)

summary = expense_summary(expenses)
print("Returned Summary:", summary)

print_report(expenses)
