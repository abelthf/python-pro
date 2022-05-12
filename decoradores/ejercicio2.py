# coding: utf-8
# poniendo en practica

from datetime import datetime


def execution_time(func):
    def wrapper(*args, **kwargs):
        # *args = argumentos posicionales
        # **kwargs = argumentos nombrados
        # * = operador de desestructuración en python
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f"pasaron {time_elapsed.total_seconds()} segundos")
        # print("pasaron " + str(time_elapsed.total_seconds()) + " segundos")

    return wrapper


@execution_time
def random_func():
    for _ in range(1, 1000000000):
        pass


@execution_time
def suma(a: int, b: int) -> int:
    return a + b


suma(2, 2)


@execution_time
def saludo(nombre="Abel"):  # kwargs
    # son paramentros nombrados es decir: kwargs
    print("hola " + nombre)


random_func()
suma(5, 5)
saludo("Abel")
