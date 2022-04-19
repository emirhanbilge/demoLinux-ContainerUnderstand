
#!/usr/bin/python


from flask import Flask
from flask import render_template , redirect
import sys




app = Flask(__name__)


@app.route('/')
def index():
    return "Server port on : "+sys.argv[1]+ "working"


if __name__ == "__main__":
    app.run("localhost",port=sys.argv[1])
