import requests
import os
import yaml


config_dir = '/etc/app-config/'
config = []

for filename in os.listdir(config_dir):
    filepath = os.path.join(config_dir, filename)

    if os.path.isfile(filepath) and filename.endswith('.yaml'):
        with open(filepath, 'r') as f:
            data = yaml.safe_load(f)
            config.append(data)

config_list = {"data_list": config}
response = requests.post("http://localhost:8000", json=config_list, headers={"Content-Type": "application/json"}) # noqa

print(response.status_code)
print(response.text)
print(response.json())
