import random

# Step 3: Calling to operation operator function, and passing in formate operation func
# ----------------------------------------------------------------------------------------------------------
def QuizOperator(valueOne = 0, valueTwo = 0):
    OperationWith = RandomOpeartion()
    print("Question For : {}".format(OperationWith))
    FormateOperation(OperationWith, valueOne, valueTwo)

# Step 4: Randomly seletion for operator from list
# ----------------------------------------------------------------------------------------------------------
def RandomOpeartion():
    randomValueOperation = random.randint(0, 4)
    OperationList = ['addition', 'Substraction', 'Multiplaction', 'Division', 'Mode']
    return OperationList[randomValueOperation]
    
# Step 5: according to condition it print on screen and passing data from user and ans is matching or not
# ----------------------------------------------------------------------------------------------------------
def FormateOperation(operation, valueOne, valueTwo):
    if operation == 'addition':
        AnswerOfQuiz = round(valueOne + valueTwo, 0)

        try:
            userAnswer = float(input('{} + {} = '.format(valueOne, valueTwo)))
            AnswerCheck(AnswerOfQuiz = AnswerOfQuiz, userAnswer = userAnswer)

        except:
            print('\n-- Input in the Floating or Integer --')

        
    elif operation == 'Substraction':
        AnswerOfQuiz = AnswerOfQuiz = round(valueOne - valueTwo, 0)

        try:
            userAnswer = float(input('{} - {} = '.format(valueOne, valueTwo)))
            AnswerCheck(AnswerOfQuiz = AnswerOfQuiz, userAnswer = userAnswer)

        except:
            print('\n-- Input in the Floating or Integer --')

        
    elif operation == 'Multiplaction':
        AnswerOfQuiz = AnswerOfQuiz = round(valueOne * valueTwo, 0)

        try:
            userAnswer = float(input('{} * {} = '.format(valueOne, valueTwo)))
            AnswerCheck(AnswerOfQuiz = AnswerOfQuiz, userAnswer = userAnswer)

        except:
            print('\n-- Input in the Floating or Integer --')
        
        
    elif operation == 'Division':
        
        if valueTwo == 0: 
            valueTwo += 1

        AnswerOfQuiz = round(valueOne / valueTwo, 0)

        try:
            userAnswer = float(input('{} / {} = '.format(valueOne, valueTwo)))
            AnswerCheck(AnswerOfQuiz = AnswerOfQuiz, userAnswer = userAnswer)

        except:
            print('\n-- Input in the Floating or Integer --')

        
    elif operation == 'Mode':
        AnswerOfQuiz = round(valueOne % valueTwo, 0)

        try:
            userAnswer = float(input('{} % {} = '.format(valueOne, valueTwo)))
            AnswerCheck(AnswerOfQuiz = AnswerOfQuiz, userAnswer = userAnswer)

        except:
            print('\n-- Input in the Floating or Integer --')

# Step 6: checking ans is same the increase count and point, else end the quiz
# ----------------------------------------------------------------------------------------------------------
counts = 0; points = 0
def AnswerCheck(userAnswer, AnswerOfQuiz):
    global counts, points
    if userAnswer == AnswerOfQuiz:
        print('Your answer is corrent, Now you can go in next round')
        print()
        counts += 1
        points += 100
        MathsQuiz()

    else:
        print('Oops!, You have not fill proper answer for this question')
        print('Your answer : {} \nCorrect Answer : {}'.format(userAnswer, AnswerOfQuiz))

# Step 2: Generating a list len of 10, between range 0 to 100, and passing to MathQuiz Function
# ----------------------------------------------------------------------------------------------------------
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

# Step 1: Start Execute here, Check Operatior and Condition to Play or Not
# ----------------------------------------------------------------------------------------------------------
def MathsQuiz():

    QuizFirstVariable, QuizSecondVariable  = StartExecute()

    checkUserCondition = input('Continue or exit the quiz (y/n) : ')

    if (checkUserCondition in 'yes') or (checkUserCondition in 'YES') :
        QuizOperator(valueOne = QuizFirstVariable, valueTwo = QuizSecondVariable)
    
    elif (checkUserCondition in 'no') or (checkUserCondition in 'NO'):
        print('Thank you for playing maths quiz, Developer')

# If User Need To Check Point or Count Then Call Directily To The Function
# ----------------------------------------------------------------------------------------------------------
def Points():
    return points

def Counts():
    return counts

# Main Function Will Check Every Time, It Doesnt Matter You Are On Which File. When You Are Executing Quiz.
# ----------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    MathsQuiz()
else:
    print('Welcome User To "Developer Quiz Game" ')