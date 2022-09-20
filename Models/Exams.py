from datetime import datetime
from time import time


class Exam():
    def __init__(self, course = None, questions = [], uid = None):
        self.course = course
        self.questions = questions
        self.uid = uid
    def serialize(self):
        return {
            "id": "{}{}".format("E", int(time()*100)),
            "course": self.course,
            "questions": self.questions,
            "uid": self.uid,
            "created_at": str(datetime.now()),
            "updated_at": str(datetime.now()),
            "time_sugg_next": time()+3600
        }
