# aplicacion que utiliza el tipado estático
# ejecutarlo con mypy para ver los errores antes de ser ejecutados


# si una cadena de carateres es palíndromo, como ana


def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    # Ana es diferente de ana, debe convertirse a minúscula
    return string == string[::-1]


def run():
    # print(is_palindrome("ana"))
    print(is_palindrome(1000))
    # ejecutar con mypy para ver el error de tipado
    # mypy contipadoestatico.py --check-untyped-defs


if __name__ == "__main__":
    run()
