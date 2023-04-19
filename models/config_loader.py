import re
import logging


class ConfigLoader:

    def __init__(self, data_list):
        self.data_list = data_list

    def validate(self, obj):
        config = obj

        # Create and configure logger
        logging.basicConfig(filename="result.log",
                            format='%(asctime)s %(message)s',
                            filemode='w')

        # Creating an object
        logger = logging.getLogger()

        # Setting the threshold of logger to DEBUG
        logger.setLevel(logging.DEBUG)

        try:
            if not isinstance(config["owner"], str):
                raise TypeError
        except TypeError:
            logger.debug("Owner should be a string\n")

        try:
            if not isinstance(config["repo"], str):
                raise TypeError
        except TypeError:
            logger.debug("Repo should be a string\n")

        try:
            if not isinstance(config["base"], str):
                raise TypeError
        except TypeError:
            logger.debug("Base should be a string\n")

        try:
            if not isinstance(config["head"], str):
                raise TypeError
        except TypeError:
            logger.debug("Head should be a string\n")

        try:
            if not isinstance(config["token"], str):
                raise TypeError
        except TypeError:
            logger.debug("Token should be a string\n")

        try:
            pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$", re.IGNORECASE)
            match = re.match(pattern, config["apiV"])
            if match is None:
                raise ValueError

        except ValueError:
            logger.debug("Api version should be of the format yyyy-mm-dd\n")

        try:
            pattern = re.compile(r"application/vnd\.github.[a-z]*")
            match = re.match(pattern, config["accept"])
            if match is None:
                raise ValueError

        except ValueError:
            logger.debug("Accept media type should be of the"
                         + " format application/vnd.github+param[+json]\n")

    def config_objects(self):
        objects = self.data_list
        for obj in objects:
            self.validate(obj)
        return objects
