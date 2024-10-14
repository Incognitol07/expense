class Report:
    """
    A class used to display and retrieve expense reports from a CSV file.

    Methods:
    -------
    display():
        Prints all records from the expenses CSV file to the console.
        
    report():
        Returns the list of all records from the expenses CSV file.
    """
    
    @staticmethod
    def display():
        """Displays all records in the expenses.csv file with line numbers."""
        try:
            with open("expenses.csv", "r") as file:
                report = file.readlines()
                for idx, line in enumerate(report, start=1):
                    print(f"{idx}. {line}")
        except FileNotFoundError:
            raise InOutError("Expenses file not found!")
    
    @staticmethod
    def report():
        """Returns all records from the expenses.csv file as a list of lines."""
        try:
            with open("expenses.csv", "r") as file:
                return file.readlines()
        except FileNotFoundError:
            raise InOutError("Expenses file not found!")


class Storage:
    """
    A class used to store new expense records into the CSV file.

    Methods:
    -------
    store(record: dict):
        Appends a new record to the expenses.csv file.
    """
    
    @staticmethod
    def store(record: dict):
        """Stores a new record into the expenses.csv file."""
        # Ensure all necessary fields are present before saving the record
        if 'date' not in record or 'description' not in record or 'amount' not in record or 'category' not in record:
            raise InOutError("Incomplete record data.")
        
        # Append the record to the file
        with open("expenses.csv", "a") as file:
            file.write(f"{record['date']},{record['description']},{record['amount']},{record['category']}\n")


class InOutError(Exception):
    """Custom exception for I/O-related errors."""
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Retrieval:
    """
    A class used for filtering expense records by category.

    Methods:
    -------
    filter(category: str):
        Filters and returns the records that match the provided category.

    display_filtered(category: str):
        Prints the filtered records based on the provided category.
    """
    
    @staticmethod
    def filter(category):
        """
        Filters records by category.
        
        Parameters:
        category (str): The category to filter records by (case-insensitive).
        
        Returns:
        list: A list of records that match the given category.
        """
        filtered = []
        report = Report.report()
        for record in report:
            record_fields = record.split(",")
            # Case-insensitive comparison of the category
            if record_fields[3].strip().lower() == category.lower():
                filtered.append(record_fields)
        return filtered
    
    @staticmethod
    def display_filtered(category):
        """
        Displays filtered records that match the specified category.
        
        Parameters:
        category (str): The category to filter records by.
        """
        filtered_records = Retrieval.filter(category)
        if not filtered_records:
            print(f"No records found for category: {category}")
            return
        
        # Display filtered records with details
        for idx, record in enumerate(filtered_records, start=1):
            print(f"{idx}. Date: {record[0]}, Description: {record[1]}, Amount: {record[2]}, Category: {record[3].strip()}")


class Edit:
    """
    A class used to modify or delete existing expense records.

    Methods:
    -------
    modify_record(index: int, new_record: dict):
        Modifies a specific record by index with new data.

    delete_record(index: int):
        Deletes a specific record by index.
    """
    
    @staticmethod
    def modify_record(index: int, new_record: dict):
        """
        Modifies an existing record in the expenses.csv file.
        
        Parameters:
        index (int): The line number of the record to modify (1-based).
        new_record (dict): The new record data to replace the old one.
        """
        report = Report.report()
        
        # Validate the index
        if index < 1 or index > len(report):
            raise InOutError("Invalid record index.")
        
        # Ensure new record data is complete
        if 'date' not in new_record or 'description' not in new_record or 'amount' not in new_record or 'category' not in new_record:
            raise InOutError("Incomplete new record data.")
        
        # Update the record at the given index
        report[index - 1] = f"{new_record['date']},{new_record['description']},{new_record['amount']},{new_record['category']}\n"
        
        # Write updated records back to the file
        with open("expenses.csv", "w") as file:
            file.writelines(report)
        print("Record updated successfully.")

    @staticmethod
    def delete_record(index: int):
        """
        Deletes a record from the expenses.csv file.
        
        Parameters:
        index (int): The line number of the record to delete (1-based).
        """
        report = Report.report()
        
        # Validate the index
        if index < 1 or index > len(report):
            raise InOutError("Invalid record index.")
        
        # Remove the record at the given index
        report.pop(index - 1)
        
        # Write updated records back to the file
        with open("expenses.csv", "w") as file:
            file.writelines(report)
        print("Record deleted successfully.")


class Record:
    """
    A class representing an individual expense record.

    Methods:
    -------
    details():
        Returns the details of the record as a dictionary.
    """
    
    def __init__(self, date: str, description: str, amount: float, category: str):
        """
        Initializes the record with the provided values.
        
        Parameters:
        date (str): The date of the expense in DD/MM/YYYY format.
        description (str): A brief description of the expense.
        amount (float): The amount spent.
        category (str): The category of the expense.
        """
        # Validate date format
        if not self.validate_date(date):
            raise InOutError("Invalid date format. Use DD/MM/YYYY.")
        
        # Ensure amount is positive
        if amount <= 0:
            raise InOutError("Amount must be positive.")
        
        self._date = date
        self._description = description
        self._amount = amount
        self._category = category

    @property
    def date(self):
        """Returns the date of the record."""
        return self._date
    
    @property
    def description(self):
        """Returns the description of the record."""
        return self._description
    
    @property
    def amount(self):
        """Returns the amount of the record."""
        return self._amount
    
    @property
    def category(self):
        """Returns the category of the record."""
        return self._category
    
    def details(self):
        """
        Returns the record details as a dictionary.
        
        Returns:
        dict: A dictionary containing the record's date, description, amount, and category.
        """
        return {"date": self.date, "description": self.description, "amount": self.amount, "category": self.category}
    
    @staticmethod
    def validate_date(date: str) -> bool:
        """
        Validates the date format (DD/MM/YYYY).
        
        Parameters:
        date (str): The date string to validate.
        
        Returns:
        bool: True if the date format is correct, False otherwise.
        """
        import re
        pattern = r"\d{2}/\d{2}/\d{4}"
        return bool(re.match(pattern, date))

if __name__ == "__main__":
    pass
