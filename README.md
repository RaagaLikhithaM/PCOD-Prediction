# PCOD-Prediction
PCOS Prediction and Dashboard
Overview
This project leverages machine learning to predict the likelihood of Polycystic Ovary Syndrome (PCOS) based on patient data. It features an interactive Streamlit dashboard that provides real-time predictions, detailed insights, and visualizations. This tool is designed to assist clinicians, researchers, and individuals in understanding the potential risk of PCOS through a data-driven approach.

PCOS affects millions of individuals worldwide, and early detection is critical for effective management. By combining machine learning models and an intuitive interface, this project aims to make predictive technology accessible and actionable.

Features
1. Prediction Models
Multiple machine learning algorithms were tested, including:
Logistic Regression
Naive Bayes
Support Vector Machines (SVM)
Decision Trees
Each model was evaluated using metrics like accuracy, precision, recall, F1-score, and ROC-AUC.
2. Interactive Dashboard
Built using Streamlit, the dashboard allows users to:
Input patient symptoms and health data.
Receive predictions about the likelihood of PCOS.
View the probability of PCOS occurrence.
Gain actionable insights to guide clinical decisions.
3. Explainable AI
SHAP Analysis was implemented to:
Identify the most influential features in the prediction.
Increase transparency and trust in the model.
4. Data-Driven Insights
Features like irregular periods, cycle length, and symptom severity score emerged as critical predictors.
Provides a comprehensive understanding of the factors contributing to PCOS.
Project Files
dashboard.py: Streamlit application for real-time predictions.
PCOD Project.ipynb: Jupyter Notebook for exploratory data analysis (EDA), feature engineering, and model training.
allData.csv: Dataset containing patient symptoms and medical information.
requirements.txt: Python dependencies required to run the project.
How to Run the Project
Step 1: Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/PCOD-Prediction.git
cd PCOD-Prediction
Step 2: Install Dependencies
Install all required Python libraries:

bash
Copy code
pip install -r requirements.txt
Step 3: Run the Streamlit Dashboard
Launch the dashboard locally:

bash
Copy code
streamlit run dashboard.py
Open the URL provided by Streamlit in your browser (e.g., http://localhost:8501).

Technologies Used
Python: Programming language for analysis and development.
Streamlit: For building the interactive dashboard.
scikit-learn: For machine learning model training and evaluation.
SHAP: For feature importance analysis.
Pandas & NumPy: For data manipulation.
Jupyter Notebook: For prototyping and exploratory analysis.
Key Insights
Feature Importance:
Features like irregular periods, symptom severity, and cycle length play a crucial role in predicting PCOS.
Model Performance:
Naive Bayes performed well, but Decision Trees provided better interpretability.
User-Friendly Interface:
The Streamlit dashboard makes predictions accessible to non-technical users.
Impact
This project has the potential to revolutionize early PCOS diagnosis by:

Reducing time-to-diagnosis.
Offering data-driven insights to clinicians.
Empowering individuals to make informed health decisions.
Contact
Developer: Raaga Likhitha
Email: dr.raagalikhitha@gmail.com

