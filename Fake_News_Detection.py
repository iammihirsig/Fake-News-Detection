import streamlit as st
import subprocess
import sys

try:
    import joblib
except ModuleNotFoundError:
    subprocess.run([sys.executable, "-m", "pip", "install", "joblib"])
    import joblib

# Load the model and vectorizer
vectorizer = joblib.load("vectorizer.jb")
model = joblib.load("lr_model.jb")

# Title
st.markdown(
    "<h1 style='text-align: center; color: #2C3E50;'>📰 Fake News Detector 📰</h1>",
    unsafe_allow_html=True,
)

# Label for text input
st.markdown(
    """
    <h5 style='text-align: center; font-weight: bold; margin-bottom: -10px;'>
        Enter News Article Below
    </h5>
    """,
    unsafe_allow_html=True,
)

# News input box with placeholder
news_input = st.text_area("", "", placeholder="Type or paste a news article here...")

# Centering the button using Streamlit columns
col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    check_news = st.button("Check News")  # Button placed in center column

# Prediction Logic
if check_news:
    if news_input.strip():
        transform_input = vectorizer.transform([news_input])
        prediction = model.predict(transform_input)

        if prediction[0] == 1:
            st.success("✅ The News Is Real!")
        else:
            st.error("🚨 The News Is Fake!")
    else:
        st.warning("⚠️ Please Enter Some Text To Analyze!")


# Footer with GitHub link and model details
st.markdown(
    """
    <hr>
    <p style='text-align: center; font-size: 14px;'>
        Made with 💙 by
        <a href='https://github.com/iammihirsig' target='_blank' style='color: #2980B9; font-weight: bold; text-decoration: none;'>
            Mihir Raj Singh | @iammihirsig
        </a> | Trained on <b>Logistic Regression</b>
    </p>
    <br>
    """,
    unsafe_allow_html=True,
)


# Centered Accuracy Card
st.markdown(
    """
    <style>
        .info-card {
            background-color: #f8f9fa;
            padding: 2px;
            border-radius: 15px;
            text-align: center;
            width: 90%;
            margin: auto;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
            font-size: 15px;
            font-weight: bold;
            line-height: 1.6;
        }
    </style>
    <div class='info-card'>
        🧠 <b>Model Performance</b> 🧠 <br>
        Accuracy: <span style='color: green;'>99%</span> |
        Precision: <span style='color: blue;'>98.5%</span> |
        Recall: <span style='color: orange;'>98.5%</span> |
        F1 Score: <span style='color: purple;'>99%</span> <br><br>

        Dataset: Fake News Dataset (Kaggle)
        Features: TF-IDF Vectorization, Stopword Removal, Stemming
        Training Samples: 35,920
        Model: Logistic Regression | Training Time: ~30s
    </div>
    """,
    unsafe_allow_html=True,
)
