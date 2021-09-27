import requests
from flask import Flask, jsonify
from flask_restful import Api, Resource
import os
import json
token = os.getenv('GITHUB_TOKEN')
app = Flask(__name__)
# api = Api(app)


# class Search(Resource):
@app.route('/search/<search_term>/<user>')
def get(search_term,user):
    query_url = "https://api.github.com/search/code" #"code_search_url": "https://api.github.com/search/code?q={query}{&page,per_page,sort,order}"
    para_str= search_term + " in:file user:" + user
    parameter= {"q":para_str } #"q":nginx in:file user:rajravichandrann
    r = requests.get(query_url,params=parameter)
    response= r.json()
    d = dict();#create a dictionary
    d['file_url'] = response['items'][0]['html_url']
    d['repo'] = response['items'][0]['repository']['full_name']
    return d


# api.add_resource(Search, '/search')


if __name__=="__main__":
    app.run(debug=True)
