import re
import json
from datetime import datetime


class Transaction:
    def __init__(self, date, description, amount, credit_balance):
        self.date = date
        self.description = description
        self.amount = amount
        self.credit_balance = credit_balance

    @classmethod
    def from_data(cls, data):
        date_string, description, amount, credit_balance = data
        datetime_obj = datetime.strptime(date_string, "%m/%d/%Y")
        date = {
            "month": datetime_obj.month,
            "day": datetime_obj.day,
            "year": datetime_obj.year
        }
        return cls(date, description, amount, credit_balance)


class CSVParser:
    @staticmethod
    def csv_to_json(csv_file, json_file=None):
        transactions = []

        with open(csv_file, "r") as in_file:
            for line in in_file:
                line = line[:-1]
                data = re.split(',+', line)
                t = Transaction.from_data(data)
                transactions.append(t)

        json_data = json.dumps([t.__dict__ for t in transactions])

        # if json file is not given, don't write to file
        if json_file:
            with open(json_file, "w") as out_file:
                out_file.write(json_data)

        return json_data


csv_file = "./example.csv"
json_file = "./transactions.json"

CSVParser.csv_to_json(csv_file, json_file)
