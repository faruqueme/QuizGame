from data import question_data2
from question_model import Question
from quiz_brain import QuizBrain
question_bank= []
for i in question_data2["results"]:
    x = i['question']
    y = i['correct_answer']
    quesanans = Question(x,y)
    question_bank.append(quesanans)
quizbrain= QuizBrain(question_bank)

while quizbrain.still_has_questions():
    quizbrain.next_question ( )
if quizbrain.question_number == len (question_data2["results"]):
    print (f"You have completed the challenge!!!\nYour final score is {quizbrain.score}/{quizbrain.question_number}")