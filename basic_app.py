from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/json', methods=['GET'])
def send_json():
    data = {"message": 'hello', "status": 'success'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)