
import sqlite3
import numpy as np

# Database setup function to store data permanently
def init_db():
    conn = sqlite3.connect('bank_data.db')
    cursor = conn.cursor()
    # Creating table with account number as Primary Key
    cursor.execute('''CREATE TABLE IF NOT EXISTS accounts 
                      (acc_num INTEGER PRIMARY KEY, balance REAL, interest_rate REAL)''')
    conn.commit()
    conn.close()

class BankAccount:
    def __init__(self, acc_num, balance):
        self.acc_num = acc_num
        self.balance = balance

    def deposit(self, add_amount):
        # Checking if deposit amount is valid
        if add_amount > 0:
            self.balance += add_amount
            self.update_db()
            print("Amount Deposited:", add_amount)
            print("Current Balance:", self.balance)
        else:
            print("Invalid deposit amount")

    def withdraw(self, wid_amount):
        # Checking for sufficient balance before withdrawal
        if 0 < wid_amount <= self.balance:
            self.balance -= wid_amount
            self.update_db()
            print("Amount Withdrawn:", wid_amount)
            print("Remaining Balance:", self.balance)
        else:
            print("Insufficient funds or invalid amount")

    def update_db(self):
        # Updating the balance in SQLite database
        conn = sqlite3.connect('bank_data.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE accounts SET balance = ? WHERE acc_num = ?", (self.balance, self.acc_num))
        conn.commit()
        conn.close()

class SavingsAccount(BankAccount):
    def __init__(self, acc_num, balance, interest_rate):
        super().__init__(acc_num, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        # Using numpy array to calculate interest amount
        balance_arr = np.array([self.balance])
        interest = (balance_arr * self.interest_rate) / 100
        self.balance += float(interest[0])
        self.update_db()
        print("Interest Rate Applied:", self.interest_rate)
        print("Final Balance after interest:", self.balance)

# Main program execution
if __name__ == "__main__":
    init_db()
    
    # Taking basic inputs from user
    a_num = int(input("Enter Account Number: "))
    bal = float(input("Enter Initial Balance: "))
    rate = float(input("Enter Interest Rate: "))

    # Inserting data into database if it doesn't exist
    conn = sqlite3.connect('bank_data.db')
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO accounts VALUES (?, ?, ?)", (a_num, bal, rate))
    conn.commit()
    conn.close()

    # Creating object of SavingsAccount
    obj = SavingsAccount(a_num, bal, rate)
    
    # Performing bank operations
    dep = float(input("Enter amount to deposit: "))
    obj.deposit(dep)
    
    withd = float(input("Enter amount to withdraw: "))
    obj.withdraw(withd)
    
    print("Calculating interest...")
    obj.apply_interest()