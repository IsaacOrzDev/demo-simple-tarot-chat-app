import streamlit as st
from chat import chat

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "AI", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "Human", "content": prompt})
    st.chat_message("user").write(prompt)
    # print('st.session_state.messages', st.session_state.messages)
    response = chat(prompt,  st.session_state.messages)
    st.session_state.messages.append(
        {"role": "AI", "content": response})
    st.chat_message("AI").write(response)
