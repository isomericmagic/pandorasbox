# Pandora's Box v1.0
# usage - python3 pandorasbox.py

import requests
from requests.exceptions import Timeout
from requests.exceptions import MissingSchema
import re
from flask import Flask, request, render_template, Markup
import subprocess

def print_output(file_path_1):
    final_response = "Your file path is: " + file_path_1
    return final_response

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def my_results_form():
    if request.method == 'POST':
        first_text = request.form['first_file']
        second_text = request.form['second_file']
        #output = print_output(first_text + ' ... ' + second_text)
        #return render_template('results.html', output = output)
        subprocess.check_call("./test.sh %s %s" % (first_text, second_text), shell=True)
        return render_template('results.html')
    elif request.method == 'GET':
        return render_template('index.html')

if __name__ == '__main__':
   app.run(debug = True, port = 3456, host = '0.0.0.0')