import requests
import os
import yaml


def config_params(payload=None):
    if payload is None:
        path = os.path.join('config', 'configuration.yaml')
        f = open(path, "r")
        config = list(yaml.safe_load_all(f))
        config_list = {"data_list": config}
        f.close()
        return config_list
    else:
        return payload


payload = {"data_list": [
                            {
                                "owner": "brave",
                                "repo": "brave-browser",
                                "base": "master",
                                "head": "0.72.x",
                                "apiV": "2022-11-28",
                                "accept": "application/vnd.github+json",
                                "token": "" # noqa

                            },

                            {
                                "owner": "spring-projects",
                                "repo": "spring-framework",
                                "base": "3.0.x",
                                "head": "3.1.x",
                                "apiV": "2022-11-28",
                                "accept": "application/vnd.github+json",
                                "token": "" # noqa

                            }

                        ]
           }
# for specifying payload in configuration file
# api_body = config_params()

# for specifying payload in file
api_body = config_params(payload)

response = requests.post("http://localhost:8000", json=api_body, headers={"Content-Type": "application/json"}) # noqa

print(response.status_code)
print(response.json())
