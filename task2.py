import random

def guessing():
    '''fufunction allows user to type his 6 guesses'''
    guessed = []
    n = 0
    print('Put 6 numbers from 1 to 49')
    try:
        while n not in guessed:
            n = int(input('Put first number: '))
            if n not in range(1, 49):
                print("Number out of range!")
            else:
                guessed.append(n)
                break
    except ValueError:
        print ("It's not a number")
    n1 = int(0)
    i = 0
    while i < 5:
        try:
            n1 = int(input('Put next number: '))
            if n1 in guessed:
                print("Can't put the same numer twice!")
                n1 = int(0)
            elif n1 not in range(1, 49):
                print("Number out of range!")
            else:
                guessed.append(n1)
                i += 1
        except ValueError:
            print("It's not a number")
    guessed.sort()
    return guessed

def drawing():
    '''function draws 6 random numbers'''
    draws = []
    for i in range(49):
        draws.append(int(i))
    random.shuffle(draws)
    draws = draws[:6]
    return draws

def checking(draws, guessed):
    '''function cheks how many numbers were hit by user'''
    score = int(0)
    for i in draws:
        for j in guessed:
            if i == j:
                score += 1
    return score

guessed = guessing()
draws = drawing()
print(guessed)
print(draws)
score = checking(draws, guessed)
print(f"Your score is {score}")
