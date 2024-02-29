import json
import requests
import random

class Hangman:
    def __init__(self):
        self.word = ''
        self.secret = ''
        self.wrong = []
        self.correct = []

    def get_word_local(self):
        words = ['computer', 'concurrency', 'constructor', 'polymorphism', 'inheritance']
        pos = random.randint(0, 4)
        return words[pos]

    def start_new_game(self):
        self.wrong = []
        self.correct = []
        # url = 'https://random-word-api.herokuapp.com/word'
        url = 'https://random-word-api.vercel.app/api?words=1'
        response = requests.get(url)
        data = json.loads(response.text)
        self.word = data[0]
        # self.word = self.get_word_local()
        print(self.word)
        self.compose_secret_word()


    def compose_secret_word(self):
        self.secret = self.word[0]
        for i in range(1, len(self.word)-1):
            if self.word[i] in self.correct:
                self.secret += self.word[i]
            else:
                self.secret += '_'
        self.secret += self.word[-1]

    def play(self, letter):
        if letter in self.word and letter not in self.correct:
            self.correct.append(letter)
        elif letter not in self.wrong:
            self.wrong.append(letter)
        self.compose_secret_word()

    def is_hanged(self):
        return len(self.wrong) == 6

    def found(self):
        return self.word == self.secret
