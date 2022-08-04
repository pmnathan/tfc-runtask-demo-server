from urllib.request import Request, urlopen
from opa_client.opa import OpaClient
import ssl
import json

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

