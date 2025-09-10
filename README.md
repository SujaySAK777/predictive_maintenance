⚙️ Predictive Maintenance System

A Flask-based web application that predicts and classifies equipment failures in industrial systems using a trained machine learning model.
The system leverages real-time sensor data inputs to detect faults like:

Heat Dissipation Failure

Overstrain Failure

Power Failure

Tool Wear Failure

This helps industries take preventive actions before costly breakdowns occur.

🚀 Features

Real-time fault prediction using a trained ML model (model.pkl).

Supports both form-based inputs (via web UI) and API-based inputs (via /predict_api).

Interactive Flask web interface for visualization.

Scalable with proper preprocessing (scaling.pkl).

🛠️ Tech Stack

Python 3.7+

Flask (Backend & API)

Scikit-learn / ML Model (for prediction)

HTML (Jinja2 templates) for frontend

NumPy & Pickle for preprocessing and model persistence

📂 Project Structure
predictive_maintenance/
│── static/                 # Static assets (CSS, JS, Images)
│── templates/
│   └── home.html           # Web UI template
│── model.pkl               # Trained ML model
│── scaling.pkl             # Pre-fitted scaler
│── app.py                  # Flask application
│── requirements.txt        # Project dependencies
│── README.md               # Project documentation

⚡ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/SujaySAK777/predictive_maintenance.git
cd predictive_maintenance

2️⃣ Create a Virtual Environment

Using conda:

conda create -p venv python==3.7 -y
conda activate venv/


Or using venv:

python -m venv venv
source venv/bin/activate  # for Mac/Linux
venv\Scripts\activate     # for Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
python app.py


Flask will start at:
👉 http://127.0.0.1:5000/

📌 Usage
🌐 Web Interface

Open browser and go to http://127.0.0.1:5000/.

Enter sensor values:

Air Temperature

Process Temperature

Rotational Speed

Torque

Tool Wear

Click Predict → It will show the type of failure.

🔗 API Endpoint

You can also send a JSON POST request to /predict_api:

Request Example (JSON):

{
  "data": {
    "air_temperature": 298,
    "process_temperature": 310,
    "rotational_speed": 1400,
    "torque": 40,
    "tool_wear": 120
  }
}


Response Example:

{
  "prediction": "Heat Dissipation Failure"
}

📜 Requirements

Python 3.7+

Flask

NumPy

Scikit-learn

Pickle

Install via:

pip install -r requirements.txt

🔮 Future Improvements

✅ Deploy on Heroku / Render / AWS for cloud access.

✅ Add data visualization dashboards.

✅ Enhance model with deep learning for better accuracy.
