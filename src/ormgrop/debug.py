import functools
import logging
from time import perf_counter_ns as take_time

logger = logging.getLogger(__name__)


def measure(log_func=logger.debug):
    def decorate(func):
        @functools.wraps(func)
        def measure_and_log(*args, **kwargs):
            name = func.__name__
            start = take_time()
            result = func(*args, **kwargs)
            finish = take_time()
            elapsed_time = finish - start
            log_func(f"[MEASURE] Called '{name}' for {elapsed_time} nanoseconds.")
            return result

        return measure_and_log

    return decorate
