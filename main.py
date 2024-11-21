# Nuthanan Tharmarajah 
# ICS2O_P2
# Monday, June 21, 2021
# A mathematical software that allows the user to input math equations and the program also has the option to ask questions to the user.
import random

#function generates random two operation equations, that will be used in the trivia
def arithmeticGeneration ():

    #randomly generates 3 integers for the operation
    firstInteger = random.randint(1, 10) 
    secondInteger = random.randint(1, 10)
    thirdInteger = random.randint(1, 10)
    
    arthemticOperations = ["+", "-", "/", "*", "^"]
    twoChoosenArthemeticOperations = random.sample(arthemticOperations, 2) #a sample of the arthemtic operations is choosen

    #here the question is put together based on the random operations
    if twoChoosenArthemeticOperations[0] == "+": # if the first arthemetic operation is a +, it will go through this statement. 
        if twoChoosenArthemeticOperations[1] == "+": #if the second arthemetic operation is a+, it will go through this statement.
            arthemeticQuestion = str(firstInteger) + "+" + str(secondInteger) + "+" + str(thirdInteger) #this line assigns the string that will be displayed to the user
            arthemeticAnswer = firstInteger + secondInteger + thirdInteger #this line will calculate the answer
            #the same thing applies the next few statments. 
        elif twoChoosenArthemeticOperations[1] == "-":
            arthemeticQuestion = str(firstInteger) + "+" + str(secondInteger) + "-" + str(thirdInteger)
            arthemeticAnswer = firstInteger + secondInteger - thirdInteger
        elif twoChoosenArthemeticOperations[1] == "/":
            arthemeticQuestion = str(firstInteger) + "+" + str(secondInteger) + "/" + str(thirdInteger)
            arthemeticAnswer = firstInteger + secondInteger / thirdInteger
        elif twoChoosenArthemeticOperations[1] == "*":
            arthemeticQuestion = str(firstInteger) + "+" + str(secondInteger) + "*" + str(thirdInteger)
            arthemeticAnswer = firstInteger + secondInteger * thirdInteger
        else:
            arthemeticQuestion = str(firstInteger) + "+" + str(secondInteger) + "^" + str(thirdInteger)
            arthemeticAnswer = firstInteger + secondInteger ** thirdInteger
    elif twoChoosenArthemeticOperations[0] == "-":
        if twoChoosenArthemeticOperations[1] == "+":
            arthemeticQuestion = str(firstInteger) + "-" + str(secondInteger) + "+" + str(thirdInteger)
            arthemeticAnswer = firstInteger - secondInteger + thirdInteger
        elif twoChoosenArthemeticOperations[1] == "-":
            arthemeticQuestion = str(firstInteger) + "-" + str(secondInteger) + "-" + str(thirdInteger)
            arthemeticAnswer = firstInteger - secondInteger - thirdInteger
        elif twoChoosenArthemeticOperations[1] == "/":
            arthemeticQuestion = str(firstInteger) + "-" + str(secondInteger) + "/" + str(thirdInteger)
            arthemeticAnswer = firstInteger - secondInteger / thirdInteger
        elif twoChoosenArthemeticOperations[1] == "*":
            arthemeticQuestion = str(firstInteger) + "-" + str(secondInteger) + "*" + str(thirdInteger)
            arthemeticAnswer = firstInteger - secondInteger * thirdInteger
        else: 
            arthemeticQuestion = str(firstInteger) + "-" + str(secondInteger) + "^" + str(thirdInteger)
            arthemeticAnswer = firstInteger - secondInteger ** thirdInteger
    elif twoChoosenArthemeticOperations[0] == "/":
        if twoChoosenArthemeticOperations[1] == "+":
            arthemeticQuestion = str(firstInteger) + "/" + str(secondInteger) + "+" + str(thirdInteger)
            arthemeticAnswer = firstInteger / secondInteger + thirdInteger
        elif twoChoosenArthemeticOperations[1] == "-":
            arthemeticQuestion = str(firstInteger) + "/" + str(secondInteger) + "-" + str(thirdInteger)
            arthemeticAnswer = firstInteger / secondInteger - thirdInteger
        elif twoChoosenArthemeticOperations[1] == "/":
            arthemeticQuestion = str(firstInteger) + "/" + str(secondInteger) + "/" + str(thirdInteger)
            arthemeticAnswer = firstInteger / secondInteger / thirdInteger
        elif twoChoosenArthemeticOperations[1] == "*":
            arthemeticQuestion = str(firstInteger) + "/" + str(secondInteger) + "*" + str(thirdInteger)
            arthemeticAnswer = firstInteger / secondInteger * thirdInteger
        else: 
            arthemeticQuestion = str(firstInteger) + "/" + str(secondInteger) + "^" + str(thirdInteger)
            arthemeticAnswer = firstInteger /secondInteger ** thirdInteger
    elif twoChoosenArthemeticOperations[0] == "*":
        if twoChoosenArthemeticOperations[1] == "+":
            arthemeticQuestion = str(firstInteger) + "*" + str(secondInteger) + "+" + str(thirdInteger)
            arthemeticAnswer = firstInteger * secondInteger + thirdInteger
        elif twoChoosenArthemeticOperations[1] == "-":
            arthemeticQuestion = str(firstInteger) + "*" + str(secondInteger) + "-" + str(thirdInteger)
            arthemeticAnswer = firstInteger * secondInteger - thirdInteger
        elif twoChoosenArthemeticOperations[1] == "/":
            arthemeticQuestion = str(firstInteger) + "*" + str(secondInteger) + "/" + str(thirdInteger)
            arthemeticAnswer = firstInteger * secondInteger / thirdInteger
        elif twoChoosenArthemeticOperations[1] == "*":
            arthemeticQuestion = str(firstInteger) + "*" + str(secondInteger) + "*" + str(thirdInteger)
            arthemeticAnswer = firstInteger * secondInteger * thirdInteger
        else: 
            arthemeticQuestion = str(firstInteger) + "*" + str(secondInteger) + "^" + str(thirdInteger)
            arthemeticAnswer = firstInteger * secondInteger ** thirdInteger
    elif twoChoosenArthemeticOperations[0] == "^":
        if twoChoosenArthemeticOperations[1] == "+":
            arthemeticQuestion = str(firstInteger) + "^" + str(secondInteger) + "+" + str(thirdInteger)
            arthemeticAnswer = firstInteger ** secondInteger + thirdInteger
        elif twoChoosenArthemeticOperations[1] == "-":
            arthemeticQuestion = str(firstInteger) + "^" + str(secondInteger) + "-" + str(thirdInteger)
            arthemeticAnswer = firstInteger ** secondInteger - thirdInteger
        elif twoChoosenArthemeticOperations[1] == "/":
            arthemeticQuestion = str(firstInteger) + "^" + str(secondInteger) + "/" + str(thirdInteger)
            arthemeticAnswer = firstInteger ** secondInteger / thirdInteger
        elif twoChoosenArthemeticOperations[1] == "*":
            arthemeticQuestion = str(firstInteger) + "^" + str(secondInteger) + "*" + str(thirdInteger)
            arthemeticAnswer = firstInteger ** secondInteger * thirdInteger
        else: 
            arthemeticQuestion = str(firstInteger) + "^" + str(secondInteger) + "^" + str(thirdInteger)
            arthemeticAnswer = firstInteger ** secondInteger ** thirdInteger

    #if the answer is a float, we have to round the answer by two
    arthemeticAnswer = round(arthemeticAnswer, 2)
    arthemeticList = [arthemeticQuestion, arthemeticAnswer]
    return arthemeticList

