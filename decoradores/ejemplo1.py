def decorador(func):
    def envoltura():
        print("esto se añade a mi funcion original")
        func()

    return envoltura


def saludo():
    print("¡hola!")


saludo()
# output: ¡hola!

saludo = decorador(saludo)
saludo()
# output
# esto se añade a mi funcion original
# ¡hola!
