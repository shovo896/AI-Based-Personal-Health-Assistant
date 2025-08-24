import streamlit as st
from assistant import get_response  # Make sure assistant.py is in the same folder

st.set_page_config(page_title="AI-Based Personal Health Assistant", layout="centered")
st.title(" AI-Based Personal Health Assistant")
st.write("Type your health or emotion query below and get instant responses.")

# Input from user
user_input = st.text_input("Enter your query:")

# Initialize chat history
if 'history' not in st.session_state:
    st.session_state.history = []

# Only call get_response when user types something
if user_input:
    response = get_response(user_input)
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Assistant", response))

# Display chat history
for speaker, text in st.session_state.history:
    if speaker == "You":
        st.markdown(f"You: {text}")
    else:
        st.markdown(f"Assistant: {text}")

