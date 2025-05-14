from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Number API!"})

@app.route('/NumberNuggets',methods=['POST'])  #registered in bot
def NumberNuggets():
    #fetch the data
    data = request.get_json()
    #processign code
    SendMessageToBot("Hello")
    return jsonify({"message": "Welcome to the Number API!"})

#knowabout number

#know about date
#suprise me
def TodaysHistory():
    print("HistoryMethod Invoked")

#send message to bot
def  SendMessageToBot(textMessage):
    url = "https://v1-api.swiftchat.ai/api/bots/0210276432749689/messages"
    payload = "{\"to\": \"+919764772960\",\"type\": \"text\",  \"text\": {\"body\": \""+ {textMessage}+"\" }}"
    api_key = "21bda582-e8d0-45bc-bb8b-a5c6c555d176"
    headers = {"Authorization": f"Bearer {api_key}",'Content-type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)




#sample
@app.route('/funfact', methods=['POST'])
def funfactnumber():

    data = request.get_json()

    number = data['message_id']
    #if number.isdigit():
    response = requests.get("http://numbersapi.com/" + str(10))
    #senddatatochatbot(response.text)

    url = "https://v1-api.swiftchat.ai/api/bots/0210276432749689/messages"

    payload = "{\"to\": \"+919764772960\",\"type\": \"text\",  \"text\": {\"body\": \"Hello\" }}"

    api_key = "21bda582-e8d0-45bc-bb8b-a5c6c555d176"
    headers = {"Authorization": f"Bearer {api_key}",'Content-type': 'application/json'}

    responsenew = requests.request("POST", url, headers=headers, data=payload)

    # print(response.text)
    return jsonify(response.text + responsenew.text)

# do not change needed to run in render

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=10000)
    #app.run(debug=True)


