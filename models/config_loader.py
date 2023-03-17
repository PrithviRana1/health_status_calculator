import yaml
import re
import os


class ConfigLoader:
    def config_params(self):
        path = os.path.join('config', 'configuration.yaml')
        f = open(path, "r")
        config = yaml.load(f, Loader=yaml.FullLoader)
        f.close()
        return config

    def validate(self):
        config = self.config_params()
        try:
            if not isinstance(config["owner"], str):
                raise TypeError
        except TypeError:
            print("Owner should be a string\n")

        try:
            if not isinstance(config["repo"], str):
                raise TypeError
        except TypeError:
            print("Repo should be a string\n")

        try:
            if not isinstance(config["base"], str):
                raise TypeError
        except TypeError:
            print("Base should be a string\n")

        try:
            if not isinstance(config["head"], str):
                raise TypeError
        except TypeError:
            print("Head should be a string\n")

        try:
            if not isinstance(config["token"], str):
                raise TypeError
        except TypeError:
            print("Token should be a string\n")

        try:
            pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$", re.IGNORECASE)
            match = re.match(pattern, config["apiV"])
            if match is None:
                raise ValueError

        except ValueError:
            print("Api version should be of the format yyyy-mm-dd\n")

        try:
            pattern = re.compile(r"application/vnd\.github.[a-z]*")
            match = re.match(pattern, config["accept"])
            if match is None:
                raise ValueError

        except ValueError:
            print("Accept media type should be of the"
                  + " format application/vnd.github+param[+json]\n")

        return config
