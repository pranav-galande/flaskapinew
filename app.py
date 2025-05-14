from datetime import datetime

from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Number API!"})

@app.route('/funfact', methods=['POST'])
def funfactnumber():
    data = request.get_json()
    response_text = None
    #Today's History

    #Surprise Me

    #date
    value = data['option']
    if str(value) == "1":
        print("Surprise Me")
        
    elif str(value) == "2":
        print("Option Number")
        print("Option Date")
        numberwrapper = data["text"]
        numberentered = numberwrapper["body"]
        response = requests.get("http://numbersapi.com/" + str(numberentered) )
        response_text = response.text
    elif str(value) == "3":
        print("Option Date")
        datewrapper = data["text"]
        dateentered = datewrapper["body"]
        date_object = datetime.strptime(dateentered,'%Y-%m-%d')
        response = requests.get("http://numbersapi.com/" + str(date_object.month)+"/"+str(date_object.day)+"/date")
        response_text = response.text
    elif str(value) == "4":
        print("Option History")
    else:
        print("Please select an option")

    #senddatatochatbot(response.text)
    url = "https://v1-api.swiftchat.ai/api/bots/0210276432749689/messages"
    payload = "{\"to\": \"+919764772960\",\"type\": \"text\",  \"text\": {\"body\": \""+ str(response_text)+"\" }}"
    api_key = "21bda582-e8d0-45bc-bb8b-a5c6c555d176"
    headers = {"Authorization": f"Bearer {api_key}",'Content-type': 'application/json'}
    responsenew = requests.request("POST", url, headers=headers, data=payload)
    return jsonify(response_text + responsenew.text)

if __name__ == '__main__':
    #app.run(host='0.0.0.0',port=10000)
    app.run(debug=True)


