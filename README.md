# 📌 Text Classification 

## 🚀 Live Demo

👉 Try the https://text-classification-production-41b5.up.railway.app/docs

<img width="1907" height="968" alt="image" src="https://github.com/user-attachments/assets/44c09677-5c5f-4fff-8da1-7523b45d326b" />
---
## Streamlit Demo
👉 Try the http://localhost:8501/

<img width="1913" height="942" alt="image" src="https://github.com/user-attachments/assets/9ba4d6a0-bcb9-44ec-ba9c-7f15caea2c76" />


## 🧠 Overview

This project is a **Machine Learning-based Text Classification system** that classifies input text into predefined categories:

- Politics 🏛️  
- Sports ⚽  
- Technology 💻  
- Entertainment 🎬  
- Business 💼  

The model is trained using **TF-IDF vectorization** and **Logistic Regression**, and deployed using **FastAPI** as a RESTful API.

---

## 🧠 Project Pipeline

1. Data Collection (Kaggle Dataset)
2. Data Preprocessing (Cleaning, Tokenization)
3. Feature Extraction (TF-IDF)
4. Model Training (Logistic Regression)
5. Model Saving (Pickle files)
6. API Development (FastAPI)
7. Deployment (Railway)
8. Frontend Integration (Streamlit)

---

## 🏗️ Project Structure

```text
Text-Classification/
│
├── app/
│   ├── main.py
│   ├── routes/
│   │     └── predict.py
│   ├── models/
│   │     └── schema.py
│   ├── services/
│   └── utils/
│
├── model/
│   ├── logistic_regression_model.pkl
│   ├── tfidf_vectorizer.pkl
│
├── requirements.txt
├── Text_Classification.ipynb
├── README.md
````

---

## ⚙️ Technologies Used

* Python 🐍
* Scikit-learn 🤖
* Pandas 📊
* NumPy 🔢
* NLTK 📝
* FastAPI ⚡
* Uvicorn 🚀
* Joblib 📦
* Streamlit 🎨

---

## 🚀 How to Run Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/faridahelmy26/Text-Classification.git
cd Text-Classification
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv env
env\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run API

```bash
uvicorn app.main:app --reload
```

---

## 📡 API Usage

### 🔹 Endpoint

```
POST /predict
```

### 🔹 Request Body

```json
{
  "text": "The football team won the championship"
}
```

### 🔹 Response

```json
{
  "prediction": "Sports",
  "confidence": 0.85
}
```

---

## 📊 Model Performance

* Algorithm: Logistic Regression
* Feature Extraction: TF-IDF
* Output Classes: 5 categories
* Evaluation: Accuracy-based classification

---
## confusion matrix
<img width="658" height="267" alt="WhatsApp Image 2026-05-03 at 8 15 58 PM" src="https://github.com/user-attachments/assets/ae9af70c-767a-4247-b344-531bd5d5a524" />
---

## 📁 Dataset

Dataset used from Kaggle:

👉 [https://www.kaggle.com/datasets/tanishqdublish/text-classification-documentation](https://www.kaggle.com/datasets/tanishqdublish/text-classification-documentation)

⚠️ Not included in repository due to size.

---

## 🔥 Features

✔ Real-time text prediction
✔ REST API using FastAPI
✔ Machine Learning pipeline
✔ Streamlit UI integration
✔ Cloud deployment (Railway)
✔ Lightweight & fast inference
---
## 👩‍💻 Author

**Farida Helmy**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!

```
