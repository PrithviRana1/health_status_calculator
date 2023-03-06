import repo_config



#On occasion api returns severities as moderate or low instead of medium and minor
#Added those to the dict with the score of the severity that they seem most closely associated to
severity_dict = {'critical': 1, 'high': 0.8,'moderate': 0.5, 'medium': 0.5, 'minor': 0.1, 'low' : 0.1}

severity_score = [severity_dict[x] for x in repo_config.severities]

health_status = repo_config.num_of_dependencies/(repo_config.num_of_vulnerabilities*(sum(severity_score))) if repo_config.num_of_vulnerabilities > 0 else 0

print(health_status)
