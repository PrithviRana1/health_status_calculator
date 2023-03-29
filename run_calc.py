from core import calculation
from database import loadDB
import logging

test = calculation.Calc()
db = loadDB.DB()

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
    logger.debug(status[0])
    config = status[1]
    logger.debug(config["owner"] + " " +
                 config["repo"] + " " + config["base"] + config["head"])
    db.load(status)
