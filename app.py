# app.py

from flask import Flask, request
from github import Github


# using an access token

g = Github("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")

app = Flask(__name__)
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print("Data received from Webhook is: ", request.json)
        for repo in g.get_user().get_repos():
            print(repo.name)
        #with open("test.txt", "w") as outfile:
            #outfile.write("test")
            #outfile.close()
        return "Webhook received!"


app.run(host='0.0.0.0', port=8000)
