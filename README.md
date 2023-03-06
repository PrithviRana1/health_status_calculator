# health_status_calculator
Calculates repo health status based on vulnerabilities and dependencies 

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
5. Activate virtual environment and run pip install -r requirements.txt in terminal
6. Run python calculation.py in terminal  <br>
(Make sure that you are using Python 3)
# How to configure for custom runs
You can configure the program for custom runs by following the prompts displayed on the terminal after you run the file
# Sample experiments

### https://github.com/brave/brave-browser
owner : brave
repo : brave-browser


1.
base : master
head : 0.72.x
health_status = 0.036630036630036625

2.
base : master
head = 1.50.x
health_status = 0

### https://github.com/spring-projects/spring-framework
owner : spring-projects
repo : spring-framework

1.
base : 3.0.x
head : 3.1.x
health_status = 0.0007328075213192672


2.
base : main
head : 5.3.x
health_status = 0

### https://github.com/hibernate/hibernate-reactive
owner : hibernate
repo : hibernate-reactive

1.
base : 1.0
head : 1.1
health_status = 0


2.
base : main
head : 1.1
health_status = 0

### https://github.com/fastify/fastify
owner : fastify
repo : fastify

1.
base : 1.x
head : 2.x
health_status = 180.0

2.
base : main
head : fix-log-test-node-v16
health_status = 0

### https://github.com/expressjs/express
owner : expressjs
repo : express

1.
base : benchmark
head : traige
health_status = 0.15624999999999994

2.
base : master
head : develop
health_status = 0



