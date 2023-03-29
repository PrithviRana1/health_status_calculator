
import json
import logging
from models import github_api


class ForumulaParams():
    api = github_api.GithubApi()
    api.connections()

    dependency_objs = api.response

    def all_objs(self):
        self.response = [self.collect(json.loads(obj[0].text))
                         for obj in self.dependency_objs]

        self.repo_info = [obj[1] for obj in self.dependency_objs]

    def collect(self, obj):
        num_of_dependencies = len(obj)

        # Create and configure logger
        logging.basicConfig(filename="result.log",
                            format='%(asctime)s %(message)s',
                            filemode='w')

        # Creating an object
        logger = logging.getLogger()

        # Setting the threshold of logger to DEBUG
        logger.setLevel(logging.DEBUG)

        try:
            severities = [v['severity'] for dict in
                          obj
                          for v in dict['vulnerabilities']]
            num_of_vulnerabilities = len(severities)
            return {'severities': severities,
                    'num_of_vulnerabilities': num_of_vulnerabilities,
                    'num_of_dependencies': num_of_dependencies}
        except (AttributeError, TypeError):
            logger.debug(obj)

# print(json.loads(response.text))
# print(severities)
# print(num_of_vulnerabilities)
# print(num_of_dependencies)
