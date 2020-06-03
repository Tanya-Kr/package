import functools
import time


def main():
    print(number_divide(2, 2))
    print(number_divide(5, 0))


def timer(func):
    """Prints the runtime of the decorated function."""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()

        try:
            value = func(*args, **kwargs)
        finally:
            end_time = time.perf_counter()
            run_time = end_time - start_time
            print(f"Finished {func.__name__!r} in {run_time:.20f} secs")
        return value

    return wrapper_timer


@timer
def number_divide(num1, num2):
    return num1/num2


if __name__ == '__main__':
    main()