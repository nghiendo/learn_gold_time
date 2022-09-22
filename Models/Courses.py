from datetime import datetime
from random import random
from time import time


class Course():
    def __init__(self, name = None, img = None, tags = None):
        self.name = name
        self.img = img
        self.tags = tags
    
    def serialize(self):
        return {
            "id": "{}{}".format("C", int(time())),
            "name": self.name,
            "img": self.img,
            "tags": self.tags,
            "date": str(datetime.now()),
            "child": []
        }