#this function generates a random set, and finds the median 
def randomMedianSetGenerator():
    howManyNumber = random.randint(4,10) #generates a number between 4 and 10 finding how much numbers are going to be in the set
    numberSet = [] 
    choices = 0
    #the following while loop will append a random number between 1 and 20, and append the amount of numbers the random generation made up
    while choices < howManyNumber:
        integer = random.randint(1, 20)
        numberSet.append(integer)
        choices += 1

    correctSet = [] #here is the set that will be in chronological order
    index = 0
    number = 1
    #the following while loop takes the index, less than the overall length of number set, goes through every element and checks if its 1, if not, it adds 1, and reurns the loop, after this, it will continue going through the loop until every number has been placed
    while index < len(numberSet) and number < 21:
        #here it checks if the index is equal to the number, if so it will append that number into the correct list
        if numberSet[index] == number:
            correctSet.append(numberSet[index])
        index += 1
        #when the index equals the length of the number set, and the number is less than 20, the index resets, and the number gets added by one
        if index == len(numberSet) and number < 20:
            index = 0
            number += 1 
    dividedBy2 = howManyNumber//2 #the following number is where the middle number will be
    if howManyNumber % 2 == 0: #if the items in the list is an even number, it will go through this code.
        #here it will take the two middle numbers, sum those two up, divide them by two, and we have our median
        medianNumber1 = correctSet[dividedBy2] 
        medianNumber2 = correctSet[dividedBy2 - 1]
        medianNumber = (medianNumber1 + medianNumber2)/2

    else: #if the number is odd, our lives are way more easier, we simply have to get the middle number using dividedBy2
        medianNumber = correctSet[dividedBy2]

    medianList = [numberSet, medianNumber]
    return medianList

#this function creates a random percentage question for our trivia game
def randomPercentageGenerator():

    #here we have two lists full of numbers, that will be used to make our percentage questions, as you can already tell, the percentages are divisible by 5 and the numbers are divisible by 10, making it easier for the user
    arrayPercentages = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95] 
    arrayNumbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    #here it selects one random item from each of the two lists
    randomPercent = random.choice(arrayPercentages)
    randomNumber = random.choice(arrayNumbers)

    #then it calculates the answer to the question
    percentAnswer = (randomPercent/100)*randomNumber

    percentList = [randomPercent, randomNumber, percentAnswer]
    return percentList

