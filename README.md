****************************************************************************************
🌟⚙️⚡  PREDICTIVE MAINTENANCE SYSTEM  ⚡⚙️🌟
****************************************************************************************

A Flask-based web application that predicts and classifies equipment failures in industrial systems
using a trained machine learning model. Leverages real-time sensor data 🔧 to detect and prevent costly breakdowns 💥.

----------------------------------------------------------------------------------------
🔥 FAILURE TYPES 🔥
----------------------------------------------------------------------------------------
- Heat Dissipation Failure 🔥
- Power Failure ⚡
- Overstrain Failure 🏋️
- Tool Wear Failure 🛠️

----------------------------------------------------------------------------------------
🚀 FEATURES 🚀
----------------------------------------------------------------------------------------
- Real-time fault prediction using a trained ML model (model.pkl) 🔮
- Supports Web UI (form inputs) and API (/predict_api) 🌐
- Interactive Flask web interface 🖥️
- Scalable preprocessing (scaling.pkl) 📊

----------------------------------------------------------------------------------------
🛠️ TECH STACK 🛠️
----------------------------------------------------------------------------------------
- Python 3.7+ 🐍
- Flask (Backend & API) ⚡
- Scikit-learn (ML Model) 🤖
- HTML (Jinja2 templates) for frontend 🎨
- NumPy & Pickle for preprocessing and model persistence 🔢

----------------------------------------------------------------------------------------
⚡ INSTALLATION & SETUP ⚡
----------------------------------------------------------------------------------------
1. Clone the Repository
   git clone https://github.com/SujaySAK777/predictive_maintenance.git
   cd predictive_maintenance

2. Create Virtual Environment
   Using conda:
       conda create -p venv python=3.7 -y
       conda activate venv/
   Using venv:
       python -m venv venv
       # Mac/Linux
       source venv/bin/activate
       # Windows
       venv\Scripts\activate

3. Install Dependencies
   pip install -r requirements.txt

4. Run the Application
   python app.py
   Access the app at: http://127.0.0.1:5000/

----------------------------------------------------------------------------------------
📌 USAGE 📌
----------------------------------------------------------------------------------------
Web Interface:
- Open http://127.0.0.1:5000/
- Enter sensor values:
    Air Temperature 🌡️
    Process Temperature 🌡️
    Rotational Speed 🔄
    Torque 🌀
    Tool Wear 🛠️
- Click Predict → System displays the failure type ✅

API Endpoint:
- Send a POST request to /predict_api
- Request Example:
    {
      "data": {
        "air_temperature": 298,
        "process_temperature": 310,
        "rotational_speed": 1400,
        "torque": 40,
        "tool_wear": 120
      }
    }
 - Response Example:
    {
      "prediction": "Heat Dissipation Failure 🔥"
    }

----------------------------------------------------------------------------------------
🔮 FUTURE IMPROVEMENTS 🔮
----------------------------------------------------------------------------------------
- Deploy on Heroku / Render / AWS ☁️
- Add interactive data visualization dashboards 📊
- Enhance model with deep learning for better accuracy 🤖

****************************************************************************************
✨ Built with Python & Flask 🐍✨
****************************************************************************************
