import time
import tracemalloc


def measurements(func):
    """
    Measures time and memory complexity of given function. Retruns tuple of
    time (in seconds), memory (in megabytes) and output of given function.

    :param func: function
    :return: tuple (float, float, func output)
    """
    def measurements_wrapper(*args, **kwargs):
        # initialization of measurement
        tracemalloc.start()
        start = time.perf_counter_ns()

        # execution of function
        output = func(*args, **kwargs)

        # end of measurement
        peak = tracemalloc.get_traced_memory()[1]
        end = time.perf_counter_ns()
        tracemalloc.stop()

        # calculation of output vals - time in seconds, memory in MB
        time_of_execution = (end - start) / 10 ** 9
        memory_used = peak / 10 ** 6
        return time_of_execution, memory_used, output,

    return measurements_wrapper