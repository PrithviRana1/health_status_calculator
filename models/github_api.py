import requests
from models import config_loader


class GithubApi:
    setup = config_loader.ConfigLoader()

    def github_connector(self, obj):
        config = obj
        url = 'https://api.github.com/repos/{}/{}/dependency-graph/compare/{}...{}'.format(config['owner'], config['repo'], config['base'], config['head']) # noqa
        headers = {'Accept': config['accept'],
                   'X-GitHub-Api-Version': config['apiV'],
                   'Authorization': 'Bearer ' + config['token']}
        return requests.get(url, headers=headers)

    def connections(self):
        objects = self.setup.config_objects()
        self.response = [self.github_connector(obj) for obj in objects]

