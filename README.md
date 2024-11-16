# PCOD-Prediction and Dashboard 
**Overview**
This project leverages machine learning to predict the likelihood of Polycystic Ovary Syndrome (PCOS) based on patient data. It features an interactive Streamlit dashboard for real-time predictions, detailed insights, and visualizations. Designed to assist clinicians, researchers, and individuals, this tool provides a data-driven approach for early PCOS detection and management.PCOS affects millions of individuals worldwide, and early detection is critical for effective management. By combining machine learning models and an intuitive interface, this project aims to make predictive technology accessible and actionable.

**Features
1. Prediction Models**
Implemented and evaluated multiple machine learning algorithms:
Logistic Regression
Naive Bayes
Support Vector Machines (SVM)
Decision Trees
_Evaluated models using metrics:_
_Accuracy, Precision, Recall, F1-score, and ROC-AUC._
**2. Interactive Dashboard**
Built using Streamlit, the dashboard allows users to:
Input patient symptoms and health data.
Receive predictions about the likelihood of PCOS.
View probabilities and gain actionable insights for clinical decisions.
**3. Explainable AI
Used SHAP Analysis to:**
Identify the most important features contributing to predictions.
Enhance transparency and trust in the model.
**4. Data Insights**
Features like irregular periods, cycle length, and symptom severity score emerged as critical predictors of PCOS.
Provides a comprehensive understanding of PCOS risk factors.


**Project Files**
-dashboard.py: Code for the Streamlit dashboard.
-PCOD Project.ipynb: Jupyter Notebook for exploratory data analysis (EDA), feature engineering, and model training.
-allData.csv: Dataset containing patient symptoms and medical information.



**requirements.txt: 
**
Python dependencies required to run the project.
**How to Run the Project**
_1. Clone the Repository_

git clone https://github.com/RaagaLikhithaM/PCOD-Prediction.git

cd PCOD-Prediction

_2. Install Dependencies_

Use the requirements.txt file to install the necessary Python libraries:

pip install -r requirements.txt

_3. Run the Streamlit Dashboard_
_Launch the dashboard locally:_
-streamlit run dashboard.py
-Open the URL provided by Streamlit in your browser (e.g., http://localhost:8501).

**Technologies Used**
Python: For analysis and development.
Streamlit: For the interactive dashboard.
scikit-learn: For machine learning models.
SHAP: For feature importance analysis.
Pandas & NumPy: For data manipulation.
Jupyter Notebook: For prototyping and exploratory analysis.
**Key Insights**
Feature Importance: Features like irregular periods, symptom severity, and cycle length were highly predictive of PCOS.
Model Performance: Naive Bayes performed well, with a balance between accuracy and interpretability.
User-Friendly Dashboard: The Streamlit app provides accessible predictions for non-technical users.
**Impact**
This project has the potential to:
Reduce time-to-diagnosis for PCOS.
Provide clinicians with actionable data insights.
Empower individuals with predictive tools for better health management.

**Contact**
Developer: Raaga Likhitha
Email: dr.raagalikhitha@gmail.com
