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
    return jsonify(response.text)

    # if user input is not valid, it'll notify the user accordingly and then give them a fact about some random generated number



if __name__ == '__main__':
    app.run(debug=True)
