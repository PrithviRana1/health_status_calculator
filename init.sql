
CREATE DATABASE healthdb;
\c healthdb;

CREATE TABLE healthStatus (repo_owner VARCHAR (50) NOT NULL, 
                            repo VARCHAR (50) NOT NULL, 
                            base VARCHAR (50) NOT NULL, 
                            head VARCHAR(50) NOT NULL, 
                            health_status DECIMAL, 
                            date_time TIMESTAMP NOT NULL);

