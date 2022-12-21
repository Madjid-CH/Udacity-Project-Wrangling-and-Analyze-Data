from functools import wraps
from timeit import default_timer as time


def timer(func):
    """A decorator that prints how long a function took to run.

    Args:
        func (callable): The function being decorated.

    Returns:
        callable: The decorated function.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        t_start = time()
        result = func(*args, **kwargs)
        t_total = time() - t_start
        print('{} took {}s'.format(func.__name__, t_total))
        return result

    return wrapper



def sub_dict(data, sub_keys):
    """Extracting sub_dictionary from a dictionary."""

    return {k: v for k, v in data.items() if k in sub_keys}