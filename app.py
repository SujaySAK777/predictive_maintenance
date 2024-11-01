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

@app.route('/predict', methods=['POST'])
def predict():
    # Gather data from form inputs and convert to float
    data = [float(x) for x in request.form.values()]
    
    # Transform the input using the pre-loaded scaler
    final_input = scaler.transform(np.array(data).reshape(1, -1))
    print("Transformed Input:", final_input)
    
    # Make a prediction using the model
    output = model.predict(final_input)[0]
    
    # Display prediction result in a user-friendly format
    return render_template("home.html", prediction_text="The failure is: {}".format(output))


if __name__ == "__main__":
    app.run(debug=True)
