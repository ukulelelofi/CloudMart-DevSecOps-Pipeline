from flask import Flask, render_template

app = Flask(__name__)

PRODUCTS = [
    {"name": "CloudMart Laptop", "price": 2499},
    {"name": "Secure Headset", "price": 299},
    {"name": "DevSecOps Hoodie", "price": 159},
]

@app.route("/")
def home():
    return render_template("index.html", products=PRODUCTS)

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)