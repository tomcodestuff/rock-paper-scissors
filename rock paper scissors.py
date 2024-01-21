import random
import time


while True:
    for x in ('Rock','Paper','Scissors','Shoot!'):
        print(x)
        time.sleep(1)

    game = ('Rock','Paper','Scissors')
    comp_answer = random.choice(game)

    answer = input('Answer: ')

    if answer != 'Rock' and answer != 'Paper' and answer != 'Scissors':
        print('You must enter a viable answer. Make sure it is a capital.')

    else:
        print('You selected {} and the computer selected {}.'.format(answer,comp_answer))
        time.sleep(0.5)
        print('This means...')
        time.sleep(0.5)

        if answer == comp_answer:
            print('Its a tie!')

        elif (answer == 'Rock' and comp_answer == 'Scissors') or \
                (answer == 'Scissors' and comp_answer == 'Paper') or \
                (answer == 'Paper' and comp_answer == 'Rock'):
            print('You win!')

        else:
            print('You lose.')

    play_again = input('Play again? Y/N: ')
    if play_again != 'Y':
        break
