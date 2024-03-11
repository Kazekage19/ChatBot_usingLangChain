import streamlit as st 
from openai import OpenAI
import chatLLM

st.title('A Huehue ChatBot')
st.caption("Yes, I answer questions based on your data, and ofc in general")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role" : "chatbot", "content": "Hi Bamby"}]

for texts in st.session_state.messages:
    st.chat_message(texts['role']).write(texts['content'])
    
if query := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").write(query)
    response = chatLLM.chat(query)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)


    