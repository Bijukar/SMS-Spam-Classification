
# 📩 SMS Spam Classification 
### 🚀 End-to-End Machine Learning Project + Streamlit Web App

An interactive machine learning project that predicts whether an SMS message is **Spam** or **Ham**, powered by **Python, Scikit-learn, TF-IDF**, and deployed using **Streamlit**.

---

## 🌟 Features  
- 🔹 Full end-to-end ML pipeline  
- 🔹 Clean text preprocessing  
- 🔹 TF-IDF feature engineering  
- 🔹 High-accuracy ML model  
- 🔹 Real-time prediction using Streamlit  
- 🔹 Modern UI with spinner/loading animation  
- 🔹 Lightweight & fast  

---

## 🏗️ Tech Stack  

| Category | Tools |
|---------|--------|
| **Language** | Python |
| **ML** | Scikit-learn, TF-IDF |
| **Deployment** | Streamlit |
| **Model Saving** | Joblib |
| **Data Handling** | Pandas, NumPy |

---

## 🧠 Project Workflow  

### **1️⃣ Data Loading & Understanding**
- Loaded `spam.csv`
- Inspected null values, duplicates, label distribution

### **2️⃣ Data Cleaning**
- Removed unnecessary columns
- Removed duplicates 
- Mapped labels (`ham → 0`, `spam → 1`)  
- Basic text cleanup  

### **3️⃣ EDA (Exploratory Data Analysis)**
- Spam vs ham distribution  
- Message length distribution analysis  
- WordCloud Generation  

### **4️⃣ Data Preprocessing**
Steps include:
- Lowercasing  
- Removing punctuation
- Removing URL
- Removing numbers  
- Removing stopwords  
  
#### **5️⃣ Feature Engineering**
- Converted text to numerical vectors using **TF-IDF Vectorizer**

#### **6️⃣ Train/Test Split**
- Split dataset: **80% train / 20% test**

### **7️⃣ Model Training**

- **Multinomial Naive Bayes** (fast + great for text)

### **8️⃣ Model Evaluation**
- Accuracy,Precision, F1-Score  
- Confusion matrix
- ROC-AUC Curve
   
### **9️⃣ Model Saving**
Saved using Joblib:
- `spam_model.joblib`  
- `tfidf_vectorizer.joblib`  

### **🔟 Streamlit App Deployment**
- Beautiful UI  
- Text input box  
- Predict button  
- Spinner animation  
- Spam/Ham output with colors  

---

## 📂 Folder Structure

sms_spam_classifier/ │ ├── app/ │   └── app.py │ ├── data/ │   └── spam.csv │ ├── models/ │   ├── spam_model.joblib │   └── tfidf_vectorizer.joblib │ ├── notebooks/ │   └── model_training.ipynb │ ├── requirements.txt └── README.md

---

## ▶️ How to Run the Project  

### **1️⃣ Install Requirements**

pip install -r requirements.txt

### **2️⃣ Run App**

streamlit run app.py

### **3️⃣ Predict**
- Type an SMS  
- Click **“Predict”**  
- See instant prediction ⚡  

---

## 🖥️ Streamlit App Preview

📩 SMS Spam Classifier

Enter your message: 👉 "Congratulations! You've won a cash prize!"

⏳ Analyzing...

🚨 SPAM DETECTED!

---

## 🚀 Future Enhancements  
- Add LSTM/Transformer-based model  
- Add interactive charts in app  
- Add theme switching (dark/light mode)  
- Deploy on Render / Streamlit Cloud  
- Add API endpoint using FastAPI  

---
