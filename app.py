# app.py

from flask import Flask, request
import dropbox


# using an access token
dbx = dropbox.Dropbox('sl.BIHrA2OxmhhRbKbeVGMAvWeCB-5V6jIugXVEN7ldnz0Gjp7QAbR2W0PhsiW0op9-fJllfeRXgWbRxYkxrDblx5MihNLvghWiIJYVWHu_QjoiVtPPeqUsye40a5Dm_cW3IaKl-8qRf-Q')
for entry in dbx.files_list_folder('').entries:
    print(entry.name)


app = Flask(__name__)
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
	print("Data received from Webhook is: ", request.json)
	#with open("test.txt", "w") as outfile:            
		#outfile.write("test")
		#outfile.close()
        return "Webhook received!"


app.run(host='0.0.0.0', port=8000)
