import streamlit as st
import random

# -------------------------
# Access control (Top of file)
# -------------------------
password = st.text_input("Enter Access Code:", type="password")

if password != "Avasmamta":
    st.warning("🔒 Please enter the correct access code to continue.")
    st.stop()  # stops execution if password is wrong

# -------------------------
# Quiz code starts here
# -------------------------
st.title("📝 Math Quiz App")

questions = [
    {
        "question": "What is 5 + 3?",
        "options": ["A. 6", "B. 7", "C. 8", "D. 9"],
        "answer": "C"
    },
    {
        "question": "What is 9 - 4?",
        "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
        "answer": "C"
    }
]

score = 0

for q in questions:
    st.subheader(q["question"])
    choice = st.radio("Choose an answer:", q["options"], key=q["question"])
    if st.button("Submit", key="submit"+q["question"]):
        if choice.startswith(q["answer"]):
            st.success("✅ Correct!")
            score += 1
        else:
            st.error("❌ Wrong! Correct answer is " + q["answer"])

st.write(f"Your final score: {score}/{len(questions)}")
