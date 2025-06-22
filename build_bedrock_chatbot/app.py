import streamlit as st
import boto3


# Page configuration
st.set_page_config(
    page_title="Bedrock Chatbot",
    page_icon=":robot_face:",
    layout="wide",
    initial_sidebar_state="expanded",
    )

st.title("🚀 ChatLab")
st.subheader("Build your own Bedrock Chatbot")

with st.sidebar:
    st.html("Configuration ")
    st.html("<hr style='border: 2px solid #c033ff;'>")
    