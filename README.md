
```sh
seperate server(Django Rest) and client(Angularjs) code
client folder contains Angularjs code
server folder contais Django code

Django using Rest Framework API
Django run on port - 8000
Angularjs run on port -8081


pip install -r requirements.txt

for running Django :-
========================
python server/manage.py migrate
python server/manage.py makemigrations
python server/manage.py runserver

for running Angularjs :-
========================
cd client (inside the client folder)
npm install
npm start

'''

Notes:
  pip installed Pillow in server/ to work with images
