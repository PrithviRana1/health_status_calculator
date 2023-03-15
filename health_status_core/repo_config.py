
import requests
import json
import yaml
import re


class ConfigLoader:
    def config_params(self):
        f = open("config.yaml", "r")
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


class GithubApi:
    setup = ConfigLoader()

    def github_connector(self):
        config = self.setup.validate()
        url = 'https://api.github.com/repos/{}/{}/dependency-graph/compare/{}...{}'.format(config['owner'], config['repo'], config['base'], config['head']) # noqa
        headers = {'Accept': config['accept'],
                   'X-GitHub-Api-Version': config['apiV'],
                   'Authorization': 'Bearer ' + config['token']}
        self.response = requests.get(url, headers=headers)


class ForumulaParams():
    api = GithubApi()
    api.github_connector()

    dependency_graph_diff = json.loads(api.response.text)

    def collect(self):
        self.num_of_dependencies = len(self.dependency_graph_diff)
        try:
            self.severities = [v["severity"] for dict in
                               self.dependency_graph_diff
                               for v in dict["vulnerabilities"]]
            self.num_of_vulnerabilities = len(self.severities)
        except (AttributeError, TypeError):
            print(self.dependency_graph_diff)

# print(json.loads(response.text))
# print(severities)
# print(num_of_vulnerabilities)
# print(num_of_dependencies)
