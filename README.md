تمام 👍 ده **README كامل واحترافي** تقدري تحطيه مباشرة في مشروعك على GitHub:

---

# 📌 Text Classification API

## 🚀 Overview

This project is a **Machine Learning-based Text Classification system** that classifies input text into predefined categories:

* Politics 🏛️
* Sports ⚽
* Technology 💻
* Entertainment 🎬
* Business 💼

The model is trained using **TF-IDF vectorization** and **Logistic Regression**, and deployed using **FastAPI** as a RESTful API.

---

# 🧠 Project Pipeline

1. Data Collection (Kaggle Dataset)
2. Data Preprocessing (Cleaning, Tokenization)
3. Feature Extraction (TF-IDF)
4. Model Training (Logistic Regression)
5. Model Saving (Pickle files)
6. API Development (FastAPI)
7. Prediction via REST API

---

# 🏗️ Project Structure

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
```

---

# ⚙️ Technologies Used

* Python 🐍
* Scikit-learn 🤖
* Pandas 📊
* NumPy 🔢
* NLTK 📝
* FastAPI ⚡
* Uvicorn 🚀
* Joblib 📦

---

# 🚀 How to Run the Project Locally

## 1️⃣ Clone the repository

```bash
git clone https://github.com/faridahelmy26/Text-Classification.git
cd Text-Classification
```

---

## 2️⃣ Create virtual environment

```bash
python -m venv env
```

Activate it:

```bash
env\Scripts\activate
```

---

## 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run the API

```bash
uvicorn app.main:app --reload
```

---

## 5️⃣ Open API docs

```
http://127.0.0.1:8000/docs
```

---

# 📡 API Usage

## 🔹 Endpoint

```
POST /predict
```

## 🔹 Request Body

```json
{
  "text": "The football team won the championship"
}
```

## 🔹 Response

```json
{
  "input_text": "The football team won the championship",
  "prediction": "Sports",
  "confidence": 0.85
}
```

---

# 📊 Model Performance

* Algorithm: Logistic Regression
* Feature Extraction: TF-IDF
* Output Classes: 5 categories
* Evaluation: Accuracy-based classification

---

# 📁 Dataset

Dataset used from Kaggle (Text Classification Dataset).

👉 Not included in repository due to size.
You can download it from Kaggle and place it in a local `https://www.kaggle.com/datasets/tanishqdublish/text-classification-documentation?resource=download` folder.

---

# 🔥 Features

✔ Real-time text prediction
✔ REST API using FastAPI
✔ Machine Learning pipeline
✔ Easy to extend with new classes
✔ Lightweight and fast inference

---

# 👩‍💻 Author

**Farida Helmy**

---

# ⭐ If you like this project

Give it a ⭐ on GitHub!

