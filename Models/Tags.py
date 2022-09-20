from time import time

class Tags():
    def __init__(self, name = None, root = None):
        self.name = name
        self.root = root
    def serialize(self):
        return {
            "id": "{}{}".format("T", int(time() * 100)),
            "name": self.name,
            "root": self.root,
            "child": []
        }