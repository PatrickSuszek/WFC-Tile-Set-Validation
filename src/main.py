import itertools

from my_logger import setup_logger
from validation import *


if __name__ == "__main__":

    data = {
        0: {0, 1, 2},
        1: {0, 1, 4},
        2: {0, 2, 4},
        3: {1, 2, 3},
        4: {1, 3, 4},
    }

    
    logger = setup_logger("./src/test.info", False)
    valid = two_dim(logger, data)
    valid = chunk(logger, data)



    if valid:
        logger.info("The given tile constraint set is valid")