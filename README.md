# Database-Driven Banking System

A professional Python-based banking application that demonstrates the integration of Object-Oriented Programming (OOPs), Database Management (DBMS), and Data Science libraries.

## 🚀 Key Features

- **Data Persistence:** Integrated **SQLite** database to ensure that account balances and details are saved permanently, even after the program is closed.
- **Advanced Calculations:** Utilized **NumPy** for efficient interest rate processing and numerical operations.
- **Object-Oriented Structure:** Built using inheritance (SavingsAccount inheriting from BankAccount) to ensure code reusability and clean architecture.
- **Input Validation:** Includes error handling for withdrawal and deposit operations to prevent negative balances or invalid entries.

## 🛠️ Tech Stack

- **Language:** Python 3
- **Database:** SQLite3 (SQL)
- **Library:** NumPy
- **Version Control:** Git & GitHub

## 📂 Project Structure

- `bank_system.py`: The main source code containing class logic, database connections, and user interaction.
- `bank_data.db`: The local database file generated automatically to store user data.

## 📝 How to Run
1. Ensure Python and NumPy are installed: `pip install numpy`
2. Run the script: `python bank_system.py`
3. Enter account details to start banking operations.
