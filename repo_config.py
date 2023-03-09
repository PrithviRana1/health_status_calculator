
import requests
import json


class GithubApi:
    def request_params(self):
        owner = input("Enter repo owner name: ")
        repo = input("Enter repo name: ")
        base = input("Enter name of base branch: ")
        head = input("Enter name of head branch: ")
        api_version = input("Enter api version: ")
        accept = input("Enter format of data to be returned: ")
        token = input("Enter Github personal access token: ")
        return {'owner': owner, 'repo': repo, 'base': base, 'head': head,
                'api_version': api_version, 'accept': accept, 'token': token}

    def github_connector(self):
        params = self.request_params()
        url = 'https://api.github.com/repos/{}/{}/dependency-graph/compare/{}...{}'.format(params['owner'], params['repo'], params['base'], params['head']) # noqa
        headers = {'Accept': params['accept'],
                   'X-GitHub-Api-Version': params['api_version'],
                   'Authorization': 'Bearer ' + params['token']}
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
