from app import app
from flask import render_template, jsonify, request, url_for, redirect
import requests

@app.route('/', methods=['GET', 'POST'])
def submit():


    return render_template('index.html')



@app.route('/index')
def index():
    #
    #
    # url = 'https://api.flickr.com/services/rest/?method=flickr.photos.search&tags={}&api_key=8fea723e595025b5e332ffde745db8d5&format=json'.format(tag)

    # photo = requests.get(url).json()

    return render_template('index.html')
