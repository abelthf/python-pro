FALLBACK_PHONE = "e+00000000"


def get_phone():
    phone = input("Dame tu número de cel: ")
    if not phone:
        return FALLBACK_PHONE.round()
    return int(phone)


def run():
    my_phone = get_phone()
    print(f"Tu número de teléfono es: {my_phone}")


run()
