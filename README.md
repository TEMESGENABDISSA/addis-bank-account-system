# Addis Bank Account Management System 🏦

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Git](https://img.shields.io/badge/Git-Version%20Control-orange)
![Project](https://img.shields.io/badge/Project-Banking%20System-green)

## Overview

**Addis Bank Account Management System** is a Python-based banking application designed to manage Ethiopian customer accounts using Ethiopian Birr (ETB).

This project starts with a simple **Account class** and gradually grows into a complete banking system by applying professional software engineering concepts including:

- Object-Oriented Programming (OOP)
- Encapsulation
- Inheritance
- SOLID Principles
- Design Patterns
- Data Structures
- Unit Testing


The purpose of this project is to build a scalable and maintainable banking system similar to real-world financial applications.

---

# Project Goals

The system aims to provide:

- Customer account management
- Multiple account types
- Secure financial transactions
- Balance management
- Transaction tracking
- Account searching and management
- Clean and professional software architecture


---

# Technologies Used

## Programming Language

- Python 3


## Tools

- Git
- GitHub
- Visual Studio Code


## Software Engineering Concepts

- Object-Oriented Programming
- Encapsulation
- Inheritance
- Polymorphism
- SOLID Principles
- Design Patterns
- Data Structures
- Automated Testing


---

# Current Features

## Account Management

The system currently supports:

- Creating bank accounts
- Storing account owner information
- Managing account numbers
- Secure balance management


---

## Account Transactions

Supported operations:

- Deposit money
- Withdraw money
- Check balance
- Generate account statement


All transactions are validated to prevent:

- Negative deposits
- Invalid withdrawals
- Overdraft errors


---

# Account Design

The first version of the system contains an encapsulated Account class.

Example structure:

```
Account

Attributes:
    owner
    account_number
    __balance


Methods:
    deposit()
    withdraw()
    statement()
```

The balance is private and can only be modified through approved methods.

---

# Project Development Roadmap


## Phase 1 - Account Class

Branch:

```
feature/account-class
```

Implemented:

- Account class
- Private balance
- Balance property
- Deposit validation
- Withdrawal validation
- Account statement


---

## Phase 2 - Account Types

Branch:

```
feature/account-types
```

Upcoming features:

- Savings Account
- Current Account
- Account inheritance
- Different account behaviors


Example:

```
              Account
                 |
        -------------------
        |                 |
 SavingsAccount     CurrentAccount
```


---

## Phase 3 - SOLID Design

Branch:

```
feature/solid-design
```

Improvements:

- Separation of responsibilities
- Service classes
- Better code organization
- Maintainable architecture


---

## Phase 4 - Design Patterns

Branch:

```
feature/design-patterns
```

Implemented patterns:

- Factory Pattern
- Singleton Pattern
- Repository Pattern


---

## Phase 5 - Account Management System

Branch:

```
feature/account-management
```

Features:

- Manage multiple accounts
- Search accounts
- Update accounts
- Delete accounts
- Transfer money


---

## Phase 6 - Data Structures

Branch:

```
feature/data-structures
```

Features:

- Lists for account collections
- Dictionaries for fast searching
- Queues for transaction processing
- Transaction history management


---

# Project Structure

Final project structure:

```
addis-bank-account-system/

│
├── README.md
├── .gitignore
├── requirements.txt
│
├── account.py
├── savings_account.py
├── current_account.py
├── customer.py
├── transaction.py
│
├── bank.py
├── account_manager.py
│
├── services/
│   ├── account_service.py
│   └── transaction_service.py
│
├── patterns/
│   └── account_factory.py
│
├── tests/
│   ├── test_account.py
│   ├── test_accounts.py
│   └── test_transactions.py
│
└── docs/
    ├── architecture.md
    └── design.md
```

---

# Git Workflow

This project follows a professional Git branching strategy.


## Main Branch

```
master
```

The master branch contains stable and reviewed code.


## Feature Branches

Development happens using feature branches:

```
feature/account-class

feature/account-types

feature/solid-design

feature/design-patterns

feature/account-management

feature/data-structures
```


Development workflow:

```
Create Feature Branch
          |
          ↓
Write Code
          |
          ↓
Test Changes
          |
          ↓
Commit Changes
          |
          ↓
Push Branch
          |
          ↓
Create Pull Request
          |
          ↓
Code Review
          |
          ↓
Merge Into Master
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/TEMESGENABDISSA/addis-bank-account-system.git
```

Move into the project:

```bash
cd addis-bank-account-system
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Application

Run:

```bash
python main.py
```

---

# Testing

The project includes tests to verify:

- Account creation
- Deposit operations
- Withdrawal operations
- Balance validation
- Transaction processing


Run tests:

```bash
pytest
```

---

# Future Improvements

## Database Integration

Future versions will include:

- MySQL/PostgreSQL database
- Customer records
- Account storage
- Transaction history


## Security Features

Planned:

- User authentication
- Password encryption
- PIN verification
- Transaction authorization


## User Interface

Future versions:

- Command Line Interface
- Web Application
- Mobile Application


## Additional Banking Features

Planned:

- Money transfer
- Loan management
- Interest calculation
- Notifications
- Monthly statements


---

# Learning Outcomes

Through this project, the following skills are developed:

- Writing clean Python code
- Designing scalable applications
- Using Git professionally
- Applying software engineering principles
- Building maintainable systems


---

# Author

**Temesgen Abdissa**

Information Systems Student  
Software Developer


---

# License

This project is created for educational purposes.