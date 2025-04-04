import random

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
        AnswerOfQuiz = valueOne + valueTwo

        try:
            userAnswer = float(input('{} + {} = '.format(valueOne, valueTwo)))
            AnswerCheck(AnswerOfQuiz = AnswerOfQuiz, userAnswer = userAnswer)

        except:
            print('\n-- Input in the Floating or Integer --')

        
    elif operation == 'Substraction':
        AnswerOfQuiz = valueOne - valueTwo

        try:
            userAnswer = float(input('{} - {} = '.format(valueOne, valueTwo)))
            AnswerCheck(AnswerOfQuiz = AnswerOfQuiz, userAnswer = userAnswer)

        except:
            print('\n-- Input in the Floating or Integer --')

        
    elif operation == 'Multiplaction':
        AnswerOfQuiz = valueOne * valueTwo

        try:
            userAnswer = float(input('{} * {} = '.format(valueOne, valueTwo)))
            AnswerCheck(AnswerOfQuiz = AnswerOfQuiz, userAnswer = userAnswer)

        except:
            print('\n-- Input in the Floating or Integer --')
        
        
    elif operation == 'Division':
        if valueTwo == 0: valueTwo += 1
        AnswerOfQuiz = valueOne / valueTwo

        try:
            userAnswer = float(input('{} / {} = '.format(valueOne, valueTwo)))
            AnswerCheck(AnswerOfQuiz = AnswerOfQuiz, userAnswer = userAnswer)

        except:
            print('\n-- Input in the Floating or Integer --')

        
    elif operation == 'Mode':
        AnswerOfQuiz = valueOne % valueTwo

        try:
            userAnswer = float(input('{} % {} = '.format(valueOne, valueTwo)))
            AnswerCheck(AnswerOfQuiz = AnswerOfQuiz, userAnswer = userAnswer)

        except:
            print('\n-- Input in the Floating or Integer --')

        

def AnswerCheck(userAnswer, AnswerOfQuiz):
    if userAnswer == AnswerOfQuiz:
        print('Your answer is corrent, Now you can go in next round')
        print()
        MathsQuiz()

    else:
        print('Oops!, You have not fill proper answer for this question')
        print('Your answer : {} \nCorrect Answer : {}'.format(userAnswer, AnswerOfQuiz))

# -----------------------------------------------------------------------------------------
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(len(lst))

# Random no generating for excessing with that index value from lst
# ---------------------------------------------------------------------
randomIndexForFirstVariable = random.randint(0, (len(lst) - 1))
randomIndexForSecondVariable = random.randint(0, (len(lst) - 1))
# print(randomIndexForFirstVariable)
# print(randomIndexForSecondVariable)

# Random Number From lst inside variable
# ----------------------------------------------------------------------
QuizFirstVariable = lst[randomIndexForFirstVariable]
QuizSecondVariable = lst[randomIndexForSecondVariable]
# print(QuizFirstVariable)
# print(QuizSecondVariable)

# -----------------------------------------------------------------------
def MathsQuiz():

    checkUserCondition = input('Continue or exit the quiz (y/n) : ')

    if (checkUserCondition in 'yes') or (checkUserCondition in 'YES') :
        QuizOperator(valueOne = QuizFirstVariable, valueTwo = QuizSecondVariable)
    
    elif (checkUserCondition in 'no') or (checkUserCondition in 'NO'):
        print('Thank you for playing maths quiz, Developer')


if __name__ == "__main__":
    MathsQuiz()
else:
    print('Welcome User To "Developer Quiz Game" ')