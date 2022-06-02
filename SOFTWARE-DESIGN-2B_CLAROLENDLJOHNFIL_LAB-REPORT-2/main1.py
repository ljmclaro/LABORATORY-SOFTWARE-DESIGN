import random

def reply(sentence):
    probability = random.randint(1, 4)
    if probability == 1:
        return random.choice(hedges)
    else:
        return random.choice(qualifiers) + changePerson(sentence)

def changePerson(sentence):
    words = sentence.split()
    replyWords = []
    for word in words:
        replyWords.append(replacements.get(word, word))
        return " ".join(replyWords)

def main():
    print("Hello. How are you?.")
    print("What can I do for you?")
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "IM HERE FOR APPOINTMENT":
            print("Oh ok! Please proceed...")
        elif sentence.upper() == "HELLO IM HERE FOR YOU":
            print("Oh, no!")
        elif sentence.upper() == "IM HERE TO BUY MEDICINE":
            print("Please proceed left to near pharmacy!")
        elif sentence.upper() == "QUIT":
            print("Have a nice day!")
            break
            print(reply(sentence))

if __name__ == "__main__":
    main()