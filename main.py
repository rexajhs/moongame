import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letter = letters[random.randint(1,25)]
def check(x):
    x = x.lower()
    return x.startswith(letter)
def bring():
    return letter+letters[random.randint(0,25)]+letters[random.randint(0,25)]

print('GOING TO THE MOON GAME')
while 1:
    item = input('Type in your item: ')
    if(check(item)):
        print(f"You can bring {item}.")
        break
    else:
        print(f"You can't bring {item}.")
        print(f"I will bring {bring()}.")
        
