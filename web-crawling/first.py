from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello World"


if __name__ == "__main__":
    app.run(host="localhost")
    # print(host)