from flask import Flask,jsonify,request
import json
app = Flask(__name__)


todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]


@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def post_todos():
    request_body=request.data
    decoded_object=json.loads(request_body)
    todos.append(decoded_object)

    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todos(position):
    todos.pop(position)

    return jsonify(todos)


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=3245, debug=True)