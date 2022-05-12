# poniendo en práctica

from datetime import datetime


def execution_time(func):
    def wrapper():
        initial_time = datetime.now()
        func()
        final_time = datetime.now()
        time_elapsed = final_time - initial_time

        print(f"pasaron {time_elapsed.total_seconds()} segundos")
        # print("pasaron " + str(time_elapsed.total_seconds()) + " segundos")

    return wrapper


@execution_time
def random_func():
    for _ in range(1, 1000000):
        pass


random_func()
