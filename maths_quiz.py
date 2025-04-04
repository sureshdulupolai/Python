import random
from quiz_class import Quiz

def QuizOperator(valueOne = 0, valueTwo = 0):
    OperationWith = RandomOpeartion()
    print("Question For : {}".format(OperationWith))
    FormateOperation(OperationWith, valueOne, valueTwo)

def RandomOpeartion():
    randomValueOperation = random.randint(0, 4)
    OperationList = ['addition', 'Substraction', 'Multiplaction', 'Division', 'Mode']
    return OperationList[randomValueOperation]
    
def FormateOperation(operation, valueOne, valueTwo):
    if operation == 'addition':
        AnswerOfQuiz = round(valueOne + valueTwo, 2)

        try:
            userAnswer = float(input('{} + {} = '.format(valueOne, valueTwo)))
            AnswerCheck(AnswerOfQuiz = AnswerOfQuiz, userAnswer = userAnswer)

        except:
            print('\n-- Input in the Floating or Integer --')

        
    elif operation == 'Substraction':
        AnswerOfQuiz = AnswerOfQuiz = round(valueOne - valueTwo, 2)

        try:
            userAnswer = float(input('{} - {} = '.format(valueOne, valueTwo)))
            AnswerCheck(AnswerOfQuiz = AnswerOfQuiz, userAnswer = userAnswer)

        except:
            print('\n-- Input in the Floating or Integer --')

        
    elif operation == 'Multiplaction':
        AnswerOfQuiz = AnswerOfQuiz = round(valueOne * valueTwo, 2)

        try:
            userAnswer = float(input('{} * {} = '.format(valueOne, valueTwo)))
            AnswerCheck(AnswerOfQuiz = AnswerOfQuiz, userAnswer = userAnswer)

        except:
            print('\n-- Input in the Floating or Integer --')
        
        
    elif operation == 'Division':
        if valueTwo == 0: valueTwo += 1
        AnswerOfQuiz = round(valueOne / valueTwo, 2)

        try:
            userAnswer = float(input('{} / {} = '.format(valueOne, valueTwo)))
            AnswerCheck(AnswerOfQuiz = AnswerOfQuiz, userAnswer = userAnswer)

        except:
            print('\n-- Input in the Floating or Integer --')

        
    elif operation == 'Mode':
        AnswerOfQuiz = round(valueOne % valueTwo, 2)

        try:
            userAnswer = float(input('{} % {} = '.format(valueOne, valueTwo)))
            AnswerCheck(AnswerOfQuiz = AnswerOfQuiz, userAnswer = userAnswer)

        except:
            print('\n-- Input in the Floating or Integer --')

        

def AnswerCheck(userAnswer, AnswerOfQuiz):
    if userAnswer == AnswerOfQuiz:
        print('Your answer is corrent, Now you can go in next round')
        print()
        Quiz(count = 1, point = 100)
        MathsQuiz()

    else:
        print('Oops!, You have not fill proper answer for this question')
        print('Your answer : {} \nCorrect Answer : {}'.format(userAnswer, AnswerOfQuiz))

# ----------------------------------------------------------------------------------------
def StartExecute():
    lst = []
    for DataForList in range(11):
        Data = random.randint(0, 100)
        if Data not in lst:
            lst += [Data]

    randomIndexForFirstVariable = random.randint(0, (len(lst) - 1))
    randomIndexForSecondVariable = random.randint(0, (len(lst) - 1))

    QuizFirstVariable = lst[randomIndexForFirstVariable]
    QuizSecondVariable = lst[randomIndexForSecondVariable]

    return (QuizFirstVariable, QuizSecondVariable)
# -----------------------------------------------------------------------
def MathsQuiz():

    QuizFirstVariable, QuizSecondVariable  = StartExecute()

    checkUserCondition = input('Continue or exit the quiz (y/n) : ')

    if (checkUserCondition in 'yes') or (checkUserCondition in 'YES') :
        QuizOperator(valueOne = QuizFirstVariable, valueTwo = QuizSecondVariable)
    
    elif (checkUserCondition in 'no') or (checkUserCondition in 'NO'):
        print('Thank you for playing maths quiz, Developer')


if __name__ == "__main__":
    MathsQuiz()
else:
    print('Welcome User To "Developer Quiz Game" ')