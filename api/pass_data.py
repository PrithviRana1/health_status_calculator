import requests
import os
import yaml


config_dir = '/config'

config = []

for filename in os.listdir(config_dir):
    filepath = os.path.join(config_dir, filename)
    with open(filepath, 'r') as f:
        data = yaml.load(f, Loader=yaml.Loader)
        config.append(data)

config_list = {"data_list": config}

response = requests.post("http://localhost:8000", json=config_list, headers={"Content-Type": "application/json"}) # noqa

print(response.status_code)
print(response.json())
