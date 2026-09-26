import streamlit as st
import pandas as pd
import joblib
import sklearn
# ---------------- PAGE ----------------
st.set_page_config(
    page_title="Employee Attrition Prediction",
    page_icon="👤",
    layout="centered"
)

# ---------------- TITLE ----------------
st.title("👤 Employee Attrition Prediction")
st.write("Enter employee details to predict the probability of attrition.")

st.divider()

# ---------------- INPUTS ----------------
col1, col2= st.columns(2)

with col1:
    age = st.number_input("Age", 18, 65, 30)

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    marital_status = st.selectbox(
        "Marital Status",
        ["Single", "Married", "Divorced"]
    )

    number_of_dependents = st.number_input(
        "Number of Dependents",
        0, 10, 0
    )

    job_role = st.selectbox(
        "Job Role",
        ['Education', 'Media', 'Healthcare', 'Technology', 'Finance']
    )

    job_level = st.selectbox(
        "Job Level",
        ["Entry", "Mid", "Senior", "Executive"]
    )

    education_level = st.selectbox(
        "Education Level",
        ['Associate Degree', 'Master’s Degree', 'Bachelor’s Degree',
       'High School', 'PhD']
    )

    monthly_income = st.number_input(
        "Monthly Income",
        min_value=0,
        value=5000
    )

    years_at_company = st.number_input(
        "Years at Company",
        0, 50, 5
    )

    company_tenure = st.number_input(
        "Company Tenure",
        0, 50, 5
    )

    number_of_promotions = st.number_input(
        "Number of Promotions",
        0, 3, 0
    )
with col2:
   
    job_satisfaction = st.selectbox(
        "Job Satisfaction",
        ["Low", "Medium", "High", "Very High"]
    )

    performance_rating = st.selectbox(
        "Performance Rating",
        ["Low", "Average", "High", "Excellent"]
    )

    work_life_balance = st.selectbox(
        "Work-Life Balance",
        ["Poor", "Fair", "Good", "Excellent"]
    )

    overtime = st.selectbox(
        "Overtime",
        ["Yes", "No"]
    )

    remote_work = st.selectbox(
        "Remote Work",
        ["Yes", "No"]
    )

    distance_from_home = st.number_input(
        "Distance from Home",
        0, 200, 10
    )

    company_size = st.selectbox(
        "Company Size",
        ["Small", "Medium", "Large"]
    )

    company_reputation = st.selectbox(
        "Company Reputation",
        ["Poor", "Fair", "Good", "Excellent"]
    )

    employee_recognition = st.selectbox(
        "Employee Recognition",
        ["Low", "Medium", "High","Very High"]
    )

    leadership_opportunities = st.selectbox(
        "Leadership Opportunities",
        ["Yes", "No"]
    )

    innovation_opportunities = st.selectbox(
        "Innovation Opportunities",
        ["Yes", "No"]
    )
st.divider()

# ---------------- PREDICT ----------------
if st.button("🔮 Predict Attrition", use_container_width=True):

    # Create input dataframe
    input_data = pd.DataFrame({
    "age": [age],
    "gender": [gender],
    "marital_status": [marital_status],
    "number_of_dependents": [number_of_dependents],
    "job_role": [job_role],
    "job_level": [job_level],
    "education_level": [education_level],
    "monthly_income": [monthly_income],
    "years_at_company": [years_at_company],
    "company_tenure": [company_tenure],
    "number_of_promotions": [number_of_promotions],
    "job_satisfaction": [job_satisfaction],
    "performance_rating": [performance_rating],
    "work_life_balance": [work_life_balance],
    "overtime": [overtime],
    "remote_work": [remote_work],
    "distance_from_home": [distance_from_home],
    "company_size": [company_size],
    "company_reputation": [company_reputation],
    "employee_recognition": [employee_recognition],
    "leadership_opportunities": [leadership_opportunities],
    "innovation_opportunities": [innovation_opportunities]
})

    # Load model
    try:
        model = joblib.load("employee_attrition.pkl")

        # Prediction
        prediction = model.predict(input_data)[0]

        # Probability
        # Probability
        if hasattr(model, "predict_proba"):
            
            probabilities = model.predict_proba(input_data)[0]
            classes = model.classes_

            probability = probabilities[list(classes).index(prediction)] * 100
        else:
            probability = None
        st.subheader("Prediction Result")

        if str(prediction).lower() == "left":
            st.error("⚠️ High Attrition Risk")
        else:
            st.success("✅ Low Attrition Risk")

        if probability is not None:
            st.metric(
                "Attrition Probability",
                f"{probability:.2f}%"
            )

    except FileNotFoundError:
        st.warning(
            "Model file not found. Place your "
            "`attrition_pipeline.pkl` in the same folder."
        )

    except Exception as e:
        st.error(f"Prediction error: {e}")






