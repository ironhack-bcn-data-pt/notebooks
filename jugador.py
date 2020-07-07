import random

class Jugador:
    
    def __init__(self):
        pass
    
    def piensa(self):
        self.numero = random.randint(1,100)
    
    def pregunta(self):
        while True:
            try:
                numero = int(input('Dime un número: '))
                break
            except:
                pass
        
        return numero
    
    def chequea(self, guess):
        if self.numero > guess:
            print('el numero es mayor')
        elif self.numero < guess:
            print('el numero es menor')
        else:
            print('has acertado')

class Juego:
    def __init__(self):
        self.name = 'Guess my number'
        self.descripcion = 'Tienes que adivinar el numero que he pensado'


    def jugar(self):
        j = Jugador()
        j.piensa()

        while True:
            guess = j.pregunta()
            j.chequea(guess)
            if j.numero == guess:
                break

if __name__ == '__main__':
    juego = Juego()
    print(juego.name)
    print(juego.descripcion)
    while True:
        juego.jugar()
        if input('Quieres seguir jugando? (y|n)') != 'y':
            break