
import random

def guessinggame():
    guessnumber = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input('guess a number from 1 - 100:'))
            attempts += 1
            if guess < guessnumber:
                print('higher than this! try again.')
            elif guess > guessnumber:
                print('lower than thsi! try again.')
            else:
                print(f'Correct! you guessed it in {attempts} guesses')
                break
        except ValueError:
            print('invalid number! try again')

def game():
    rps = ['rock', 'paper', 'scissors']
    choice = input('Choose rock , paper or scissor:').lower()
    Bot = random.choice(rps)

    print(f'Computer has chosen: {Bot}')

    if choice == Bot:
        print ('Draw!')
    elif (choice == 'rock' and Bot == 'scissor') or \
        (choice == 'scissor' and Bot == 'paper') or \
        (choice == 'paper' and Bot == 'rock' ):
        print ('You Win!')
    else :
        print ('You Lose!')

def main():

    while True:
        print ('\nSelect your choice:')
        print ('1. Number guessing game')
        print ('2. Rock, papers and scissors')
        print ('3. Exit')

        choice = input('Enter your choice:')
        if choice == '1':
            guessinggame()

        elif choice == '2':
            game()
    
        elif choice == '3':
            print ('Exiting...')
            break
        
        else:
            print ('Invalid choice , please choose a number against the names of each game accordingly.')

if __name__ == '__main__':
    main()

