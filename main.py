from flask import Flask, jsonify, render_template, request
from flask import request
from flask_mysqldb import MySQL
import random

app = Flask(__name__)
 
app = Flask(__name__)
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskapi'
 
mysql = MySQL(app)

@app.route('/', methods=['GET'])
def home():
    return render_template("input.html")

name = 2
@app.route('/api', methods=['GET','POST'])
def diff():
    if request.method == 'POST':
        name = request.args.get('hello')           ##changed it from request.form('hello') to  request.args.get('hello')  as we are using postman now
        cur = mysql.connection.cursor()
        cur.execute("select * from name where Name=(%s)", [name])
        fet = cur.fetchone()
        if fet == None:
            cur.execute("INSERT INTO name(Name) VALUES (%s)",[name])
            mysql.connection.commit()
            cur.close()
            return jsonify({"result" : "sanitized"})
        else:
            cur.close()
            return jsonify({"result" : "unsanitized"})

    return render_template("input.html")
   
    # inp = name["payload"]
    # ans = ["sanitized", "unsanitized"]
    # return jsonify({"result" : random.choice(ans)})
    # # return request.json
    # print(jsonify(answer))


if __name__ == "__main__":
    app.run(debug=True)