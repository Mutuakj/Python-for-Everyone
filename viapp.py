from vivi import quiz

question_prompts = [
    "What color is my Phone?\n(a) 'Black'\n(b) 'Red'\n(c) 'Purple'\n",
    "What color is my curtains?\n(a) 'Black'\n(b) 'Yellow'\n(c) 'Brown'\n",
    "What type is my Laptop?\n(a) 'HP'\n(b) 'Dell'\n(c) 'Lenovo'\n"
]

questions = [
    quiz(question_prompts[0], 'a'),
    quiz(question_prompts[1], 'b'),
    quiz(question_prompts[2], 'a')
]


def run_test(questions):
    score = 0
    for question in questions:
        while True:
            answer = input(question.prompts)
            if answer in ['a', 'b', 'c']:
                break
            else:
                print("Invalid input! Please enter 'a', 'b', or 'c'.")
        if answer == question.answer:
            score += 1
    if score >= 2:
        print('Congratulations! You scored ' + str(score) + '/' + str(len(question_prompts)), 'correct')
    else:
        print('Poor! You scored ' + str(score) + '/' + str(len(question_prompts)), 'correct')


run_test(questions)
