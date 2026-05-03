import streamlit as st
import requests

API_URL = "https://text-classification-production-41b5.up.railway.app/predict"

st.set_page_config(
    page_title="Text Classification App",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Text Classification App")
st.write("Enter a text and get its category prediction instantly.")

# 📝 Input
user_input = st.text_area("✍️ Enter your text here:")

# 🔘 Button
if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        with st.spinner("Analyzing text... 🤖"):
            response = requests.post(API_URL, json={"text": user_input})

        if response.status_code == 200:
            result = response.json()

            st.success("Prediction Result 🎯")

            st.markdown("### 🏷️ Category")
            st.markdown(f"**{result.get('prediction', 'N/A')}**")

            if "confidence" in result:
                st.markdown("### 📊 Confidence")
                st.markdown(f"{result['confidence']}")
        else:
            st.error("Something went wrong with the API")
            st.write("Status Code:", response.status_code)
            st.write("Response:", response.text)