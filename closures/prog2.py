def main():
    a = 1

    def nested():
        print(a)

    return nested


my_func = main()
my_func()

# puedo eliminar la función main, pero el valor se recordará

del main

my_func()
