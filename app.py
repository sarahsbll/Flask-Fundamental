# app.py

from flask import Flask, request
import dropbox


# using an access token

# using an access token
dbx = dropbox.Dropbox('sl.BIFVS2Po_OUNDI8q_DVraj12gqyKm4DrwwCenpc1Xy3Aq1hvzYwu5nBp8cevJ1Gt3nmctUc2J7J_kbQ0vrUU91G04dDVDptP81zr4OxSqUZgeTP2ZANOD68GAvOFQ8N0mCLlfGX2Wcb_')

str_1 = "Join our freelance network"

str_1_encoded = bytes(str_1,'UTF-8')

dbx.files_upload(str_1_encoded, '/Python/test.txt')



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
