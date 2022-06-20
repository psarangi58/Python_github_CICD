from flask import Flask

app=Flask(__name__)

@app.route("/")
def  home():
    return "Hello World"

@app.route("/home")
def index():
    return "<h1>Good Morning</h1>"

if __name__=="__main__":
    app.run()