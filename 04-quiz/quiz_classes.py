import random
import json
import requests
import html

class User:
    def __init__(self):
        self.name = 'N/A'
        self.score = 0

    def read_name(self):
        self.name = input("Type your name: ")

    def increase_score(self):
        self.score += 1

    def print_score(self):
        print("SCORE:", self.score, "/ 10")


class Question:
    def __init__(self):
        self.question = "N/A"
        self.answers = []
        self.correct_answer = -1
        self.type = "N/A"
        self.difficulty = "N/A"
        self.category = "N/A"

    def set_answers(self, correct, incorrect_list):
        self.answers = list(incorrect_list)
        r = random.randint(0, 3)
        self.answers.insert(r, correct)
        for i in range(len(self.answers)):
            self.answers[i] = html.unescape(self.answers[i])
        self.correct_answer = r

class Quiz:
    def __init__(self):
        self.questions = []

    def get_quiz(self):
        url = 'https://opentdb.com/api.php?amount=10&type=multiple'

        response = requests.get(url)
        data = json.loads(response.text)
        quiz = data['results']

        for item in quiz:
            q = Question()
            q.type = html.unescape(item['type'])
            q.category = html.unescape(item['category'])
            q.difficulty = html.unescape(item['difficulty'])
            q.question = html.unescape(item['question'])
            q.set_answers(item['correct_answer'], item['incorrect_answers'])
            self.questions.append(q)

    def display_question(self, pos):
        # print("CA", self.questions[pos].correct_answer)
        print(self.questions[pos].question)
        counter = 1
        for answer in self.questions[pos].answers:
            print(counter, answer)
            counter += 1

    def check_answer(self, answer, pos, user):
        if self.questions[pos].correct_answer == answer - 1:  # because user responds 1-4 but answer list is 0-3
            user.increase_score()

