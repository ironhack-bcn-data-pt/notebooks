from random import randrange

class Juego():

    def __init__(self):
        pass

    def run(self):
        c=0
        while True:
            n=randrange(1,101)
            a = eval(input("Take a guess: "))
            c+=1
            if (a>n):
                print("Lower...")
            elif(a<n):
                print("Higher...")
            else:
                print("You guessed it!")
                print("and it only took you {} attempt(s)".format(c))
                break

def main():
    print("Welcome to 'Guess My Number'!")
    print("I'm thinking of a number between and 100")
    print("Try to guess it in as few attemps as possible")
    Juego().run()

if __name__ == "__main__":
    main()
