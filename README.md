# Expense Tracker

A simple Python-based application for tracking and categorizing personal expenses, with the ability to filter by category and dynamically display records.

## Features
- **Add Expenses**: Easily add records with date, description, amount, and category.
- **View Expenses**: Display all expenses in a structured format with a total amount.
- **Filter by Category**: Filter expenses by category and view the results with a total amount.
- **Simple File Storage**: Stores data in a CSV file for simplicity.

## Technologies Used
- **Python**: Core programming language.
- **CSV**: Used for data storage (read/write operations).

## How to Use
### 1. Clone the repository
   ```bash
   git clone https://github.com/Incognitol07/your-repo.git
   cd your-repo
   ```
### 2. Add an Expense
    Run the program and add expenses using the interface or directly into the expenses.csv file.



# CSV File Structure
The expenses are stored in expenses.csv in the following format:

```csv
Date, Description, Amount, Category
```

### 3. Run the Application
    To execute the application:

```bash
python main.py
```
# Code Overview
The project consists of the following components:

expense_tracker.py: Main logic for handling expenses (adding, viewing, and filtering).
CSV file (expenses.csv): Stores the expense records in CSV format.

# Contributing
Contributions are welcome! Feel free to submit pull requests to improve features or fix bugs.
