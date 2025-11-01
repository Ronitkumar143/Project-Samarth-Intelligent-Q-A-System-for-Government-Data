# Project-Samarth-Intelligent-Q-A-System-for-Government-Data


🧠 Overview

Project Samarth is an end-to-end intelligent Question-Answering (Q&A) system designed to interact with real datasets from the Indian Government’s data.gov.in
 portal.
It enables policymakers, researchers, and citizens to query agricultural and climate data using natural language questions, helping derive cross-domain insights for data-driven decisions.

🚀 Features

🔍 Natural Language Q&A — Ask questions like:
“Compare rainfall in Bihar and Jharkhand over the past 5 years.”
“Which district had the highest rice production in 2023?”

🌦️ Real-Time Data Integration — Uses datasets from:

Ministry of Agriculture & Farmers Welfare

India Meteorological Department (IMD)

📊 Dynamic Visualization — Auto-generates charts and tables for quick insight.

📚 Source Traceability — Every answer includes the dataset it came from.

🧩 Modular Architecture — Separated into frontend (Streamlit app) and backend (data integration and query planner).

🔒 Privacy & Data Sovereignty — Designed for secure, local deployment.

🏗️ Project Structure
Project-Samarth-QA/
├── backend/
│   ├── data_loader.py
│   ├── query_planner.py
│   └── utils.py
├── frontend/
│   └── app.py
├── data/
│   └── sample_agriculture_dataset.csv
├── requirements.txt
└── README.md

⚙️ Tech Stack
Component	Technology
Frontend	Streamlit
Backend	Python
Data Handling	Pandas, NumPy
Visualization	Matplotlib, Seaborn
ML (Optional)	Scikit-learn
Deployment	Localhost / Streamlit Cloud
🧩 Setup & Run Instructions
1️⃣ Clone the Repository
git clone [https://github.com/Ronitkumar143/Project-Samarth-QA.git](https://github.com/Ronitkumar143/Project-Samarth-Intelligent-Q-A-System-for-Government-Data)
cd Project-Samarth-QA

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the App
set PYTHONPATH=. && streamlit run frontend/app.py


(For Linux/Mac)

export PYTHONPATH=. && streamlit run frontend/app.py

🧠 Sample Questions You Can Ask

“Compare the average annual rainfall in Bihar and Jharkhand for the last 5 years.”

“Which district in Maharashtra had the highest wheat production in 2024?”

“How has rice production in Uttar Pradesh changed over the last decade compared to rainfall trends?”

🎯 Future Improvements

Integration with live APIs from data.gov.in

Add GPT-based summarization layer for complex insights

Expand datasets to include economic and environmental factors

Enable voice-based Q&A

👨‍💻 Author

Ronit Kumar
🎓 B.Sc Student, IIT Patna
💡 Data Science | Machine Learning | Web Development
🔗 GitHub Profile
