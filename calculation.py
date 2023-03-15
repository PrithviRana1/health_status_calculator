from repo_config import ForumulaParams


class calc:
    variables = ForumulaParams()
    variables.collect()
    # On occasion api returns severities
    # as moderate or low instead of medium and minor
    # Added those to the dict with the score
    # of the severity that they seem most closely associated to

    def get_severity_score(self):
        severity_dict = {'critical': 1, 'high': 0.8, 'moderate': 0.5,
                         'medium': 0.5, 'minor': 0.1, 'low': 0.1}
        self.severity_score = [severity_dict[x] for x in
                               self.variables.severities]

    def get_health_status(self):
        self.get_severity_score()
        health_status = (self.variables.num_of_dependencies /
                         (self.variables.num_of_vulnerabilities *
                          (sum(self.severity_score)))
                         if self.variables.num_of_vulnerabilities > 0 else 0)

        return health_status


test = calc()
print(test.get_health_status())
