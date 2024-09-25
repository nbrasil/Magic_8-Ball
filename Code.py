import random

print('Hello! Welcome to your online Magic 8-Ball Program.')

while True:
    question = input('What would you like to ask today?  ')
    if question != '':
        random_number = random.randint(1,9)
        print("Magic 8-Ball's answer: ", end='')
        if random_number == 1:
            print('Yes - definitely')
        elif random_number == 2:
            print('It is decidedly so')
        elif random_number == 3:
            print('Without a doubt')
        elif random_number == 4:
            print('Reply hazy, try again')
        elif random_number == 5:
            print('Ask again later')
        elif random_number == 6:
            print('Better not tell you now')
        elif random_number == 7:
            print('My sources say no')
        elif random_number == 8:
            print('Outlook not so good')
        elif random_number == 9:
            print('Very doubtful')
        else:
            print('Error')
    else:
        print('You have to ask me a question to get an answer. Try again!')
        continue

    another_question = input('Would ou like to ask another question?(yes or no)  ')
    if another_question == 'no':
        print('See you soon, bye!')
        break

