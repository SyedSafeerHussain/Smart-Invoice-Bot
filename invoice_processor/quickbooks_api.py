from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy in-memory database (just for testing)
invoices_db = []

@app.route('/invoices', methods=['POST'])
def create_invoice():
    invoice_data = request.json
    if not invoice_data:
        return jsonify({'error': 'No invoice data provided'}), 400

    invoices_db.append(invoice_data)  # simulate saving to DB
    return jsonify({'message': 'Invoice received successfully', 'data': invoice_data}), 201

@app.route('/invoices', methods=['GET'])
def get_all_invoices():
    return jsonify({'invoices': invoices_db})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
