from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    print("Servidor está rodando em http://127.0.0.1:5000")
    app.run(debug=True)