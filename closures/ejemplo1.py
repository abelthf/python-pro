# hola 3 -> holaholahola
# abel 4 -> abelabelabelabel


def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "solo puedes usar cadenas"
        return string * n

    return repeater


def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("hola"))
    repeat_10 = make_repeater_of(10)
    print(repeat_10("hola"))


if __name__ == "__main__":
    run()
