import google.generativeai as genai
import streamlit as st

st.set_page_config(
    page_title="NovaGemini",
    page_icon="Geminilogo.png",
)
gemini_api_key = "AIzaSyCZGw2_4PXUpxsau2g39XkgWXLdFLeskIE"
genai.configure(api_key=gemini_api_key)

st.title("💬🤖 NovaGemini WebChat")
st.caption(" A Google Gemini Streamlit Powered By AbdulRahman Khairi📟💻")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    try:
        model = genai.GenerativeModel("gemini-pro")
        chat = model.start_chat(history=[])
        response = chat.send_message(prompt)
        text = response.text
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.messages.append({"role": "assistant", "content": text})
        st.chat_message("assistant").write(text)
    except Exception as e:
        st.error(f"Error occurred: {e}")