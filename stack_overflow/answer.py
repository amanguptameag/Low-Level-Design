import uuid

class Answer:
    def __init__(self, answer_text, question_id, user_id):
        self.id = str(uuid.uuid4())
        self.answer = answer_text
        self.question_id = question_id
        self.user_id = user_id
        