# github-api-search

This is a service built using python to query github api. The purpose of this service is to identify the file that contains the keyword that was given, then return the identified file's URL and the name of the repo in which it exists.

How to run this code:

Set the environment variable <i>export FLASK_APP = app.py</i><br>
Then pass in command <i>flask run</i>

The service should run in your local host so something like this http://127.0.0.1:5000/

You need to pass in two search parameters to get the file url and repo name.


http://127.0.0.1:5000/<keyword_to_be_found>/<user_name>  (eg: http://127.0.0.1:5000/nginx/rajravichandrann)
