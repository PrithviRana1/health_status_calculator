import repo_config

#No medium severity seen
#Replaced medium with moderate in dict
severity_dict = {'critical': 1, 'high': 0.8,'moderate': 0.5,'minor': 0.1}

severity_score = [severity_dict[x] for x in repo_config.severities]

health_status = repo_config.num_of_dependencies/(repo_config.num_of_vulnerabilities*(sum(severity_score)))

print(health_status)
