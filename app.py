from flask import Flask
from flask import request
import json
import os
import requests

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def format_call():
   if request.method == 'GET':
       return "Done"
   else:
       alertdata=request.json
       senddata = {}
       senddata["customer_id"] = os.environ['CUSTOMER_KEY']
       senddata["log_type"] = "SOME_LOG"
       senddata["entries"] = [alertdata]

       x = requests.post(os.environ['GC_URL'], data=json.dumps(senddata))
       return "Event Sent"
