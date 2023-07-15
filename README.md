# Cinemapi
A simple rest api made with `Flask` and `MySQL` to manage movie theaters, tickets and shows.

# Installation Guide
## Pre-requirements
In this project I will use `MySQL` as a database administrator and it is recommended to use `virtualenv` to avoid conflicts with other projects.

## How to start?
Clone the repository.
```
$ git clone https://github.com/angcoder-c/cinemapi.git
```
Create the virtual environment, and activate it.
```
> cd cinemapi
> python -m venv venv
> venv\Scripts\activate.bat
```
Create the database from the MySQL CLI client, using the `create.sql` file.
```
mysql> source C:\path\project\create.sql
```
Or by entering the following commands
```
mysql> CREATE DATABASE IF NOT EXISTS cinemapi;
mysql> USE cinemapi;
```

## Install dependencies
```
(venv) C:\cinemapi> python -m pip install -r requirements.txt
```

## Run 
```
(venv) C:\project> python main.py
```
Visit `https://127.0.0.1:5000` to see the project in operation
# License
- MIT
