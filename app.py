from flask import Flask, render_template

app = Flask(__name__)

products = [
    {"name": "Wireless Headphones", "price": "₹1,999"},
    {"name": "Smart Watch", "price": "₹2,499"},
    {"name": "Gaming Mouse", "price": "₹899"},
    {"name": "Mechanical Keyboard", "price": "₹2,999"}
]

@app.route("/")
def home():
    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)