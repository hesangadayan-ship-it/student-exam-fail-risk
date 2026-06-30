import streamlit as st
import pickle
import numpy as np
import plotly.graph_objects as go

# Load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Page title
st.title("🎓 Student Exam Fail Risk Prediction")

st.write(
    "Enter the student details below to predict the risk of failing an exam."
)

# Input fields
hours = st.number_input(
    "Hours Studied",
    min_value=0.0,
    max_value=24.0,
    value=5.0
)

previous = st.number_input(
    "Previous Scores",
    min_value=0.0,
    max_value=100.0,
    value=50.0
)

activity = st.selectbox(
    "Extracurricular Activities",
    ["Yes", "No"]
)

activity = 1 if activity == "Yes" else 0

sleep = st.number_input(
    "Sleep Hours",
    min_value=0.0,
    max_value=24.0,
    value=7.0
)

papers = st.number_input(
    "Sample Question Papers Practiced",
    min_value=0,
    max_value=50,
    value=5
)

# Predict button
if st.button("Predict Risk"):

    data = np.array([[
        hours,
        previous,
        activity,
        sleep,
        papers
    ]])

    # Probability of Fail_Risk = 1
    probability = model.predict_proba(data)[0][1]

    risk_percent = round(
        probability * 100,
        1
    )

    # Gauge Meter
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=risk_percent,

        number={"suffix":"%"},

        title={"text":"Exam Fail Risk"},

        gauge={
            "axis":{"range":[0,100]},

            "bar":{"color":"red"},

            "steps":[
                {"range":[0,40],"color":"green"},
                {"range":[40,70],"color":"yellow"},
                {"range":[70,100],"color":"red"}
            ]
        }
    ))

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # Risk Category
    if risk_percent < 40:
        st.success(
            f"Low Risk ({risk_percent}%)"
        )

    elif risk_percent < 70:
        st.warning(
            f"Medium Risk ({risk_percent}%)"
        )

    else:
        st.error(
            f"High Risk ({risk_percent}%)"
        )
