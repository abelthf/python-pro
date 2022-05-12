def make_divisor_of(n):
    def divisor(num):
        assert type(num) == int, "solo puedes usar números"
        return num / n

    return divisor


def run():
    divisor_3 = make_divisor_of(3)
    print(divisor_3(18))

    divisor_5 = make_divisor_of(5)
    print(divisor_5(100))

    divisor_18 = make_divisor_of(18)
    print(divisor_18(54))


if __name__ == "__main__":
    run()
