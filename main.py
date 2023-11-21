import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letter = letters[random.randint(0,25)]

def check(item):
    item = item.lower()
    return item.startswith(letter)
def bring():
    word = letter
    word += letters[random.randint(0,25)]
    word += letters[random.randint(0,25)]
    return word

print("GOING TO THE MOON GAME")
print("I will bring " + bring() + "!")
while 1:
    item = input("What will you bring? ")
    if (check(item)):
        print("You can bring " + item + "!")
        break
    else:
        print("You can't bring " + item + "!")
        print("I will bring " + bring() + ".")
        
        
