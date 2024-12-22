import streamlit as st
from hello_world import genAI
st.title("My GPY")

class Message:
    def __init__(self, role, content):
        self.role = role
        self.content = content
        pass
    def to_dict(self):
        role = 'user'
        if self.role == 'ai':
            role = 'model'
        return {"role": role, "parts": [self.content]}


if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'history' not in st.session_state:
    st.session_state.history = []

messages = st.session_state.messages
history = st.session_state.history


if len(messages) > 0:
    for message in messages:
        with st.chat_message(message.role):
            st.write(message.content)

prompt = st.chat_input("Nhập tin nhắn của bạn")
if prompt:
    new_message = Message("human", prompt)
    messages.append(new_message)

    with st.chat_message(new_message.role):
        st.write(new_message.content)
    
    history.append(new_message.to_dict())

    response = genAI(prompt, history)
    new_message = Message("ai", response)
    messages.append(new_message)
    
    with st.chat_message(new_message.role):
        st.write(new_message.content)
    
    history.append(new_message.to_dict())

print(history)
    