
# Importing the question object from the quiz.py file

from quiz import question

question_prompts = [
    "What color are Oranges?\n(a) Red\n(b) Orange\n(c) Purple\n\n",
    "What color are Bananas?\n(a) Green\n(b) Gray \n(c) Yellow\n\n",
    "What color are Strawberries?\n(a) Red\n(b) Yellow\n(c) Teal\n\n"
]


questions = [
    question(question_prompts[0], "b"),
    question(question_prompts[1], "c"),
    question(question_prompts[2], "a"),
]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You scored " + str(score) + "/" + str(len(questions)), "correct")

run_test(questions)