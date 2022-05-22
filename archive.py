
----------------------------------------------------------------------
#test this on heroku, using a public URL, instead of the locally generated Flask one






----------------------------------------------------------------------
#better formatted

from flask import Flask, request
import json


app = Flask(__name__)
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print("Data received from Webhook is: ", request.json)
        # Serializing json 
        json_object = json.dumps(request.get_json(), indent = 4)
        # Writing to sample.json 
        with open("sample3.json", "a") as outfile:
            outfile.write(json_object)
            outfile.close()
        return "Webhook received!"


app.run(host='0.0.0.0', port=8000)


----------------------------------------------------------------------
#simplified, without intermediary dictinary to have append works

from flask import Flask, request
import json


app = Flask(__name__)
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print("Data received from Webhook is: ", request.json)
       
        with open("sample2.json", "a") as outfile:
            json.dump(request.get_json(), outfile)
        return "Webhook received!"

        
app.run(host='0.0.0.0', port=8000)

----------------------------------------------------------------------
#initial iteration, writing to a dictionary and a json file and appending to it
from flask import Flask, request
import json
diction = {}

app = Flask(__name__)
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print("Data received from Webhook is: ", request.json)
        diction.update(request.get_json())
        print(diction)
        #print(type(diction))
        with open("sample.json", "a") as outfile:
            json.dump(diction, outfile)
        return "Webhook received!"

        
app.run(host='0.0.0.0', port=8000)