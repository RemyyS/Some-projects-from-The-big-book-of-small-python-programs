import random
wordtoguess = []
amountoftries = 5
words = ["Aardvark", "Orange", "Mptkxp"]

selectedword = random.choice(words).upper()

print (selectedword)
for letter in selectedword:
    wordtoguess.append("_")
x = "".join(wordtoguess)

while amountoftries > 0:

    guessedletter = input(f"Enter your guessed letter, you have {amountoftries} left >")

    for letter in selectedword:

        if letter == guessedletter:
            wordtoguess[selectedword.index(guessedletter)] = guessedletter
    print(wordtoguess)
        

print(wordtoguess)
