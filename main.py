from flask import Flask, jsonify, render_template
from flask import request
import random


from flask import Flask
app = Flask(__name__)

@app.route('/api', methods=['POST'])
def hello_world():
    name = request.form.get("hello")
    print(name)
    # inp = name["payload"]
    ans = ["sanitized", "unsanitized"]
    return jsonify({"result" : random.choice(ans)})
    # return request.json
    # print(jsonify(answer))

@app.route('/')
def home():
    return render_template("input.html")


if __name__ == "__main__":
    app.run(debug=True)