#this function generates a random algebra question for our game
def randomAlgebraQuestionGenerator():
    #here we generate the coefficents of the x variable and the y variable
    xValue = random.randint(1, 20)
    yIntValue = random.randint(-20, 20)

    #since we are always going to be in standard form, we have to divide the yInt value by -1, in order to indicate we flipped the sign
    algebraAnswer = yIntValue//-1

    algebraList = [xValue, yIntValue, algebraAnswer]
    return algebraList


#Introduction
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Welcome to the Math Trivia and Calculator! \n")  
userWantedNumber = 0

while userWantedNumber != 3:
    print("Enter 1 for Math Trivia")
    print("Enter 2 for Math Calculator")
    print("Enter 3 to Exit \n")

    userWantedNumber = int(input("What would you like to do: ")) #here is where it asks the user what they would like to do 

    while userWantedNumber != 1 and userWantedNumber != 2 and userWantedNumber != 3: #here it checks if the number is invalid
        print("That is an invalid number!")
        userWantedNumber = int(input("What would you like to do: \n"))

    exitString = "yes"

    while userWantedNumber == 1 and exitString != "no": #if the user entered one, or the user wanted to play again, it will lead them to this while loop
        #Instructions are printed below
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print()
        print("Welcome to the Math Trivia! Before we begin, here are the instructions!")
        print()
        print("1. You will be asked multiple questions, based on how much questions of each strand you would like!")
        print("2. You will then answer the questions, and based on your answer you will recieve a certain amount of points")
        print("3. In front of each question, will be the strand that your question is from. If it is: ")
        print("\t a) Calculation: the answer will always be an integer or decimal value (in the event that it is a decimal, please round to two decimal places)")
        print("\t b) Theory: The answer will always be one or two words, but one question is an integer value.")
        print("\t c) True or False: The answer will either be True or False, there is no other phrase that can go with this, otherwise our system will detect it wrong")
        print("4. For ONLY THEORY questions, you may enter hint into the input, and it will give you a hint, no points will be deducted.")
        print("5. The scoring system for this trivia is very simple. Here is how you can score your points: ")
        print("\t a) Getting an answer correct will give you one point.")
        print("\t b) Getting an answer incorrect will give you zero points.")
        print("\t c) Typing a theory answer correctly, but the program detects a typo, will give you 0.5 points.")
        print()
        print("We hope you have fun with our trivia game!")
        print()
        input("PRESS ENTER TO CONTINUE: ") 
        
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        #here it runs the functions that we established at the beginning of the code, and assigns it to different variables
        arthemeticList = arithmeticGeneration()
        medianList = randomMedianSetGenerator()
        percentList = randomPercentageGenerator()
        algebraList = randomAlgebraQuestionGenerator()
        print("Before we begin the trivia, how many questions of each strand would you like to ask? We have 5 questions for each strand. \n")

        #here we ask the user how many questions of each strand, the maximum amount of questions we have for each strand is 5
        calculationNumber = int(input("Calculations: "))
        #this while loops following, checks if the number is greater than 5, in which is will ask the user to enter another number
        while calculationNumber > 5:
            print("That number is greater than the amount of questions we have! Try again")
            calculationNumber = int(input("Calculations: "))

        theoryNumber = int(input("Theory: "))
        while theoryNumber > 5:
            print("That number is greater than the amount of questions we have! Try again")
            theoryNumber = int(input("Theory: "))

        trueAndFalseNumber = int(input("True and False: "))
        while trueAndFalseNumber > 5:
            print("That number is greater than the amount of questions we have! Try again")
            trueAndFalseNumber = int(input("True and False: "))

        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        #below, we have our lists for the questions and answers for every strand, and the hints for the theory
        calculationQuestions = ["What is " + str(percentList[0]) + "% of " + str(percentList[1]), arthemeticList[0] , "What is the median of this set: " + str(medianList[0]), "What is the y-intercept is the equation: " + str(algebraList[0]) + "x + y + (" + str(algebraList[1]) + ") = 0", "10^x = 1000. What is the value of x?"]
        calculationAnswers = [percentList[2], arthemeticList[1], medianList[1], algebraList[2], 3]
        theoryQuestions = ["Who was the founder of a^2 + b^2 = c^2?", "A number with only two factors is called what?", "1, 1, 2, 3, 5, 8, 13, 21. What is this set called?", "What topic uses letters and numbers to manipulate various equations?", "What quadrant number is the top left square of the Cartesian Plane? (Note, although theory, this answer is an integer)"]
        theoryAnswers = ["pythagoras", "prime number", "fibonacci sequence", "algebra", 2]
        hintForTheory = ["This person is a Greek mathematician ", "A number with more than two factors is composite.", "The first word is an Italian Mathematician.", "The word starts with an A", "The top right quadrant is 1."]
        trueAndFalseQuestions = ["True or False: Are all quadrilaterals regular?", "True or False: The third term in (x + 2)^2 = 25", "True or False: Pi (3.14159265....) is calculated by dividing the circumference of the circle by the radius?", "True or False: The International System of Units uses inches instead of meters?", "True or False: y = x^2 is a quadratic equation"]
        trueAndFalseAnswers = ["false", "true", "false", "false", "true"]

        questions = [] #here is our final list of all the questions
        answers = [] #here is our final list of all of our answers 
        hint = [] #here is the amount of hints we should have

        furthestIndex = len(calculationQuestions) - 1 
        numberIndex = 0
        #this while loop, appends the amount of calculation questions the user wants, it first checks if the numberIndex is less than the amount of calculation questions the user asked, if so, it will run the while loop
        while numberIndex < calculationNumber:
            randomIndex = random.randint(0, furthestIndex) #here, it will identify the furthest index, and generate a random number to append to the questions list
            questions.append(calculationQuestions[randomIndex]) #here it appends the question using the random index
            del calculationQuestions[randomIndex] #it then deletes the question from the original list
            # same thing applies from the questions
            answers.append(calculationAnswers[randomIndex])
            del calculationAnswers[randomIndex]
            numberIndex += 1
            furthestIndex -= 1 #the furthest index then gets subtracted by 1, as when we delete something from the list, the index will become smaller

        #the same while loops apply for the while loop in the theory and the true and false questions

        furthestIndex = len(theoryQuestions) - 1 
        numberIndex = 0
        while numberIndex < theoryNumber:
            randomIndex = random.randint(0, furthestIndex)
            questions.append(theoryQuestions[randomIndex]) 
            del theoryQuestions[randomIndex]
            answers.append(theoryAnswers[randomIndex])
            del theoryAnswers[randomIndex]
            hint.append(hintForTheory[randomIndex])
            del hintForTheory[randomIndex]
            numberIndex += 1
            furthestIndex -= 1

        furthestIndex = len(trueAndFalseQuestions) - 1 
        numberIndex = 0
        while numberIndex < trueAndFalseNumber:
            randomIndex = random.randint(0, furthestIndex)
            questions.append(trueAndFalseQuestions[randomIndex]) 
            del trueAndFalseQuestions[randomIndex]
            answers.append(trueAndFalseAnswers[randomIndex])
            del trueAndFalseAnswers[randomIndex]
            numberIndex += 1
            furthestIndex -= 1

        #here, we have our storylines that will keep the trivia engaging
        storyLine1 = "You are about to enter a 1 million dollar game then, the judge asks you a few questions, you must answer."
        storyLine2 = "You are currently working at a top secret agency. Your boss wants to give you a promotion however, you must answer a few math questions to get there. Good luck agent!"
        storyLine3 = "You are currently in a huge battle, to save the Earth, between you and the Math Lord. To save the world you must answer a few math questions to hit your boss, but be careful, getting a question wrong can be damaging! Your goal is to either kill the boss, or wait for you sidekick to come and finish the job!"

        storyLineNumber = random.randint(1,3) #here, the program generates a random number, that will be used to generate the storyLine

        if storyLineNumber == 1:
            storyLine = storyLine1
        elif storyLineNumber == 2:
            storyLine = storyLine2
        else:
            storyLine = storyLine3

        print("Perfect! Generating questions and story! A reminder to round to two decimal places if neccesary!")
        print()
        print(storyLine)
        if storyLineNumber == 3:
            print()
            print("The math lord currently has " + str(len(questions) * 6) + " HP")
            currentHP = len(questions) * 6

        index = 0
        score = 0
        totalQuestions = 0
        hintIndex = 0
        userAnswer = " "
        amountOfHintsUsed = 0 
        while index < len(questions): #here our trivia begins asking the questions, and it goes through the while loop asking all the questions in the questions and answers lists
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("Question Number ", index + 1, ": \n")
            if index < calculationNumber: #here the if statements checks if the index is less than the calculation number and prints out that the question is a calculation question
                print("This question is a calculation question.")
            elif index > calculationNumber - 1 and index < calculationNumber + theoryNumber: #this statement checks if the index is greater than the calculation number, but less than the calculation and theory number, therefore making it a theory question
                print("This question is a theory question. ")
            else: #in any other scenarios, the program will now that its a true and false question
                print("This question is a true and false question.") 
            print(questions[index]) #the program the prints the question from the list
            print()

            hintUsed = False
            userAnswer = input("Enter answer: ") #here the user can enter the answer 

            #here, the program will covert the user input, into different types of data types
            if isinstance(answers[index], int): 
               intIndex = 0
               howManyIntegers = 0
               #this while loop checks if the string is all digits and depending on if it is, it will convert the string into an integer
               while intIndex < len(userAnswer):
                   #below, it checks if the index is equal to any, or if its a negative
                   if userAnswer[intIndex] == "1" or userAnswer[intIndex] == "2" or userAnswer[intIndex] == "3" or userAnswer[intIndex] == "4" or userAnswer[intIndex] == "5" or userAnswer[intIndex] == "6" or userAnswer[intIndex] == "7" or userAnswer[intIndex] == "8" or userAnswer[intIndex] == "9" or userAnswer[intIndex] == "0" or userAnswer[intIndex] == "-":
                       howManyIntegers += 1
                   intIndex += 1 #adds one to the loop, resulting it in checking again
               if howManyIntegers == len(userAnswer): #if all are integers, it will be equal to the length of the user answer, converting it to an integer
                   userAnswer = int(userAnswer) 
            if isinstance(answers[index], bool):
                userAnswer = str(userAnswer) 
            if isinstance(answers[index], str):
                userAnswer = userAnswer.lower()
            if isinstance(answers[index], float) and userAnswer != "hint":
                intIndex = 0
                howManyIntegers = 0 
                while intIndex < len(userAnswer):
                   #same principles as the integer 
                   if userAnswer[intIndex] == "1" or userAnswer[intIndex] == "2" or userAnswer[intIndex] == "3" or userAnswer[intIndex] == "4" or userAnswer[intIndex] == "5" or userAnswer[intIndex] == "6" or userAnswer[intIndex] == "7" or userAnswer[intIndex] == "8" or userAnswer[intIndex] == "9" or userAnswer[intIndex] == "0" or userAnswer[intIndex] == "-" or userAnswer[intIndex] == ".":
                       howManyIntegers += 1
                   intIndex += 1  
                if howManyIntegers == len(userAnswer):
                    userAnswer = float(userAnswer)

            #in the event that the user enters hint, into the answer, the program will understand and try to provide a hint 
            if userAnswer == "hint":
                while userAnswer == "hint":
                    #since, hints are only applicable to theory questions, the program has to identify that the answer it is a theory statement through these statements
                    if isinstance(answers[index], str) and answers[index] != "true" and answers[index] != "false" and not hintUsed or answers[index] == 2:
                        print(hint[hintIndex]) #first the program prints the hint out
                        hintUsed = True #here, it sets the boolean to true, so that the hint doesn't get displayed again. 
                        print()
                        amountOfHintsUsed += 1 #adds one to hint used
                    #in the event the answer isnt a string, however an integer, float or a boolean, it will print something. letting the user know that they can use a hint
                    elif isinstance(answers[index], int) or isinstance(answers[index], float) or answers[index] == "true" or answers[index] == "false":
                        print("Unfortunately, because your answer is an integer, decimal or True or False, we cannot give you a hint :(")
                        print()
                    elif hintUsed: #finally, in the event that the hint is used, it prints out, letting them know that a hint has been used
                        print("You used a hint already!")
                        print()

                    userAnswer = input("Enter answer: ")
                    if isinstance(answers[index], int): 
                       intIndex = 0
                       howManyIntegers = 0
                       while intIndex < len(userAnswer):
                           if userAnswer[intIndex] == "1" or userAnswer[intIndex] == "2" or userAnswer[intIndex] == "3" or userAnswer[intIndex] == "4" or userAnswer[intIndex] == "5" or userAnswer[intIndex] == "6" or userAnswer[intIndex] == "7" or userAnswer[intIndex] == "8" or userAnswer[intIndex] == "9" or userAnswer[intIndex] == "0" or userAnswer[intIndex] == "-":
                               howManyIntegers += 1
                           intIndex += 1 
                       if howManyIntegers == len(userAnswer):
                           userAnswer = int(userAnswer) 
                    if isinstance(answers[index], bool):
                        userAnswer = str(userAnswer) 
                    if isinstance(answers[index], str):
                        userAnswer = userAnswer.lower()
                    if isinstance(answers[index], float) and userAnswer != "hint":
                        intIndex = 0
                        howManyIntegers = 0 
                        while intIndex < len(userAnswer):
                           if userAnswer[intIndex] == "1" or userAnswer[intIndex] == "2" or userAnswer[intIndex] == "3" or userAnswer[intIndex] == "4" or userAnswer[intIndex] == "5" or userAnswer[intIndex] == "6" or userAnswer[intIndex] == "7" or userAnswer[intIndex] == "8" or userAnswer[intIndex] == "9" or userAnswer[intIndex] == "0" or userAnswer[intIndex] == "-" or userAnswer[intIndex]:
                               howManyIntegers += 1
                           intIndex += 1  
                        if howManyIntegers == len(userAnswer):
                            userAnswer = float(userAnswer)
                            
            #here, it checks that if the answer is a string, and not an int, float or a boolean, it adds one to the hint index
            if isinstance(answers[index], str) and answers[index] != "true" and answers[index] != "false" or answers[index] == 2:
                hintIndex += 1 

            print() 

            #this if statement checks if the answer that the user entered is the same as the answer
            if answers[index] == userAnswer:
                if storyLineNumber == 3: #when the story line is 3, there is a bit more text, to make the game more fun and engaging
                    currentHP -= 6
                    randomDialogueNumber = random.randint(1,3)
                    if randomDialogueNumber == 1:
                        print("AHHHHH! STOP USING YOUR MATH POWERS!")
                    elif randomDialogueNumber == 2 and currentHP > (len(questions)*6)/2:
                        print("That didn't even hurt me :)")
                    else:
                        print("ACKKKK")
                    print()
                    print("The boss now has " + str(currentHP) + "HP")

                #Here they make remarks about whether you got the question correct   
                print("Correct! You have earned one point!")
                #Here we add one to the score if the user got one correct, and to the total questions
                score += 1 
                totalQuestions += 1
                print("Your current score is ", score, "/", totalQuestions) #Prints out score
            elif isinstance(answers[index], str): #For theory questions only, you are allowed to have typos, and this statement will check if there are any typos 
                stringArray = []
                answerArray = []
                index2 = 0
                #Here, the program appends every character in the user answer
                while index2 < len(userAnswer):
                    stringArray.append(userAnswer[index2])
                    index2 += 1 

                index2 = 0
                #the program also appends every character in the answer
                while index2 < len(answers[index]):
                    answerArray.append(answers[index][index2])
                    index2 += 1 

                #in the event that the lengths of both arrays are different, it will append different items, so that when comparing, it will mark it as wrong
                while len(stringArray) != len(answerArray):
                    if len(stringArray) > len(answerArray):
                        answerArray.append("error")
                    elif len(answerArray) > len(stringArray):
                        stringArray.append("error") 

                index2 = 0
                similar = 0
                #here the index will compare the two arrays, and if they are similar, one point will be added
                while index2 < len(stringArray):
                    if stringArray[index2] == answerArray[index2]:
                        similar += 1
                    index2 += 1

                print(similar)

                #if half of the characters are correct, it will detect it as a typo, and as a result will give you .5
                if similar >= len(answers[index])/2:
                    if storyLineNumber == 3:
                        print ("That was like a little pinch to me")
                        currentHP -= 3
                        print("The boss now has " + str(currentHP) + "HP")
                    print("I think you had a typo! We will give you half marks for that! The correct answer was: ", answers[index])
                    totalQuestions += 1
                    score += 0.5
                    print("Your current score is ", score, "/", totalQuestions)
                else: #in the event that you did get it wrong and it went through this statement, you will get no points
                    if storyLineNumber == 3:
                        print("AHAHAHHAHA YOU MISSED!")
                        print ("The boss still has " + str(currentHP) + " HP")
                    print("Incorrect! The correct answer is: ", answers[index])
                    totalQuestions += 1
                    print("Your current score is ", score, "/", totalQuestions)
            
            else: #finally, if the answer was an int, boolean, or float, the program will mark it as wrong. 
                if storyLineNumber == 3:
                    print("AHAHAHHAHA YOU MISSED!")
                    print ("The boss still has " + str(currentHP) + " HP")
                print("Incorrect! The correct answer is: ", answers[index])
                totalQuestions += 1
                print("Your current score is ", score, "/", totalQuestions)

            print()
            index += 1 #the index is added again, and the while loop continues 

        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print()
        #here our final score is displayed
        print("Your final score is ", score, "/", totalQuestions)
        totalPercentage = round((score/totalQuestions) * 100, 2) 
        print("In percentage: ", totalPercentage, "%")
        #depending on the amount of hints used, feedback will be provided, in these if statements
        if amountOfHintsUsed == 0:
            print("AMAZING! You used no hints! You are one true mathematician :D!")
        elif amountOfHintsUsed < 2:
            print("Great work! You used less than 2 hints! You are almost there to perfecting your mathematical skills!")
        elif amountOfHintsUsed == 3:
            print("Nice! You used 3 hints! You should continue practicing to force yourself to not use hints!")
        else:
            print("Nice Try! You used less than 6 hints! You should start using less hints and trying to guess :)")
        print()

        #based on the story line, if you got a passing grade and not a 100%, feedback is given 
        if totalPercentage > 50 and totalPercentage != 100:
            if storyLineNumber == 1:
                print("Based on your score, YOU HAVE WON A MILLION DOLLARS!")
            elif storyLineNumber == 2:
                print("Congrats! Based on your score, we are pleased to give you your promotion :)")
            else:
                print("You have defeated the boss, as your sidekick arrived and finished the job! Great work!")
        #based on the story line, if you got a 100%, you will get a special ending
        elif totalPercentage == 100:
            if storyLineNumber == 1:
                print("Based on your score, YOU HAVE WON A MILLION DOLLARS! Not just that, but you will also get another $10,000 for getting every answer correct!")
            elif storyLineNumber == 2:
                print("Congrats! Based on your score, we are pleased to give not the promotion, however the company, since you answered every question correctly!")
            else:
                print("Your sidekick arrives, but he sees that you have already defeated the monster with your amazing math skills :)")
        #finally, if you failed, you will be given feedback, however, this forces you to work even harder
        else:
            if storyLineNumber == 1:
                print("Unfournately, you have not won the million dollars due to your failing score D:")
            elif storyLineNumber == 2:
                print("You were fired from the job because of the lack of math skills you had done during your promotion test")
            else:
                print("Your sidekick arrives, but as he tried defeating the boss, he ran away because of his high levels of HP, your organization, fired you.")
            
        print()

        exitString = " "
        #the following while loop allows the user to play again, or to leave
        while exitString != "yes" and exitString != "no": 
            exitString = input("Would you like to play again: ")
            exitString = exitString.lower()
            #if the exit string says yes or no, or if it couldn't detect what the input was, feedback will be provided accordingly
            if exitString == "yes":
                print("Perfect!")
            elif exitString == "no":
                print("Okay! Going back to the main menu!")
            else:
                print("That is an invalid string! Try again!")

            print()


    #here we have our calculator part of the code
    while userWantedNumber == 2 and exitString != "no": #the following while loop checks if the user wanted a Calculator or the user wants to play again.
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("What type of calculation would you like? \n")
        userCalculationNumber = 0
        while userCalculationNumber != 1 and userCalculationNumber != 2: #Here, the user will input what they want based on the options given
            print("1 - Arthemtic  Operations ")
            print("2 - Percentage of a Number \n") 
            userCalculationNumber = int(input("What would you like to do: "))
            #program gives feedback if entered an invalid number
            if userCalculationNumber != 1 and userCalculationNumber != 2:
                print("That is an invalid number! Try again!")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        #if the user inputs that the calculation number they want is 1, it will go through this part of the calculator
        if userCalculationNumber == 1:
            #here are they instructions for the calculator
            print("Perfect! To indicate what operations you would like, please enter using these symbols, otherwise an error will occur! \n")
            print("+ --> Addition")
            print("- --> Subtraction")
            print("* --> Multiplicaiton")
            print("/ --> Division")
            print("^ --> Exponent \n")
            
            expression = input("Space out your number and the operation type! Remember to use the proper expression symbols! Enter your expression here: ") #here the user 

            index = 0
            expressionList = []
            while index < len(expression):
                if expression[index] != " ": #if there are any spaces, the if statement will not append the space
                    expressionList.append(expression[index])
                index += 1
                currentIndex = len(expressionList) - 1
                
                if len(expressionList) > 1 and index < len(expression) + 1: #if the expessionList's length is greater than 1, and the index is less than the expression + 1, it will run the code below
                    #the code below checks if there are any symbols on the index and before, if not, there are two integers, that we need to combine
                    if expressionList[currentIndex] != '+' and expressionList[currentIndex] != '-' and expressionList[currentIndex] != '*' and expressionList[currentIndex] != '/' and expressionList[currentIndex] != '^' and expressionList[currentIndex - 1] != '+' and expressionList[currentIndex - 1] != '-' and expressionList[currentIndex - 1] != '*' and expressionList[currentIndex - 1] != '/' and expressionList[currentIndex - 1] != '^':
                        currentIndex = len(expressionList) - 2 
                        fullNumber = expressionList[currentIndex] + expressionList[currentIndex + 1] #since the integers are strings, we can add both strings to concatanate
                        expressionList.append(fullNumber) #it then appends the full number to the list, instead of just a few integers
                        #then it deletes the number that it replaced
                        del expressionList[currentIndex]
                        del expressionList[currentIndex]
                    


                
            index = 1
            operationTypes = []
            #this while loop appends the different operation types that it can identify into one list
            while index < len(expressionList):
                #here it takes the operation 
                currentOperation = expressionList[index]
                if currentOperation == "+": #if the operation is a +, the program will append + into the operation list and delete the + in the list
                    operationTypes.append("+")
                    del expressionList[index]
                elif currentOperation == "-":
                    operationTypes.append("-")
                    del expressionList[index]
                elif currentOperation == "*":
                    operationTypes.append("*")
                    del expressionList[index]
                elif currentOperation == "/":
                    operationTypes.append("/")
                    del expressionList[index]
                else:
                    operationTypes.append("**")
                    del expressionList[index]
                index += 1

            while "**" in operationTypes: #the program then runs the while if an exponent is in the operation types
                if "**" in  operationTypes: 
                    currentOperationIndex = operationTypes.index("**") #the program first identifies where the index is so that it can use it to get the integers 
                    del operationTypes[currentOperationIndex] #then the operation gets deleted
                    firstInteger = float(expressionList[currentOperationIndex]) #then the first integer is found
                    secondInteger = float(expressionList[currentOperationIndex + 1]) #and then the second integer is identified
                    #both integers are then deleted
                    del expressionList[currentOperationIndex]
                    del expressionList[currentOperationIndex]
                    answer = firstInteger ** secondInteger #the answer is then calculated and appended back into the expressionList
                    expressionList.insert(currentOperationIndex, answer)

                    #the same applies to the rest of the operations, however there are some special cases that we should take note of

                    
            while "*" in operationTypes or "/" in operationTypes: #since multiplication and division can occur in any order, we have to figure out which symbol comes first
                if "/" in operationTypes or "*" in operationTypes:
                    if "*" in operationTypes: #here the program checks if there is a multiplication sign in the list if not, it assigns a number that is one greater than the index
                        current1stOperationIndex = operationTypes.index("*")
                    else:
                        current1stOperationIndex = len(expression) + 1
                    if "/" in operationTypes: #the same thing in the multiplication applies to the division
                        current2ndOperationIndex = operationTypes.index("/")
                    else:
                        current2ndOperationIndex = len(expression) + 1

                    if current1stOperationIndex < current2ndOperationIndex: #then comparisons are made between the two index's, and depending on which is less, it will perform the calculations similar to the exponent
                        del operationTypes[current1stOperationIndex]
                        firstInteger = float(expressionList[current1stOperationIndex])
                        secondInteger = float(expressionList[current1stOperationIndex + 1])
                        del expressionList[current1stOperationIndex]
                        del expressionList[current1stOperationIndex]
                        answer = firstInteger * secondInteger
                        expressionList.insert(current1stOperationIndex, answer)

                    else: #if the division index is less than the multiplication index, it will perform the division index first
                        del operationTypes[current2ndOperationIndex]
                        firstInteger = float(expressionList[current2ndOperationIndex])
                        secondInteger = float(expressionList[current2ndOperationIndex + 1])
                        del expressionList[current2ndOperationIndex]
                        del expressionList[current2ndOperationIndex]
                        answer = firstInteger/ secondInteger
                        expressionList.insert(current2ndOperationIndex, answer)


            while "+" in operationTypes or "-" in operationTypes: #the same principles from the multiplication and division are also applied to this portion of the code
                if "+" in operationTypes or "-" in operationTypes:
                    if "+" in operationTypes:
                        current1stOperationIndex = operationTypes.index("+")
                    else:
                        current1stOperationIndex = 10000
                    if "-" in operationTypes:
                        current2ndOperationIndex = operationTypes.index("-")
                    else:
                        current2ndOperationIndex = 10000

                    if current1stOperationIndex < current2ndOperationIndex:
                        del operationTypes[current1stOperationIndex]
                        firstInteger = float(expressionList[current1stOperationIndex])
                        secondInteger = float(expressionList[current1stOperationIndex + 1])
                        del expressionList[current1stOperationIndex]
                        del expressionList[current1stOperationIndex]
                        answer = firstInteger + secondInteger
                        expressionList.insert(current1stOperationIndex, answer)

                    else:
                        del operationTypes[current2ndOperationIndex]
                        firstInteger = float(expressionList[current2ndOperationIndex])
                        secondInteger = float(expressionList[current2ndOperationIndex + 1])
                        del expressionList[current2ndOperationIndex]
                        del expressionList[current2ndOperationIndex]
                        answer = firstInteger - secondInteger
                        expressionList.insert(current2ndOperationIndex, answer)

             
            print()
            print("Answer is: ", round(expressionList[0], 2)) #in the end, the program will have one final answer which will be in the list as the first number
            print()

            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

            exitString = " " 
            while exitString != "yes" and exitString != "no": #this is our exit while loop, similar to our trivia 
                exitString = input("Would you like to play again: ")
                exitString = exitString.lower() 
                if exitString == "yes":
                    print("Perfect!")
                    print()
                elif exitString == "no":
                    print("Okay! Going back to the main menu!")
                    print()
                else:
                    print("That is an invalid string! Try again!")

                    
        if userCalculationNumber == 2: #if the user wanted to choose the percentage of calculator, the code will immediately skip to this part
            print()
            expression = input("Enter your percentage expression! Make sure to use the of between the percent and number! Example: 20% of 50. Enter here: ") #here the user can input the question that they have  
            
            index = 0
            expressionList = []
            while index < len(expression): #here, the expression is appended into the list one by one
                if expression[index] != " ": #the program will avoid the spaces that the program might have
                    expressionList.append(expression[index])
                index += 1
                currentIndex = len(expressionList) - 1
                
                if len(expressionList) > 1 and index < len(expression) + 1: #similar concept to the arthemetic operation calculator, it checks if the expresionList is greater than 1 and the index is less than the length of the expression plus 1
                    if expressionList[currentIndex] != 'o' and expressionList[currentIndex] != 'f' and expressionList[currentIndex] != '%' and expressionList[currentIndex - 1] != 'o' and expressionList[currentIndex - 1] != 'f' and expressionList[currentIndex - 1] != '%': #in the event that the number and the percentages, are more than one digit, the program checks to make sure that the two indexes are not symbols, and they can be numeric values
                        currentIndex = len(expressionList) - 2 
                        fullNumber = expressionList[currentIndex] + expressionList[currentIndex + 1] #since the number is still an string, we canc oncatanate both strings to form a multiple digit number
                        expressionList.append(fullNumber) 
                        del expressionList[currentIndex]
                        del expressionList[currentIndex]
                    

            percentageAsDecimal = float(expressionList[0])/100 #here we convert the percentage into a decimal, so that the number can be performed calculations on
            finalAnswer = float(expressionList[len(expressionList) - 1])*percentageAsDecimal #the final answer is made from these calculations

            print() 
            print(expressionList[0], "% of", expressionList[len(expressionList) - 1] , "is", round(finalAnswer, 2), "\n") #here the user will see the answer to their issue

            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            
            exitString = " " 
            while exitString != "yes" and exitString != "no": #the exit or play again while loop
                exitString = input("Would you like to play again: ")
                exitString = exitString.lower() 
                if exitString == "yes":
                    print("Perfect!")
                    print()
                elif exitString == "no":
                    print("Okay! Going back to the main menu!")
                    print()
                else:
                    print("That is an invalid string! Try again!")



print("Have a great rest of your day!") #final remarks, if the user wanted to exit
