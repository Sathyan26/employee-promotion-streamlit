import streamlit as st
import pandas as pd
import pickle
from pathlib import Path

# -------------------------
# Page setup
# -------------------------
st.set_page_config(page_title="Employee Promotion Prediction", layout="centered")
st.title("Employee Promotion Prediction")
st.write("Enter employee details and click **Predict**.")

MODEL_PATH = Path(__file__).parent / "promotion_model.pkl"


# -------------------------
# Load model (cached)
# -------------------------
@st.cache_resource
def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model file not found at {MODEL_PATH}. "
            "Make sure promotion_model.pkl is in the same folder as app.py."
        )
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)


model = load_model()

# -------------------------
# Sidebar inputs
# -------------------------
with st.sidebar:
    st.header("Inputs")

    department = st.selectbox(
        "Department",
        [
            "Sales & Marketing",
            "Operations",
            "Technology",
            "Analytics",
            "R&D",
            "Procurement",
            "Finance",
            "HR",
            "Legal",
        ],
    )

    region = st.text_input("Region (e.g., region_2)", value="region_2")

    education = st.selectbox(
        "Education",
        ["Below Secondary", "Bachelor's", "Master's & above"],
    )

    gender = st.selectbox("Gender", ["m", "f"])

    recruitment_channel = st.selectbox(
        "Recruitment Channel",
        ["sourcing", "referred", "other"],
    )

    no_of_trainings = st.number_input("No. of trainings", min_value=1, max_value=50, value=1)
    age = st.number_input("Age", min_value=18, max_value=70, value=30)

    previous_year_rating_choice = st.selectbox(
        "Previous year rating",
        ["Missing", 1, 2, 3, 4, 5],
        index=0,
    )
    previous_year_rating = None if previous_year_rating_choice == "Missing" else float(previous_year_rating_choice)

    length_of_service = st.number_input("Length of service (years)", min_value=1, max_value=40, value=5)

    # IMPORTANT: these names match the renamed training columns
    kpis_met_80 = st.selectbox("KPIs met >80% (kpis_met_80)", [0, 1])
    awards_won = st.selectbox("Awards won? (awards_won)", [0, 1])

    avg_training_score = st.number_input("Avg training score", min_value=0, max_value=100, value=70)


# -------------------------
# Build input row
# -------------------------
input_df = pd.DataFrame(
    [
        {
            "department": department,
            "region": region,
            "education": education,
            "gender": gender,
            "recruitment_channel": recruitment_channel,
            "no_of_trainings": int(no_of_trainings),
            "age": int(age),
            "previous_year_rating": previous_year_rating,
            "length_of_service": int(length_of_service),
            "kpis_met_80": int(kpis_met_80),
            "awards_won": int(awards_won),
            "avg_training_score": int(avg_training_score),
        }
    ]
)

st.subheader("Input preview")
st.dataframe(input_df, use_container_width=True)

# -------------------------
# Predict
# -------------------------
if st.button("Predict"):
    try:
        pred = int(model.predict(input_df)[0])

        proba = None
        if hasattr(model, "predict_proba"):
            proba = float(model.predict_proba(input_df)[0][1])

        if pred == 1:
            st.success("✅ Prediction: PROMOTED (is_promoted = 1)")
        else:
            st.warning("❌ Prediction: NOT promoted (is_promoted = 0)")

        if proba is not None:
            st.write(f"Promotion probability: **{proba:.3f}**")

    except Exception as e:
        st.error("Prediction failed. This usually happens if input columns don't match the model training columns.")
        st.exception(e)

st.caption("Model: scikit-learn pipeline (preprocessing + classifier) trained on the Analytics Vidhya promotion dataset.") 
