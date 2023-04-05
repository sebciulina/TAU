from flask import Flask, jsonify, request
from payment_gateway import PaymentGateway

app = Flask(__name__)

@app.route('/payment/charge', methods=['POST'])
def charge():
    payment_data = request.json
    gateway = PaymentGateway()
    response = gateway.process_payment(payment_data)
    return jsonify(response)

if __name__ == '__main__':
    app.run()