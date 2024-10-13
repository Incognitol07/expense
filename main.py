class Report:
    ...

class Storage:
    ...

class InOutError(Exception):
    ...

class Retrieval:
    ...

class Edit:
    ...

class Record:
    def __init__(self, date, description, amount, category):
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