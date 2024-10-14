class Report:
    @staticmethod
    def display():
        with open("expenses.csv", "r") as file:
            report = file.readlines()
            for idx,line in enumerate(report, start=1):
                print(f"{idx}. {line}")
            file.close()

class Storage:
    @staticmethod
    def store(record: dict):
        with open("expenses.csv","a") as file:
            file.write(f"{record['date']}, {record['description']}, {record['amount']}, {record['category']}")
            file.close()

class InOutError(Exception):
    ...

class Retrieval:
    ...

class Edit:
    ...

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
        return {"date": self.date, "description": self.description, "amount": self.amount, "category": self.category}
    

if __name__ == "__main__":
    pass
