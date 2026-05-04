# Banking System — Python OOP Project

A beginner-friendly banking system built in Python that demonstrates 
all four pillars of Object-Oriented Programming.

## Concepts Covered

- **Abstraction** — `Account` is an abstract base class that cannot be instantiated directly
- **Encapsulation** — `__balance` and `__transactions` are private, accessed only via getters
- **Inheritance** — `SavingsAccount` and `CurrentAccount` both inherit from `Account`
- **Polymorphism** — `calculate_interest()` behaves differently per account type

## Features

- Deposit and withdraw money
- Transaction history stored using NumPy
- Summary statistics — total deposited, total withdrawn, average transaction size
- Interest calculation for savings accounts

## How to Run

1. Clone the repo
2. Open in Jupyter Notebook or Google Colab
3. Run all cells
4. Test using the example below:

## Example

s = SavingsAccount("Jaydeep", 1000)
s.deposit(500)
s.withdraw(200)
s.show_balance()
s.transaction_summary()
print(f"Interest earned: {s.calculate_interest()}")

## Tech Used

- Python 3
- NumPy
- abc module (Abstract Base Classes)
