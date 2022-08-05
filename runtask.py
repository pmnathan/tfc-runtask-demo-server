from urllib.request import Request, urlopen
import subprocess, ssl, json
from opa_client.opa import OpaClient

def post_data(url, data, headers={'Content-Type':'application/json'}):
    """
    POST data string to `url`, return page and headers
    """
    # if data is not in bytes, convert to it to utf-8 bytes
    bindata = data if type(data) == bytes else data.encode('utf-8')
    # need Request to pass headers
    req = Request(url, bindata, headers)
    resp = urlopen(req)
    return resp.read(), resp.getheaders()

def run_opa_as_shell():
    app.logger.info("Start subprocess for OPA request")


def process_opa(app, rq):
    app.logger.info("Processing OPA request")

    #get variables from request
    plan_json_url = rq['plan_json_api_url']
    token = rq['access_token']

    #get plan from TFC
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE #adding this because of the error: "certificate verify failed"

    req = Request(plan_json_url)
    req.add_header('Authorization', 'Bearer ' + token)
    content = urlopen(req, context=ctx).read()
    data = json.loads(content)
    print (data)

    #send plan to OPA

    #get result from OPA

    #return result to TFC

