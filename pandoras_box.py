# Pandora's Box v1.0
# usage - python3 pandorasbox.py

import requests
from requests.exceptions import Timeout
from requests.exceptions import MissingSchema
import re
from flask import Flask, request, render_template, Markup
import appscript
import os

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def my_results_form():
    if request.method == 'POST':
        first_text = request.form['first_file']
        second_text = request.form['second_file']
        directory_path = os.getcwd()
        appscript.app('Terminal').do_script('cd ' + directory_path + ';''./test.sh' + ' ' + first_text + ' ' + second_text)
        return render_template('results.html')
    elif request.method == 'GET':
        return render_template('index.html')

if __name__ == '__main__':
   app.run(debug = True, port = 3456, host = '0.0.0.0')