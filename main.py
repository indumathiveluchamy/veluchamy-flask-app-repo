from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_cloud():
  return jsonify({'message': 'Hello Cloud!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)