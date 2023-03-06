# health_status_calculator
Calculates repo health status by using dependency diff 

# About
This project calculates the health status of a repo by making use of the GitHub api <br>
health status = number of dependencies/summation(number of vulnerabilities * severity score) <br>
severity score dictionary = {'critical': 1, 'high': 0.8,'moderate': 0.5,'minor': 0.1}

# How to run
1. Clone repo and open in IDE of choice
2. Generate a GitHub personal access token (classic) <br>
    Token should atleast have admin:public_key scope
3. Create a file named access_token.yaml and store your token in it. <br>
    File should look like this: <br>
        --- <br>
        token : 'yourToken'
4. Open the terminal and create a virtual environment
5. Run pip install -r requirements.txt in terminal
6. Run calculation.py in terminal
# How to configure for custom runs
You can configure the program for custom runs by following the prompts displayed on the terminal after you run the file
# Sample experiments





