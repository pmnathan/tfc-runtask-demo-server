from flask import Flask, redirect, url_for, request
from runtask import *

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/runtask", methods = ['GET', 'POST'])
def run_task():
    if request.method == 'POST':
        rq = request.json
        app.logger.info('Processing - %s on workspace - %s [%s] ', rq['run_id'], rq['workspace_name'], rq['workspace_id'])
        if rq['run_id'] != 'run-xxxxxxxxxxxxxxxx':
            process_opa(app,rq)
        else:
            app.logger.info('Test Run Task Registration message from TFC. Skip processing OPA request')
        return "Ok"
    else:
      return "GET"