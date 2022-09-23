import json
from os import path
from config import rootfile
from Helper.helper import findLocate
class Database():
    table_dir = None
    def __init__(self, table) -> None:
        table = table
        self.table_dir = path.join(rootfile(), "data", table+".json")

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
                        flag = False
                        break
                if flag is False and "child" in x:
                    for y in x['child']:
                        for key, value in WHERE.items():
                            if y[key] == value:
                                flag = True
                            else:
                                flag = False
                                break
                    if flag is True:
                        result.append(y)
                        i += 1
                        continue
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

    def update(self, data = {}, WHERE = {}):
        try:
            with open(self.table_dir, "r") as file:
                content = json.load(file)
                i = findLocate(content, WHERE)
                for key, value in data.items():
                    content[i][key] = value
                with open(self.table_dir, "w") as f:
                    json.dump(content, f, indent=4)
                    return 1
        except:
            return 0         