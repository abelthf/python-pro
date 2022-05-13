# serie Fibonacci: 0 1 1 2 3 5 8 13 21
# 34 55 89 144 ...

# lo pondremos dentro de un iterador

# crearemos un iterador que guarde la serie Fibonacci

import time


class FiboIter:
    def __init__(self):
        pass

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2

        else:
            self.aux = self.n1 + self.n2
            # self.n1 = self.n2
            # self.n2 = self.aux
            # usando swapping
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.aux


# creando un entry point

if __name__ == "__main__":
    serieFibonacci = FiboIter()
    numero = int(input("ingresar limite de fibonacci: "))

    for element in serieFibonacci:
        if element <= numero:
            print(element)
            time.sleep(0.05)
        else:
            StopAsyncIteration
            break


# 0 1 1 2
