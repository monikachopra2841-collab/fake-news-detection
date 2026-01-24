import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

texts = [
    "Government announces new education policy",
    "Free money for everyone on WhatsApp",
    "Official notice about school exams",
    "Drinking salt water cures COVID",
    "New scheme launched by government",
    "Fake message about free recharge"
]

labels = [1, 0, 1, 0, 1, 0]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

st.title("Fake News Detection AI Project")

news_input = st.text_area("Enter news text:")

if st.button("Check News"):
    news_vec = vectorizer.transform([news_input])
    prediction = model.predict(news_vec)

    if prediction[0] == 1:
        st.success("This news is REAL")
    else:
        st.error("This news is FAKE")
