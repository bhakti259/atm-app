# app.py
from flask import Flask, request, jsonify, render_template
from atm import Atm

app = Flask(__name__)

atm = Atm()  # single ATM instance

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/create_pin', methods=['POST'])
def create_pin():
    data = request.json
    message = atm.create_pin(data['pin'])
    return jsonify({"message": message})

@app.route('/api/deposit', methods=['POST'])
def deposit():
    data = request.json
    message = atm.deposit(data['pin'], data['amount'])
    return jsonify({"message": message})

@app.route('/api/withdraw', methods=['POST'])
def withdraw():
    data = request.json
    message = atm.withdraw(data['pin'], data['amount'])
    return jsonify({"message": message})

@app.route('/api/check_balance', methods=['POST'])
def check_balance():
    data = request.json
    message = atm.check_balance(data['pin'])
    return jsonify({"message": message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
