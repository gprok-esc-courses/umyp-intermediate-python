from quiz_classes import User, Quiz

user = User()
quiz = Quiz()
user.read_name()
quiz.get_quiz()

for i in range(10):
    quiz.display_question(i)
    ans = int(input("Answer: "))
    quiz.check_answer(ans, i, user)

user.print_score()

