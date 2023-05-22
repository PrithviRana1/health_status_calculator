import requests
import os
from models import config_loader
import datetime


class GithubApi:
    def __init__(self, data_list):
        self.setup = config_loader.ConfigLoader(data_list)
        self.secret = os.environ.get('ACCESS_TOKEN')

    def github_connector(self, obj, token):
        config = obj
        url = 'https://api.github.com/repos/{}/{}/dependency-graph/compare/{}...{}'.format(config['owner'], config['repo'], config['base'], config['head']) # noqa
        headers = {'Accept': config['accept'],
                   'X-GitHub-Api-Version': config['apiV'],
                   'Authorization': 'Bearer ' + token}
        config['datetime'] = datetime.datetime.now()

        return requests.get(url, headers=headers), config

    def connections(self):
        token = self.secret
        objects = self.setup.config_objects()
        self.response = [self.github_connector(obj, token) for obj in objects]
