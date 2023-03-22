from core import calculation
import logging

test = calculation.Calc()

# Create and configure logger
logging.basicConfig(filename="result.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

# Logging Result
for status in test.all_statuses():
    logger.debug(status)
