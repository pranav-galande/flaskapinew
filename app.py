from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# In-memory storage for demonstration
items = [
    {"id": 1, "name": "Item One"},
    {"id": 2, "name": "Item Two"}
]

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask API!"})


@app.route('/funfact', methods=['POST'])
def funfactnumber():
    data = request.get_json()

    number = data['number']
    #if number.isdigit():
    response = requests.get("http://numbersapi.com/" + str(number))
    senddatatochatbot(response.text)
    return jsonify(response.text)

    # if user input is not valid, it'll notify sthe user accordingly and then give them a fact about some random generated number

def senddatatochatbot(responsetext):


    url = "https://v1-api.swiftchat.ai/api/bots/0210276432749689/messages"

    payload = "{\n   \"to\": \"+919764772960\",\n    \"type\": \"text\",\n    \"text\": {\n        \"body\": {responsetext} \n    }\n}"
    api_key = "21bda582-e8d0-45bc-bb8b-a5c6c555d176"
    headers = {"Authorization": f"Bearer {api_key}"}

    response = requests.request("POST", url, headers=headers, data=payload)

    #print(response.text)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=10000)

