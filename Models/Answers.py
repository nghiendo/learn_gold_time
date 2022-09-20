from time import time


class Answers():
    def __init__(self, ans, topic):
        self.ans = ans
        self.topic = topic
    
    def serialize(self):
        return {
            "id": "{obj}{time}".format(obj="A", time=int(time()*1000)),
            "ans": self.ans,
            "topic": self.topic,
        }