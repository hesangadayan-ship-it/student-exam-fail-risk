import streamlit as st
import pickle
import numpy as np
import plotly.graph_objects as go

# Load model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Title
st.title("🎓 Student Exam Fail Risk Prediction")

st.write(
    "Enter the student details below to predict the risk of failing an exam."
)

# Inputs
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

# Predict
if st.button("Predict Risk"):

    data = np.array([[
        hours,
        previous,
        activity,
        sleep,
        papers
    ]])

    probability = model.predict_proba(data)[0][1]

    risk_percent = round(
        probability * 100,
        1
    )

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=risk_percent,

        number={"suffix":"%"},

        title={"text":"Exam Fail Risk"},

        gauge={
            "axis":{"range":[0,100]},

            "bar":{"color":"brown"},

            "steps":[
                {"range":[0,20],"color":"darkgreen"},
                {"range":[20,40],"color":"green"},
                {"range":[40,60],"color":"yellow"},
                {"range":[60,80],"color":"orange"},
                {"range":[80,100],"color":"red"}
            ]
        }
    ))

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # Risk Categories

    if risk_percent < 20:

        st.success(
            f"✅ Very Low Risk ({risk_percent}%)"
        )

        st.write(
            "The student is performing very well and is highly unlikely to fail."
        )

    elif risk_percent < 40:

        st.success(
            f"✅ Low Risk ({risk_percent}%)"
        )

        st.write(
            "The student is progressing well but should maintain current study habits."
        )

    elif risk_percent < 60:

        st.warning(
            f"⚠️ Moderate Risk ({risk_percent}%)"
        )

        st.write(
            "Additional revision and practice are recommended."
        )

    elif risk_percent < 80:

        st.warning(
            f"⚠️ High Risk ({risk_percent}%)"
        )

        st.write(
            "The student should increase study time and seek academic support."
        )

    else:

        st.error(
            f"🚨 Critical Risk ({risk_percent}%)"
        )

        st.write(
            "Immediate intervention is strongly recommended."
        )
