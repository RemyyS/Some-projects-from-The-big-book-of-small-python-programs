import random
import sys
wordtoguess = []
amountoftries = 5
words = ["Aardvark", "Orange", "Mptkxp", "Bolosse"]

selectedword = random.choice(words).upper()

print (selectedword)
for letter in selectedword:
    wordtoguess.append("_")

while amountoftries > 0:

    guessedletter = input(f"Enter your guessed letter, you have {amountoftries} left >")
    if guessedletter not in selectedword:
        amountoftries -= 1
        print(f"You missed, you now have {amountoftries} lives left")
    
    for y in range(len(selectedword)):
        letter = selectedword[y]
        if letter is guessedletter:
            wordtoguess[y] = guessedletter
        if "_" not in wordtoguess:
            print(f"Congratulations, the word is {selectedword} !")
            sys.exit()   
            
    x = "".join(wordtoguess)
    print(x)

print(f"No more lives left, the word was {selectedword}")