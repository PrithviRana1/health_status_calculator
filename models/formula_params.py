
import json
from models import github_api


class ForumulaParams():
    api = github_api.GithubApi()
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
