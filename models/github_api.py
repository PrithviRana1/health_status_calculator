import requests
from models import config_loader
import datetime


class GithubApi:
    setup = config_loader.ConfigLoader()

    def github_connector(self, obj):
        config = obj
        url = 'https://api.github.com/repos/{}/{}/dependency-graph/compare/{}...{}'.format(config['owner'], config['repo'], config['base'], config['head']) # noqa
        headers = {'Accept': config['accept'],
                   'X-GitHub-Api-Version': config['apiV'],
                   'Authorization': 'Bearer ' + config['token']}
        config['datetime'] = datetime.datetime.now()
        return requests.get(url, headers=headers), config

    def connections(self):
        objects = self.setup.config_objects()
        self.response = [self.github_connector(obj) for obj in objects]
