# Gauge Meter
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=risk_percent,

    number={"suffix":"%"},

    title={"text":"Exam Fail Risk"},

    gauge={
        "axis":{"range":[0,100]},

        "bar":{"color":"#FF8C00"},  # Orange needle/bar

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

# Risk Categories & Recommendations

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
        "The student is progressing well but should maintain consistent study habits."
    )

elif risk_percent < 60:

    st.warning(
        f"⚠️ Moderate Risk ({risk_percent}%)"
    )

    st.write(
        "The student may benefit from additional revision and practice papers."
    )

elif risk_percent < 80:

    st.warning(
        f"⚠️ High Risk ({risk_percent}%)"
    )

    st.write(
        "The student should increase study time and seek additional academic support."
    )

else:

    st.error(
        f"🚨 Critical Risk ({risk_percent}%)"
    )

    st.write(
        "Immediate intervention is strongly recommended to reduce the risk of failure."
    )
