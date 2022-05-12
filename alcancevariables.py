# scope: alcance de las variables


def my_func():
    # local scope
    y = 5
    print(y)


my_func()

print("---------------")


# Global scope
y = 5


def my_func():
    print(y)


def my_other_func():
    print(y)


my_func()
my_other_func()
