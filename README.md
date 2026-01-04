# Employee Promotion Prediction App

This project is a web-based machine learning application that predicts whether an employee is likely to be promoted based on historical performance and demographic data. The application was developed as part of an Analytics Vidhya hackathon and deployed using Streamlit Community Cloud.

---

## Problem Statement

Employee promotions are critical decisions that impact workforce motivation and organizational growth.  
The objective of this project is to build a machine learning model that can predict whether an employee will be promoted, using past performance indicators and employee attributes.

---

## Dataset

The dataset is sourced from an Analytics Vidhya HR Analytics problem and includes features such as:
- Department
- Region
- Education
- Gender
- Recruitment channel
- Number of trainings
- Age
- Previous year rating
- Length of service
- KPIs met (>80%)
- Awards won
- Average training score

Target variable:
- **is_promoted** (0 = Not promoted, 1 = Promoted)

---

## Model & Approach

- **Model**: RandomForest Classifier  
- **Pipeline**:
  - Numerical features: Median imputation
  - Categorical features: Most-frequent imputation + OneHotEncoding
  - End-to-end pipeline built using `ColumnTransformer` and `Pipeline`
- **Evaluation**:
  - Model evaluated using Analytics Vidhya’s leaderboard metric
  - Best submission score achieved on the platform

The final trained pipeline was serialized using `pickle`.

---

## Web Application (Streamlit)

The Streamlit app allows users to:
- Input employee details via an interactive UI
- Preview the input data
- Get a real-time prediction (`Promoted` / `Not Promoted`)

The model is loaded once using Streamlit caching for faster inference.

---

## Deployment

- **Framework**: Streamlit
- **Hosting**: Streamlit Community Cloud
- **Deployment Type**: Public web application
- **Model Loading**: Pickled scikit-learn pipeline

**Live App URL**: (https://employee-promotion-app-lswmhc3zmvtbb3kpjvpvup.streamlit.app/)

---

## Project Structure

employee-promotion-streamlit/
│
├── app.py # Streamlit application code
├── promotion_model.pkl # Trained ML pipeline (pickle file)
├── requirements.txt # Python dependencies
├── runtime.txt # Python version (python-3.11)
└── README.md # Project documentation

---

## How to Run Locally

1. Clone the repository: git clone https://github.com/<your-username>/employee-promotion-streamlit.git
                         cd employee-promotion-streamlit
2. Create and activate a virtual environment (optional but recommended)

3. Install dependencies: pip install -r requirements.txt

4. Run the Streamlit app: streamlit run app.py

5. Open the app in your browser: http://localhost:8501

---

## Testing and Validation

- Tested with multiple user input scenarios:
    - Strong promotion candidate
    - Weak promotion candidate
    - Edge cases (missing ratings, varied regions)

- Application handles missing values and unseen categories gracefully
- No runtime crashes during inference

---

## Limitations

- Class imbalance could be addressed using advanced resampling techniques
- Additional models (XGBoost, LightGBM) could be explored
- Feature importance and explainability (SHAP) can be added
- REST API deployment using FastAPI + Cloud Run (future enhancement)

---

Author

Sathyan Asokan Geethpriya
Analytics Vidhya Hackathon Participant
