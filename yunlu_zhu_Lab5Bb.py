
import random

def guess_game():
    tt = random.randint(1, 1000)
    guess_count = 0
    done = False
    while not done:
        gs = input('Please guess a number: ')
        guess_count += 1
        if gs == tt:
            print 'You rock! You guessed the number in %d tries!!' % guess_count
            done = True
        elif gs > tt:
            if (gs - tt) <= 10:
                print 'Getting warm but still high!'
            else:
                print 'Too high!'
        else:
            if (tt - gs) <= 10:
                print 'Getting warm but still Low!'
            else:
                print 'Too Low!'


def main():
    game_count = 0
    game_stop = False
    random.seed()
    while not game_stop:
        game_count += 1
        guess_game()
        reply = raw_input('Do you want to play again? (y/n)')
        if reply != 'y' and reply != 'Y':
            game_stop = True
    print 'You played %d times' % game_count


if __name__ == '__main__':
    main()
