from random import randint

def guess(number):
    random_number=randint(1,10)
    tries=1
    while number != random_number:
        print("Try again!")
        number=int(input("Pick a number between 1 and 10 (inclusive): "))
        tries+=1
    print("Well done! You got the magic number in %d tries :)" % (tries))

initial_guess=int(input("Pick a number between 1 and 10 (inclusive): "))
guess(initial_guess)
        
