import requests
import streamlit as st

if prompt := st.chat_input("Enter your prompt here..."):
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Please wait..."):
            response = requests.post(
                "http://localhost:5678/webhook/generate",
                json={"prompt": prompt}
            )

            result = response.json().get("response")


    st.markdown(result)