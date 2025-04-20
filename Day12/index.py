
transaction_count = 0

def add_expense(expenses: list[float], amount: float) -> None:
    global transaction_count
    expenses.append(amount)
    transaction_count += 1

def total_expense(expenses: list[float]) -> float:
    return sum(expenses)

def highest_expense(expenses: list[float]) -> float:
    return max(expenses) if expenses else 0.0

def average_expense(expenses: list[float]) -> float:
    return sum(expenses) / len(expenses) if expenses else 0.0

def expense_summary(expenses: list[float]) -> dict[str, float]:
    return {
        'total': total_expense(expenses),
        'highest': highest_expense(expenses),
        'average': average_expense(expenses),
        'transactions': transaction_count
    }
def generate_report(expenses: list[float]) -> None:
    summary = expense_summary(expenses)
    print(summary)
expenses = []
add_expense(expenses, 50.0)
add_expense(expenses, 75.5)
add_expense(expenses, 20.25)
generate_report(expenses)