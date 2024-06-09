from user import User
from question import Question
from answer import Answer


class StackOverflow:
    def __init__(self):
        self.questions = {}
        self.users = {}

    def add_user(self, name):
        if name in self.users:
            print("user already exist")
            return self.users[name]
            
        user = User(name)
        self.users[name] = user
        return user

    def add_question(self, user_name, question_text, tags):
        if user_name not in self.users:
            print("user not exist")
            return
        
        user_id = self.users[user_name]
        question = Question(question_text, tags, user_id)
        self.questions[question_text] = question
        return question

    def add_answer(self, user_name, question_text, answer_text):
        if user_name not in self.users:
            print("user not exist")
            return
        
        if question_text not in self.questions:
            print("question doesn't exist")
            return
        
        user = self.users[user_name]
        question = self.questions[question_text]

        answer = Answer(answer_text, question.id, user.id)
        question.answers.append(answer)
        return answer

    def get_feeds(self, tag=None):
        questions = self.questions.values()

        feeds = []
        for question in questions:
            if tag:
                if tag in question.tags:
                    feeds.append(f"question: {question.question}")
            else:
                feeds.append(f"question: {question.question}")

        return feeds