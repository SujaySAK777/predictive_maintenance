import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model and scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaling.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    # Retrieve JSON data sent in the request
    data = request.json['data']
    # Transform input data for the model
    transformed_data = scaler.transform(np.array(list(data.values())).reshape(1, -1))
    # Predict using the loaded model
    output = model.predict(transformed_data)
    # Convert prediction to string, as required for predictive maintenance labels
    result = output[0]  # Example output could be labels like 'High', 'Medium', 'Low'

    # Log the prediction
    print(f"Input Data: {data}")
    print(f"Transformed Data: {transformed_data}")
    print(f"Predicted Output: {result}")
    
    # Return JSON response
    return jsonify(prediction=str(result))

if __name__ == "__main__":
    app.run(debug=True)
