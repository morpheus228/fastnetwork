import logging
import time


def time_logging(func):
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"Время выполнения {func.__name__}: {execution_time:.4f} секунд")
        return result
    return wrapper