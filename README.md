
```sh
seperate server(Django Rest) and client(Angularjs) code
client folder contains Angularjs code
server folder contais Django code 

Django using Rest Framework API
Django run on port - 8000
Angularjs run on port -8081

steps to run :- 
git clone https://github.com/anand-tiwari/Django-angularjs-boilerplate.git

creating virtual environment :-
===============================
virtualenv venv (python 2)
or
virtualenv -p python3 venv (python 3)

installing reuirements :-
==========================
pip install -r reuirements.txt

for running Django :-
========================
python server/manage.py migrate
python server/manage.py makemigrations
python server/manage.py runserver

for running Angularjs :-
========================
cd client (inside the client folder)
npm start

'''
