```markdown
# ⚙️ Predictive Maintenance System

A Flask-based web application that predicts and classifies equipment failures in industrial systems using a trained machine learning model. The system leverages real-time sensor data inputs to detect faults like:

- 🔥 Heat Dissipation Failure  
- ⚡ Power Failure  
- 🏋️ Overstrain Failure  
- 🛠️ Tool Wear Failure  

This helps industries take preventive actions before costly breakdowns occur.

---

## 🚀 Features

- 🔮 Real-time fault prediction using a trained ML model (model.pkl).  
- 🌐 Supports both form-based inputs (via web UI) and API-based inputs (/predict_api).  
- 🖥️ Interactive Flask web interface for visualization.  
- 📊 Scalable with proper preprocessing (scaling.pkl).  

---

## 🛠️ Tech Stack

- 🐍 Python 3.7+  
- ⚡ Flask (Backend & API)  
- 🤖 Scikit-learn (ML Model)  
- 🎨 HTML (Jinja2 templates) for frontend  
- 🔢 NumPy & Pickle (Preprocessing & Model Persistence)  

---

## 📂 Project Structure

```

predictive\_maintenance/
│── static/                 # Static assets (CSS, JS, Images)
│── templates/
│   └── home.html           # Web UI template
│── model.pkl               # Trained ML model
│── scaling.pkl             # Pre-fitted scaler
│── app.py                  # Flask application
│── requirements.txt        # Project dependencies
│── README.md               # Project documentation

````

---

## ⚡ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/SujaySAK777/predictive_maintenance.git
cd predictive_maintenance
````

### 2️⃣ Create a Virtual Environment

Using conda:

```bash
conda create -p venv python==3.7 -y
conda activate venv/
```

Using venv:

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
python app.py
```

Flask will start at 👉 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 📌 Usage

### 🌐 Web Interface

* Open browser → [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
* Enter sensor values:

  * Air Temperature
  * Process Temperature
  * Rotational Speed
  * Torque
  * Tool Wear
* Click Predict → The system will display the failure type.

### 🔗 API Endpoint

Send a POST request to /predict\_api

Request Example (JSON):

```json
{
  "data": {
    "air_temperature": 298,
    "process_temperature": 310,
    "rotational_speed": 1400,
    "torque": 40,
    "tool_wear": 120
  }
}
```

Response Example:

```json
{
  "prediction": "Heat Dissipation Failure"
}
```

---

## 📜 Requirements

* Python 3.7+
* Flask
* NumPy
* Scikit-learn
* Pickle

Install via:

```bash
pip install -r requirements.txt
```

---

## 🔮 Future Improvements

* 🚀 Deploy on Heroku / Render / AWS for cloud access
* 📊 Add data visualization dashboards
* 🤖 Enhance model with deep learning for better accuracy

```
```
