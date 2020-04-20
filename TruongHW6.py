'''
    Name: Eric Truong
    ID: 018149311
    Instructor: Minhthong Nguyen
    Date: November 7, 2018
'''
import random

def howmanyLines():
    random.seed()
    looper = random.randint(1, 9)
    return looper

def randomNumbers():
    random.seed()
    x = random.randint(1, 100)
    return x

def homeworkPartOne():
    #create numbers file
    numbers = open('numbers', 'w')

    #write numbers onto file
    looper = howmanyLines()
    for i in range(looper):
        x = randomNumbers()
        x = str(x)
        numbers.write(x)
        numbers.write('\n')

    #close it
    numbers.close()

    #open up numbers file
    file = open('numbers', 'r')

    #make accumulator
    total = 0.0

    #read, total all the numbers, and close the file
    for line in file:
        amount = float(line)
        total += amount
    file.close()

    #calculate average
    total /= looper

    #print calculated average
    print('The average is:', format(total, '.2f'))

def scoreCard():
    nameLine = int(input('How many players?: '))
    counter = 1
    scoreCard = open('scorecard', 'w')
    for i in range(nameLine):
        players = input('Please enter name of player ' + str(counter) + ': ')
        scoreCard.write(players)
        scoreCard.write('\t')
        counter += 1
    scoreCard.write('\n')
    rounds = int(input('How many rounds did you play?: '))
    x = 0
    while (x < rounds):
        counter = 1
        for i in range(nameLine):
            s1 = int(input('Please enter score ' + str(counter) + ': '))
            counter += 1
            s1 = str(s1)
            scoreCard.write(s1)
            scoreCard.write('\t')
        scoreCard.write('\n')
        x += 1
    scoreCard.close()
    file = open('scorecard', 'r')
    file_contents = file.read()
    file.close()
    print(file_contents)
        
        
homeworkPartOne()
scoreCard()
