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

    response_text = str(data)
    #Today's History

    #Surprise Me

    #date
    '''value = data['option']
    if str(value) == "1":
        print("Surprise Me")
        innerwrapper =  data["text"]
        optionentered = innerwrapper["body"]
        if(optionentered == "trivia"):
            response = requests.get("http://numbersapi.com/random/trivia")
            response_text = response.text
        elif(optionentered == "math"):
            response = requests.get("http://numbersapi.com/random/math")
            response_text = response.text
        elif (optionentered == "date"):
            response = requests.get("http://numbersapi.com/random/date")
            response_text = response.text
        elif (optionentered == "year"):
            response = requests.get("http://numbersapi.com/random/year")
            response_text = response.text
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
        print("Please select an option")'''

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
    payload= "{\n    \"to\": \"+919764772960\",\n    \"type\": \"button\",\n    \"button\": {\n        \"body\": {\n            \"type\": \"text\",\n            \"text\": {\n                \"body\": \"Hello, click on the button to explore Number Nuggets.\"\n            }\n        },\n        \"buttons\": [\n            {\n                \"type\": \"solid\",\n                \"body\": \"Trivia\",\n                \"reply\": \"Mathematics, Class 1\"\n            },\n            {\n                \"type\": \"solid\",\n                \"body\": \"Mathematics quiz, Class 1\",\n                \"reply\": \"Mathematics quiz, Class 1\"\n            },\n            {\n                \"icon\": \"registration\",\n                \"type\": \"dotted\",\n                \"body\": \"Add another student\",\n                \"reply\": \"Add another student\"\n            }\n        ],\n        \"allow_custom_response\": true,\n        \"ttl\": 600\n    }\n}"

    responsenew = requests.request("POST", url, headers=headers, data=payload)
    return jsonify(responsenew.text)


if __name__ == '__main__':
    #app.run(host='0.0.0.0',port=10000)
    app.run(debug=True)


