import requests
from models import config_loader


class GithubApi:
    setup = config_loader.ConfigLoader()

    def github_connector(self):
        config = self.setup.validate()
        url = 'https://api.github.com/repos/{}/{}/dependency-graph/compare/{}...{}'.format(config['owner'], config['repo'], config['base'], config['head']) # noqa
        headers = {'Accept': config['accept'],
                   'X-GitHub-Api-Version': config['apiV'],
                   'Authorization': 'Bearer ' + config['token']}
        self.response = requests.get(url, headers=headers)
