import streamlit as st

st.title("🧠 Fake News Detection AI Project")

news = st.text_area("Enter a news message:")

fake_keywords = ["free money", "whatsapp", "guaranteed", "cure", "fake", "instant"]

if st.button("Check News"):

    found_keywords = []

    for word in fake_keywords:
        if word.lower() in news.lower():
            found_keywords.append(word)

    if len(found_keywords) == 0:
        real_percent = 90
        fake_percent = 10
        st.success("✅ This news is likely REAL")
    else:
        fake_percent = min(90, 50 + len(found_keywords) * 10)
        real_percent = 100 - fake_percent
        st.error("❌ This news is likely FAKE")

    st.write("### 🔢 Prediction Confidence")
    st.write(f"🟢 Real News: {real_percent}%")
    st.write(f"🔴 Fake News: {fake_percent}%")

    if found_keywords:
        st.write("### 🚩 Suspicious Keywords Found:")
        for k in found_keywords:
            st.write(f"- {k}")
    else:
        st.write("### ✅ No suspicious keywords found")
