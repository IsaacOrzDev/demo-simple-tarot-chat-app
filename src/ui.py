import streamlit as st
from chat import chat

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    # print('st.session_state.messages', st.session_state.messages)
    response = chat(prompt)
    st.session_state.messages.append(
        {"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
