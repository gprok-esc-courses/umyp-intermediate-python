import random

ca = "correct"

ia = ["incorrec1", "incorrec2", "incorrec3"]

answers = list(ia)

r = random.randint(0, 3)
answers.insert(r, ca)

print(answers)
print(ia)
