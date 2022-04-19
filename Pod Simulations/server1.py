from flask import Flask
from flask import render_template , redirect


app = Flask(__name__)




@app.route('/')
def index():
    return "Server 1 working"



if __name__ == "__main__":
    app.run("localhost",port=5001)

