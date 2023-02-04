import json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def main():
    return "hello world 123"

@app.route("/hello_world", methods = ["GET"])
def hello_world():
    return "another hello world page"

@app.route("/my_ml_model", methods = ["GET"])
def my_ml_model():
    a=3;b=5
    return f"{a+b}"

# @app.route("/<string:str>", methods = ["GET"])
# def dynamic_string(str):
#     return f"hello from {str}"

# @app.route("/<int:value>", methods = ["GET"])
# def dynamic_integer(value):
#     return f"value = {value}"

@app.route("/   ", methods = ["GET"])
def json_data():
    dict_ = {
        "name":"awais",
        "class":"KAI"
    }
    return dict_

@app.route("/status_code", methods = ["GET"])
def status_code():
    try:
        print(1/0)
        return "successful", 200
    except:
        return "failed", 500

@app.route("/arguments", methods = ["GET"])
def arguments():
    try:
        page = request.args.get('page')
        name = request.args.get('name')
        all_params = request.args.to_dict()
        # return f"page is: {page} \n name is: {name}"
        return jsonify(all_params), 200
    except:
        return "page error", 500

@app.route("/send_data", methods = ["GET", "POST"])
def send_data():
    if request.method == "GET":
        return "invalid method call", 500
    if request.method == "POST":
        if request.content_type == 'application/json':
            data = request.json
        else:
            data = request.data
        
        print(data)
        return jsonify(data), 200


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port= 8000)
