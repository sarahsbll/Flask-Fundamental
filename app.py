# app.py

from flask import Flask, request
import json


app = Flask(__name__)
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print("Data received from Webhook is: ", request.json)
        with open("test.txt", "w") as outfile:
            outfile.write("test")
            outfile.close()
        return "Webhook received!"


app.run(host='0.0.0.0', port=8000)
