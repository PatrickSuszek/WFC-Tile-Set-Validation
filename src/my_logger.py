import logging
from logging import Logger

def setup_logger(logfile: str, console_log: bool) -> Logger:
    """ Creates a logger, that can write events to a logfile.
        Additionally, the events can be printed to the console.

    Args:
        logfile (str): Path to the logfile
        console_log (bool): True if the logger should also output to the console

    Returns:
        Logger: The logging object
    """

    # setup logger
    logger = logging.getLogger(logfile)
    logger.setLevel(logging.INFO)

    # setup logging to file
    file_handler = logging.FileHandler(logfile)
    logger.addHandler(file_handler)

    # setup logging to console if requested
    if console_log:
        console_handler = logging.FileHandler(logfile)
        logger.addHandler(console_handler)

    return logger
