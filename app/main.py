from flask import Flask, jsonify

app = Flask(__name__)

def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

def multiply_numbers(a, b):
    """Multiply two numbers and return the result."""
    return a * b

@app.route('/')
def hello():
    """Return a friendly greeting."""
    return jsonify({"message": "Hello, CI/CD on GCP!"})

@app.route('/add/<int:a>/<int:b>')
def add_route(a, b):
    """API endpoint to add two numbers."""
    result = add_numbers(a, b)
    return jsonify({"result": result})

@app.route('/multiply/<int:a>/<int:b>')
def multiply_route(a, b):
    """API endpoint to multiply two numbers."""
    result = multiply_numbers(a, b)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)