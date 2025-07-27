# app/server.py

from flask import Flask, request, jsonify
from app.model import predict
from app.preprocess import preprocess_input

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def fraud_prediction():
    try:
        json_data = request.get_json()
        data_df = preprocess_input(json_data)
        result = predict(data_df)
        return jsonify({'fraudulent': bool(result)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
