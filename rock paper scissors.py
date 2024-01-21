import random
import time

winning_score = 10
cscore = 0
score = 0
round = 1

while True:
    print('Round '+str(round))
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
            score = score + 1
            cscore = cscore + 1
            print('Its a tie!')

        elif (answer == 'Rock' and comp_answer == 'Scissors') or \
                (answer == 'Scissors' and comp_answer == 'Paper') or \
                (answer == 'Paper' and comp_answer == 'Rock'):
            print('You win!')
            score = score + 1

        else:
            cscore = cscore + 1
            print('You lose.')

    print('Your score is '+str(score))
    print('Computer score is ' + str(cscore))
    round = round + 1


    if score == winning_score and cscore == winning_score:
        print('You and the computer win the game at a draw!')
        break
    elif score == winning_score:
        print('You win the game!')
        break
    elif cscore == winning_score:
        print('Computer wins the game...')
        break
    else:
        play_again = input('Next round? Y/N: ')
        if play_again != 'Y':
            break
