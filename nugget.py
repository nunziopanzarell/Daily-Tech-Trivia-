
from datetime import datetime


class Nugget:
    def __init__(self, id: int, question: str, answer: str, link: str, last_execution: datetime):
        self.id = id
        self.question = question
        self.answer = answer
        self.link=link
        self.last_execution=last_execution


