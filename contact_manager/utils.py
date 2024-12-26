import time
import logging

logging.basicConfig(level=logging.INFO)


def log_execution(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Starting execution of {func.__name__}")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(f"Finished execution of {func.__name__} in {end_time - start_time:.4f} seconds")
        return result
    return wrapper
