import logging
import os

LOG_PATH = "data/log_file.log"

def setup_logger():
    os.makedirs("data", exist_ok=True)

    logger = logging.getLogger("app_logger")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(LOG_PATH)
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger