
import requests
import json
import yaml

with open('access_token.yaml', 'r') as file:
    access_token_file = yaml.safe_load(file)

owner = input("Enter repo owner name: ")
repo = input("Enter repo name: ")
base = input("Enter name of base branch: ")
head = input("Enter name of head branch: ")




url = 'https://api.github.com/repos/{}/{}/dependency-graph/compare/{}...{}'.format(owner, repo, base, head)
headers = {'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28', 
           'Authorization': 'Bearer ' + access_token_file['token'] }
response = requests.get(url, headers=headers)



dependency_graph_diff = json.loads(response.text)
num_of_dependencies = len(dependency_graph_diff)

try:
    severities = [v["severity"] for dict in dependency_graph_diff 
                for v in dict["vulnerabilities"]]
    num_of_vulnerabilities = len(severities)  
except:
    print(json.loads(response.text))



#print(json.loads(response.text))
#print(severities)
#print(num_of_vulnerabilities)
#print(num_of_dependencies)



