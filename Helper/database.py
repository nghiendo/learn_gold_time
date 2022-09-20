import json
from operator import truediv
from os import path
from config import rootfile
class Database():
    table_dir = None
    def __init__(self, table) -> None:
        table = table
        self.table_dir = "{}/Data/{}.json".format(rootfile(), table)

    def select(self, WHERE = None, limit = None):
        if path.exists(self.table_dir) is False:
            return []
        with open(self.table_dir, "r") as file:
            data = json.load(file)
            if WHERE is None:
                return data
            result = []
            i = 0
            for x in data:
                if limit is not None:
                    if limit == i:
                        return result
                flag = False
                for key, value in WHERE.items():
                    if x[key] == value:
                        flag = True
                    else:
                        # print(x, value, flag, end="")
                        # if flag is True:
                        #     flag = False
                        #     break
                        break
                if flag is True:
                    result.append(x)
                    i += 1
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

    def delete(self, WHERE = None):
        with open(self.table_dir, "r") as file:
            if WHERE is None:
                return 0
            content = json.load(file)
            for i,x in enumerate(content):
                flag = False
                for key, value in WHERE.items():
                    if x[key] == value:
                        flag = True
                    else:
                        flag = False
                        break
                if flag == True:
                    del content[i]
                    with open(self.table_dir, "w") as f:
                        json.dump(content, f, indent=4)
                        return 1                        
            return 0