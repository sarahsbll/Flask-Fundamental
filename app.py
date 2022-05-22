# app.py

from flask import Flask, request
import dropbox


# using an access token
dbx = dropbox.Dropbox('sl.BIEbGIOWbwMq_6iMeJHwP6AnDZBNNWpzn_ywEosK3RtOnf8G00YDz1PfeBhIFRqMua57xsoAlVOo6Edh0Ota7meDwD748GnilHtuvg5eEFEl3K806XaYmyKX2vGdYJIze0Rx0Xdb7ZM')

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
