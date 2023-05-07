from kubernetes import client, config

class tokenLoader:

    def __init__(self):
        # Load the Kubernetes configuration
        config.load_incluster_config()

        # Create a Kubernetes API client
        api = client.CoreV1Api()

        # Specify the name and namespace of the secret
        secret_name = "access_token"
        namespace = "default"

        # Retrieve the secret object from the API
        secret = api.read_namespaced_secret(secret_name, namespace)
        self.token = secret.data["access_token"].decode()

