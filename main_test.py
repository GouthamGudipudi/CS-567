import unittest

from main import BankAccount, LoanAccount


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account1 = BankAccount("123456", "John Doe", interest_rate=2.0)
        self.account2 = BankAccount("789012", "Jane Smith", balance=1000.0, interest_rate=1.5)

    def test_deposit(self):
        self.account1.deposit(500.0)
        self.assertEqual(self.account1.balance, 500.0)

    def test_withdraw(self):
        self.account2.withdraw(200.0)
        self.assertEqual(self.account2.balance, 800.0)

    def test_transfer(self):
        self.account1.transfer(self.account2, 100.0)
        self.assertEqual(self.account1.balance, 400.0)
        self.assertEqual(self.account2.balance, 900.0)

    def test_check_balance(self):
        self.assertEqual(self.account1.check_balance(), "Account Number: 123456\nAccount Holder: John Doe\nCurrent Balance: $0.00")

    def test_calculate_interest(self):
        self.account1.calculate_interest()
        self.assertEqual(self.account1.balance, 0.0)


class TestLoanAccount(unittest.TestCase):
    def setUp(self):
        self.loan_account = LoanAccount("111222", "Alice Johnson", loan_amount=5000.0, interest_rate=7.5)

    def test_apply_for_loan(self):
        self.loan_account.apply_for_loan(2000.0)
        self.assertEqual(self.loan_account.balance, 2000.0)
        self.assertEqual(self.loan_account.remaining_loan, 7000.0)

    def test_repay_loan(self):
        self.loan_account.apply_for_loan(2000.0)
        self.loan_account.repay_loan(1000.0)
        self.assertEqual(self.loan_account.balance, 1000.0)
        self.assertEqual(self.loan_account.remaining_loan, 6000.0)

    def test_check_remaining_loan(self):
        self.assertEqual(self.loan_account.check_remaining_loan(), "Remaining Loan for Account 111222: $5000.00")


if __name__ == '__main__':
    unittest.main()
