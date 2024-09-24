import streamlit as st

st.title("TDS Web App")
st.subheader("Made by Parampreet Singh and Anant Luthra")
st.markdown("_This is an unofficial web app for the **TDS Graded Assignment 0**_.")

st.markdown("""#### Q1: What is the value in the "**answer**" column of `q1.csv`?
""")

with st.expander("Instructions"):
    st.markdown("""1. Download the ZIP file from the link provided in [portal](https://tools-in-data-science.pages.dev/ga0).
2. Upload the ZIP file below.""")


uploaded_file = st.file_uploader("Upload ZIP file", type=["zip"])

if uploaded_file is not None:
    st.write(uploaded_file)
