# decorador con azucar sintáctica para ser mas legible


def decorador(func):
    def envoltura():
        print("esto se añade a mi función original")
        func()

    return envoltura


@decorador
def saludo():
    print("¡Hola!")


saludo()
