import streamlit as st
import joblib
import string
import re
import time 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

#load model and vectorizer
model=joblib.load('spam_model.pkl')
tfidf=joblib.load('tfidf_vectorizer.pkl')

#text preprocessing
def clean_text(text):
    text=text.lower()
    text=re.sub(r'https?://\s+|www\.\s+','',text) 
    text=re.sub(r'\d+','',text) 
    text=''.join([c for c in text if c not in string.punctuation])
    return text

#--------streamlit UI----
st.title("📩 SMS Spam Classifier")
st.write("Enter a message to check if it's spam or not.")

message = st.text_area("Please Enter Your Message:")
if st.button("Predict"):
    if message.strip() == "":
        st.warning("Please enter a message!")
    else:
        with st.spinner("🔄 Analyzing message..."):
            time.sleep(1.5)
            cleaned = clean_text(message)
            vector = tfidf.transform([cleaned])
            prediction = model.predict(vector)[0]

        if prediction == 1:
            st.error("🚨 **SPAM MESSAGE!**")
        else:
            st.success("✅ This message is **NOT SPAM**.")
            
    