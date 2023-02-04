from flask import Flask, jsonify, request
app = Flask(__name__)

list = ["task1", "task2", "task3"]

@app.route('/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

@app.route('/main', methods=['GET', 'POST'])
def main():
    return "main page!"

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>', methods=['GET', 'POST'])
# def pages(path):
#     return f"on page number {path}!"

@app.route('/<int:number>', methods=['GET', 'POST'])
def pages(number):
    return f"on page number {number}!"

@app.route('/jsonify', methods=['GET', 'POST'])
def user_data():
    return jsonify({'name':'paul', 'age':12})

@app.route('/arguments', methods = ['GET'])
def get_args():
    # print(request.args.listvalues())
    print(request.args.to_dict())
    return request.args.to_dict()


@app.route('/send_data', methods=['POST'])
def send_data():
    data = request.json
    data['name']
    return data

# if __name__ == '__main__':
app.run(host='0.0.0.0', port=105, debug=True)


# welcome page
# list tasks
# add task
# deletes
