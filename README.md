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
4. Add token and update repo and branch targets in configuration file
5. Open the terminal and run docker compose up
6. Run docker exec health_status_calculator-app-1 python /code/api/pass_data.py or go to http://127.0.0.1:8000/docs

# How to configure for custom runs
Update pass_data or use http://127.0.0.1:8000/docs

# Sample experiments

### https://github.com/brave/brave-browser
owner : brave <br>
repo : brave-browser


1.
base : master <br>
head : 0.72.x <br>
health_status = 0.036630036630036625

2.
base : master <br>
head = 1.50.x <br>
health_status = 0

### https://github.com/spring-projects/spring-framework
owner : spring-projects <br>
repo : spring-framework

1.
base : 3.0.x <br>
head : 3.1.x <br>
health_status = 0.0006205450990727045


2.
base : main <br>
head : 5.3.x <br>
health_status = 0

### https://github.com/hibernate/hibernate-reactive
owner : hibernate <br>
repo : hibernate-reactive

1.
base : 1.0 <br>
head : 1.1 <br>
health_status = 0


2.
base : main <br>
head : 1.1 <br>
health_status = 0

### https://github.com/fastify/fastify
owner : fastify <br>
repo : fastify  <br>

1.
base : 1.x <br>
head : 2.x <br>
health_status = 180.0

2.
base : main <br>
head : fix-log-test-node-v16 <br>
health_status = 0

### https://github.com/expressjs/express
owner : expressjs <br>
repo : express

1.
base : benchmark <br>
head : triage <br>
health_status = 0.15624999999999994

2.
base : master <br>
head : develop <br>
health_status = 0



