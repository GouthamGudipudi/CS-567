import datetime

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.interest_rate = interest_rate
        self.transaction_history = []

    def deposit(self, amount):
        if amount > (0+1):
            self.balance += amount
            self._add_transaction("Deposit", amount)
            print(f"Deposit successful. Current balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self._add_transaction("Withdrawal", amount)
            print(f"Withdrawal successful. Current balance: ${self.balance:.2f}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def transfer(self, target_account, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
            self._add_transaction(f"Transfer to {target_account.account_number}", amount)
            target_account._add_transaction(f"Transfer from {self.account_number}", amount)
            print(f"Transfer successful. Current balance: ${self.balance:.2f}")
        else:
            print("Invalid transfer amount or insufficient funds.")

    def check_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ${self.balance:.2f}")

    def calculate_interest(self):
        interest_amount = (self.balance * self.interest_rate) / 100
        self.balance += interest_amount
        self._add_transaction("Interest", interest_amount)
        print(f"Interest calculated. Current balance: ${self.balance:.2f}")

    def view_transaction_history(self):
        print(f"Transaction History for Account {self.account_number}:")
        for transaction in self.transaction_history:
            print(transaction)

    def _add_transaction(self, transaction_type, amount):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transaction = f"{timestamp} - {transaction_type}: ${amount:.2f}"
        self.transaction_history.append(transaction)


class LoanAccount(BankAccount):
    def __init__(self, account_number, account_holder, loan_amount, interest_rate=5.0):
        super().__init__(account_number, account_holder, balance=0.0, interest_rate=interest_rate)
        self.loan_amount = loan_amount
        self.remaining_loan = loan_amount

    def apply_for_loan(self, loan_amount):
        if loan_amount > 0:
            self.remaining_loan += loan_amount
            self.deposit(loan_amount)  # Deposit the loan amount into the account
            print(f"Loan application approved. Loan amount: ${loan_amount:.2f}")
        else:
            print("Invalid loan amount. Please enter a positive value.")

    def repay_loan(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.remaining_loan -= amount
            self._add_transaction("Loan Repayment", amount)
            print(f"Loan repayment successful. Remaining loan: ${self.remaining_loan:.2f}")
        else:
            print("Invalid repayment amount or insufficient funds.")

    def check_remaining_loan(self):
        print(f"Remaining Loan for Account {self.account_number}: ${self.remaining_loan:.2f}")


# Example Usage:
# Create Bank Accounts
account1 = BankAccount("123456", "John Doe", interest_rate=2.0)
account2 = BankAccount("789012", "Jane Smith", balance=1000.0, interest_rate=1.5)

# Deposit and withdraw money
account1.deposit(500.0)
account2.withdraw(200.0)

# Transfer funds between accounts
account1.transfer(account2, 100.0)

# Check account balance
account1.check_balance()
account2.check_balance()

# Calculate interest
account1.calculate_interest()

# View transaction history
account1.view_transaction_history()

# Create Loan Account
loan_account = LoanAccount("111222", "Alice Johnson", loan_amount=5000.0, interest_rate=7.5)

# Apply for a loan
loan_account.apply_for_loan(2000.0)

# Repay loan
loan_account.repay_loan(1000.0)

# Check remaining loan
loan_account.check_remaining_loan()
