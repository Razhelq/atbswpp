import random, logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


guess = ''
while guess not in ('1', '0'):
    guess = input('Guess the coin toss! Enter 1 for heads or 0 for tails:')
toss = str(random.randint(0, 1)) # 0 is tails, 1 is heads
logging.debug('guess = {}, toss = {}'.format(guess, toss))
if toss == guess:
    print('You got it!')
else:
    guess = input('Nope! Guess again!')
    logging.debug('guess = {}, toss = {}'.format(guess, toss))
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
