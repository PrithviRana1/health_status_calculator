
import json
import logging
from models import github_api


class ForumulaParams():
    api = github_api.GithubApi()
    api.github_connector()

    dependency_graph_diff = json.loads(api.response.text)

    def collect(self):
        self.num_of_dependencies = len(self.dependency_graph_diff)

        # Create and configure logger
        logging.basicConfig(filename="result.log",
                            format='%(asctime)s %(message)s',
                            filemode='w')
        
        # Creating an object
        logger = logging.getLogger()
        
        # Setting the threshold of logger to DEBUG
        logger.setLevel(logging.DEBUG)

        try:
            self.severities = [v["severity"] for dict in
                               self.dependency_graph_diff
                               for v in dict["vulnerabilities"]]
            self.num_of_vulnerabilities = len(self.severities)
        except (AttributeError, TypeError):
            logger.debug(self.dependency_graph_diff)

# print(json.loads(response.text))
# print(severities)
# print(num_of_vulnerabilities)
# print(num_of_dependencies)
