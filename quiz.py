import random
import streamlit as st

st.title("🧮 Math Quiz Game")

# Initialize session state
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.q_no = 0

def generate_question():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    operator = random.choice(["+", "-", "*"])
    if operator == "+":
        answer = a + b
    elif operator == "-":
        answer = a - b
    else:
        answer = a * b
    question = f"{a} {operator} {b} = ?"
    options = [answer,
               answer + random.randint(1, 5),
               answer - random.randint(1, 5),
               answer + random.randint(6, 10)]
    random.shuffle(options)
    return question, options, answer

# Button to generate new question
if st.button("New Question") or st.session_state.q_no == 0:
    q, opts, ans = generate_question()
    st.session_state.q = q
    st.session_state.opts = opts
    st.session_state.ans = ans
    st.session_state.q_no += 1

# Show question
if "q" in st.session_state:
    st.write(f"**Q{st.session_state.q_no}: {st.session_state.q}**")
    choice = st.radio("Choose your answer:", st.session_state.opts)
    if st.button("Submit Answer"):
        if choice == st.session_state.ans:
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Wrong! Correct Answer: {st.session_state.ans}")
        st.write(f"**Score: {st.session_state.score}**")
