import logging
import logging.config


def setup_logger():
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%d/%m/%y %H:%M:%S",
        level=logging.INFO,
    )

setup_logger()