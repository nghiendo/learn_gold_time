import json
from os import path
from config import rootfile
class Database():
    table_dir = None
    def __init__(self, table) -> None:
        table = table
        self.table_dir = "{}/Data/{}.json".format(rootfile(), table)

    def select(self, WHERE = None):
        if path.exists(self.table_dir) is False:
            return []
        with open(self.table_dir, "r") as file:
            data = json.load(file)
            if WHERE is None:
                return data
            result = []
            for x in data:
                flag = False
                for key, value in WHERE.items():
                    if x[key] == value:
                        flag = True
                    else:
                        if flag is True:
                            flag = False
                            break
                if flag is True:
                    result.append(x)
            return result
    
    def insert(self, data):
        if path.exists(self.table_dir) is False:
            return 0
        with open(self.table_dir, "r+") as file:
            content = json.load(file)
            content.append(data)
            file.seek(0)
            json.dump(content, file, indent=4)
            return 1