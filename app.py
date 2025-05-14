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

    #response_text = str(data)
    #Today's History

    #Surprise Me

    #date
    if "button_index" not in data:
        value = -1
    else:
        value = data['button_index']



    if str(value) == "0":
        print("Surprise Me")
        response = requests.get("http://numbersapi.com/random/trivia")
        response_text = response.text
    elif str(value) == "1":
        print("Option History")

        
    elif str(value) == "2":
        print("Option Number")
        response_text = "Enter a number"
    elif str(value) == "3":
        print("Option Date")
        datewrapper = data["text"]
        dateentered = datewrapper["body"]
        date_object = datetime.strptime(dateentered,'%Y-%m-%d')
        response = requests.get("http://numbersapi.com/" + str(date_object.month)+"/"+str(date_object.day)+"/date")
        response_text = response.text
    elif str(value) == "-1":
        print("Number details")
        print("Option num")
        numberwrapper = data["text"]
        numberentered = numberwrapper["body"]
        response = requests.get("http://numbersapi.com/" + str(numberentered))
        response_text = response.text
    else:
        print("Please select an option")

    #senddatatochatbot(response.text)
    url = "https://v1-api.swiftchat.ai/api/bots/0210276432749689/messages"
    payload = "{\"to\": \"+919764772960\",\"type\": \"text\",  \"text\": {\"body\": \""+ str(response_text)+"\" }}"
    api_key = "21bda582-e8d0-45bc-bb8b-a5c6c555d176"
    headers = {"Authorization": f"Bearer {api_key}",'Content-type': 'application/json'}
    responsenew = requests.request("POST", url, headers=headers, data=payload)
    return jsonify(response_text + responsenew.text)

@app.route('/createbuttons', methods=['GET'])
def createbuttons():
    url = "https://v1-api.swiftchat.ai/api/bots/0210276432749689/messages"
    api_key = "21bda582-e8d0-45bc-bb8b-a5c6c555d176"
    headers = {"Authorization": f"Bearer {api_key}", 'Content-type': 'application/json'}
    payload = "{\n    \"to\": \"+919764772960\",\n    \"type\": \"button\",\n    \"button\": {\n        \"body\": {\n            \"type\": \"text\",\n            \"text\": {\n                \"body\": \"Hello, click on the button to explore Number Nuggets.\"\n            }\n        },\n        \"buttons\": [\n            {\n                \"type\": \"solid\",\n                \"body\": \"Number Trivia\",\n                \"reply\": \"Number Trivia\"\n            },\n            {\n                \"type\": \"solid\",\n                \"body\": \"Today History\",\n                \"reply\": \"Today History \"\n            },\n            {\n            \"type\": \"solid\",\n                \"body\": \"Know about a number\",\n                \"reply\": \"Know about a number\"\n            }\n        ],\n        \"allow_custom_response\": true,\n        \"ttl\": 600\n    }\n}"

    responsenew = requests.request("POST", url, headers=headers, data=payload)
    return jsonify(responsenew.text)


if __name__ == '__main__':
    #app.run(host='0.0.0.0',port=10000)
    app.run(debug=True)


