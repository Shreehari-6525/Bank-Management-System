# 🏦 Python Banking Management System

A console-based Banking Management System developed using Python as part of the Python training program conducted by **Rubicon** under the guidance of **Prof. Vipul Mahindrakar, Training and Placement Head**.

The project demonstrates core Python programming concepts through a practical banking application, including account creation, loan eligibility checks, money transactions, customer record management, and locker services.

## 📌 Project Overview

The Python Banking Management System simulates basic banking operations through an interactive, menu-driven interface. Users can create bank accounts, view customer details, apply for different types of loans, perform financial transactions, and manage bank lockers.

This project was developed as a practical learning exercise to strengthen programming fundamentals and apply Python concepts to a real-world-inspired scenario.

## ✨ Features

### 1. Account Management
- Create a new customer account.
- Choose between Current and Savings accounts.
- Validate minimum opening balance requirements.
- Generate a unique 12-digit account number.
- Store customer information, including name, age, date of birth, mobile number, and account type.

### 2. Loan Management
- Apply for four types of loans:
  - Home Loan
  - Car Loan
  - Education Loan
  - Agricultural Loan
- Check basic loan eligibility based on annual income, repayment period, and estimated monthly principal repayment.
- Maintain loan status and loan type in customer records.
- Prevent multiple loan applications when a loan is already recorded.

### 3. Money Transactions
- Deposit money into an account.
- Withdraw money after checking the available balance.
- Transfer money between two existing accounts.
- Update account balances after successful transactions.
- Validate account numbers, transaction amounts, and available funds.

### 4. Locker Management
- Create a locker linked to an existing bank account.
- Generate a unique locker number.
- Set and confirm a four-digit locker PIN.
- Access the locker after verifying the locker number and PIN.
- Prevent duplicate locker creation for the same account.

### 5. Customer Details
- Retrieve customer records using an account number.
- Display account holder information in an aligned format.
- View account balance, account type, loan status, and locker status.
- Display the locker number when a locker has been created.

### 6. Interactive Menu
- Use a menu-driven interface for navigation.
- Handle invalid menu choices.
- Return to the main menu after completing an operation.
- Exit the program gracefully.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.10+ | Core programming language |
| `random` module | Generate account and locker numbers |
| `match-case` | Menu selection and control flow |
| Lists and dictionaries | Store customer and account information |
| Functions | Organize banking operations into reusable modules |
| Conditional statements | Validate transactions and eligibility |
| Loops | Handle repeated menu operations and record searches |
| String formatting | Display aligned customer information |

**External libraries:** None required. The project uses Python's built-in functionality.

## 📂 Project Structure

```text
Python-Banking-Management-System/
│
├── banking_system.py
└── README.md
```

`banking_system.py` contains the main application and its banking functionalities.

## ⚙️ Installation and Execution

### Prerequisites
- Python 3.10 or later.
- A code editor such as Visual Studio Code or PyCharm.
- A terminal or command prompt.

### Step 1: Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Replace the placeholder with your actual GitHub repository URL.

### Step 2: Open the project directory

```bash
cd Python-Banking-Management-System
```

### Step 3: Run the application

```bash
python banking_system.py
```

On Windows, if the `python` command is unavailable, try:

```bash
py banking_system.py
```

### Step 4: Select an operation

The main menu provides the following options:

```text
========== BANK SYSTEM ==========
1. Create Account
2. Apply For Loan
3. Display Customer Details
4. Money Transaction
5. Locker Services
6. Exit
Enter Your Choice:
```

Enter the corresponding number to perform the desired operation.

## 🧠 Python Concepts Learned and Applied

This project provides practical experience with the following Python concepts:

- **Variables and data types:** Store customer information, account balances, and transaction details.
- **Lists:** Maintain customer information in an ordered structure.
- **Dictionaries:** Associate account numbers with customer records.
- **Functions:** Separate account creation, loan processing, transactions, and locker operations into reusable functions.
- **Loops:** Iterate through customer records and repeatedly display menus.
- **Conditional statements:** Validate account details, minimum balances, loan eligibility, and transaction conditions.
- **Pattern matching:** Implement menu navigation using `match-case`.
- **Random number generation:** Generate account and locker numbers using Python's `random` module.
- **Input handling:** Accept and process customer input.
- **String formatting:** Present customer information in a readable, aligned format.
- **Data manipulation:** Update account balances, loan statuses, and locker information.

## 🗃️ Data Storage Approach

The application uses a list containing dictionaries, with each dictionary mapping an account number to an inner list of customer details.

Example:

```python
customer_details = [
    {
        123456789012: [
            "Shreehari",
            21,
            50000,
            True,
            "21/05/2005",
            "9876543210",
            "Saving",
            False,
            "None",
            False,
            None,
            None
        ]
    }
]
```

This structure demonstrates how Python collections can represent related data without requiring a database.

**Note:** Customer records are stored in memory and are not retained after the program terminates.

## 🔮 Future Enhancements

The project can be extended with the following improvements:

- Integrate MySQL or SQLite for persistent customer records.
- Introduce secure authentication and password or PIN hashing.
- Add transaction history and account statements.
- Implement interest-rate-based loan repayment calculations.
- Add transaction limits and minimum-balance enforcement.
- Introduce input validation and exception handling.
- Develop a graphical user interface or web-based banking dashboard.
- Add automated unit tests for banking operations.
- Implement audit logs and stronger access controls.

## ⚠️ Disclaimer

This project is intended for educational purposes and Python training practice only. It is not a production-ready banking application and must not be used to store real financial information or perform actual financial transactions.

Loan eligibility calculations are simplified demonstrations and do not represent official lending criteria. Locker PINs and customer records are not protected using production-grade security mechanisms.

## 🎓 Training and Acknowledgement

This project was developed as part of the Python training program conducted by **Rubicon**.

Special acknowledgement to **Prof. Vipul Mahindrakar, Training and Placement Head**, for his guidance and support during the training.

The project reflects the practical application of Python programming concepts learned during the training program.

## 👨‍💻 Author

**Shreehari Patil**

Computer Engineering | Python Programming | Software Development

---

*Developed as a Python training project with Rubicon under the guidance of Prof. Vipul Mahindrakar, Training and Placement Head.*
