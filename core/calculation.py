from models import formula_params


class Calc:
    def __init__(self, data_list):
        self.variables = formula_params.ForumulaParams(data_list)

    def get_variables_all_objs(self):
        self.variables.all_objs()
    # On occasion api returns severities
    # as moderate or low instead of medium and minor
    # Added those to the dict with the score
    # of the severity that they seem most closely associated to

    def get_severity_scores(self):
        severity_dict = {'critical': 1, 'high': 0.8, 'moderate': 0.5,
                         'medium': 0.5, 'minor': 0.1, 'low': 0.1}

        self.severity_scores = ['N/A' if x is None else [severity_dict[y]
                                for y in x['severities']] for x in
                                self.variables.response]

    def get_health_status(self, obj, severity_score):
        health_status = (obj['num_of_dependencies'] /
                         (obj['num_of_vulnerabilities'] *
                         (sum(severity_score)))
                         if obj['num_of_vulnerabilities'] > 0 else 0)

        return health_status

    def all_statuses(self):
        self.get_variables_all_objs()
        self.get_severity_scores()
        statuses = ['N/A' if obj is None
                    else (self.get_health_status(obj, severity_score), info)
                    for obj, severity_score, info in
                    zip(self.variables.response,
                        self.severity_scores, self.variables.repo_info)]

        return statuses
