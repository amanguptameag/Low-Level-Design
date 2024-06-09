import uuid

class Question:
    def __init__(self, question_text, tags, user_id):
        self.id = str(uuid.uuid4())
        self.question = question_text
        self.tags = tags
        self.user_id = user_id
        self.answers = []
        