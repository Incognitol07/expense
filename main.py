class Report:
    @staticmethod
    def display():
        try:
            with open("expenses.csv", "r") as file:
                report = file.readlines()
                for idx,line in enumerate(report, start=1):
                    print(f"{idx}. {line}")
        except FileNotFoundError:
            raise InOutError("Expenses file not found!")
    
    @staticmethod
    def report():
        try:
            with open("expenses.csv", "r") as file:
                report = file.readlines()
                return report
        except FileNotFoundError:
            raise InOutError("Expenses file not found!")


class Storage:
    @staticmethod
    def store(record: dict):
        with open("expenses.csv","a") as file:
            file.write(f"{record['date']},{record['description']},{record['amount']},{record['category']}\n")

class InOutError(Exception):
    ...

class Retrieval:
    @staticmethod
    def filter(category):
        filtered = []
        report = Report.report()
        for record in report:
            record_fields = record.split(",")
            if record_fields[3].strip() == category:
                filtered.append(record_fields)
        return filtered
    
    @staticmethod
    def display_filtered(category):
        filtered_records = Retrieval.filter(category)
        if not filtered_records:
            print(f"No records found for category: {category}")
            return
        
        for idx, record in enumerate(filtered_records, start=1):
            print(f"{idx}. Date: {record[0]}, Description: {record[1]}, Amount: {record[2]}, Category: {record[3].strip()}")



class Edit:
    @staticmethod
    def modify_record(index, new_record: dict):
        report = Report.report()  # Load all records
        if index < 1 or index > len(report):
            print("Invalid index.")
            return

        # Replace the old record with the new one
        report[index - 1] = f"{new_record['date']},{new_record['description']},{new_record['amount']},{new_record['category']}\n"
        
        # Write updated data back to the file
        with open("expenses.csv", "w") as file:
            file.writelines(report)
        print("Record updated successfully.")

    @staticmethod
    def delete_record(index):
        report = Report.report()  # Load all records
        if index < 1 or index > len(report):
            print("Invalid index.")
            return
        
        # Remove the selected record
        report.pop(index - 1)
        
        # Write the updated data back to the file
        with open("expenses.csv", "w") as file:
            file.writelines(report)
        print("Record deleted successfully.")


class Record:
    def __init__(self, date: str, description: str, amount: float, category:str):
        self._date = date
        self._description = description
        self._amount = amount
        self._category = category

    @property
    def date(self):
        return self._date
    
    @property
    def description(self):
        return self._description
    
    @property
    def amount(self):
        return self._amount
    
    @property
    def category(self):
        return self._category
    
    def details(self):
        return {"date": self.date,"description": self.description,"amount": self.amount,"category": self.category}
    

if __name__ == "__main__":
    pass
