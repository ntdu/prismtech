# ️⚡️ Menu merchant ⚡️

## Project Description
Menu merchant is a data API written in python3.

## Table of Content
* [Project Description](#project-description)
* [Getting Started](#getting-started)
  + [Running Locally](#running-locally)
    + [Prerequisites](#local-prerequisites) 
    + [Setup](#local-setup)
  + [Running On Docker](#running-on-docker)
    + [Prerequisites](#docker-prerequisites) 
    + [Setup](#docker-setup)
  + [Continuous Integration](#continuous-integration)
  + [Continuous Deployment](#continuous-deployment)

    

## <a id="getting-started"> Getting Started </a>


## <a id="running-locally"> Running Locally</a>

### <a id="local-prerequisites"> Prerequisites</a>
  - Python >= 3.8
  - pip >= 18.0

### <a id="local-setup"> Setup</a>
1. Python environment Installation
Use the package manager [virtualenv](https://pip.pypa.io/en/stable/) to install virtualenv.

```bash
pip install virtualenv
```

2. Build and activate the environment with  [pip](https://virtualenv.pypa.io/en/latest/) to install virtualenv from python 3.8.

```bash
virtualenv your_venv --python=python3.8
source your_venv/bin/activate
```



3. Dependencies Installation

```bash
pip install -r requirments.txt
```


4. Environment variables setup

   - Use the sample env file to create your .env file and save it at the root of the prismtech directory. 

   - You may use EXPORT to set up env variables manually through the command shell.
   

5. Setting up local Postgresql database

   - Install and run postgressql locally [psql](https://www.postgresql.org/download/).

     - [MacOs](https://wiki.postgresql.org/wiki/Homebrew)

     - [Linux](https://www.postgresql.org/download/linux/ubuntu/)


```bash
# Run psql locally and create a Database called cartavolta
# create user and password corresponding the ones you have under your
# .env file USER_DB_USER and USER_DB_PASSWORD.

psql postgres
CREATE DATABASE uspos;
CREATE USER youruser WITH ENCRYPTED PASSWORD 'yourpass';
GRANT ALL PRIVILEGES ON DATABASE uspos TO youruser;
```

6. Local Deployment
   - In the prismtech directory and run the application using the below command.

```bash
python manage.py runserver
```
this will have the API running on the port 8000
### <a id="docker-setup"> Setup ENV</a>
Update database configuration in:
```bash
POSTGRES_HOST=prismtech-db
POSTGRES_PORT=5432
POSTGRES_USER=prismtech
POSTGRES_PASS=prismtech
POSTGRES_DB=uspos
DBTYPE="postgresql"
```
## Usage
1. Migrations: Running two below command
`python manage.py makemigrations`
`python manage.py migrate`

2. Using curl or other tools, you can send requests to the endpoints through methods defined here:
``` http://127.0.0.1:8000/```

3. Postman collections for testing can be found at [here](https://app.getpostman.com/join-team?invite_code=ee0ad27acfefb4ff31f2d3a2a6012046&ws=7412560f-f86f-437c-8cf7-5aab27b4d70e)

## <a id="running-on-docker"> Running On Docker</a>
### <a id="docker-prerequisites"> Prerequisites</a>
  - Docker - [Install Docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04)
  - Docker-compose - [Install Docker-compose](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04)

### <a id="docker-setup"> Setup</a>
1. Build:  `docker-compose build`
2. Run: `docker-compose up`
## <a id="continuous-integration"> Continuous Integration</a>
tbd

## <a id="continuous-deployment"> Continuous Deployment</a>
tbd
