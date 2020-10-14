from flask import Flask,render_template
app = Flask(__name__)

@app.route('/<user_name>/<int:id>')
def hello_world(user_name=None):
    return render_template('hello.html',name=user_name,id_1=id)