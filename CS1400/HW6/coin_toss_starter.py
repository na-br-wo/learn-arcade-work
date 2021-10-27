'''Coin_toss contains functionality to support flipping a virtual coin.'''
import random
coin = ['Heads','Tails']

def flip():
    '''Returns 'Heads' or 'Tails' as a random choice "coin flip."'''
    result = random.choice(coin)
    return(result)

def flips(p_iterations, p_toss_string = 'Toss a coin'):
    '''Call flip p_iterations times to run a string of coin tosses.'''        
    for i in range(p_iterations):
        print(p_toss_string,':',flip())


if __name__ == '__main__':
    flips(13, 'Test flip')        

