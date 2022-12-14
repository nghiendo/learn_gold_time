from datetime import datetime
from time import time


class Question():
    def __init__(self, title = None, answers = None, topic = None, cid=None, les_id = None):
        self.title = title
        self.answers = answers
        self.topic = topic
        self.cid = cid
        self.les_id = les_id

    def serialize(self):
        return {
            "id": "{obj}{time}".format(obj="Q", time=int(time())),
            "cid": int(self.cid),
            "title": self.title,
            "answers": self.answers,
            "topic": self.topic,
            "lesson_id": self.les_id,
            "created_at": str(datetime.now()) 
        }

    def ques_ans(self):
        pass