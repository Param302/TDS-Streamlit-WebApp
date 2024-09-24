import streamlit as st

st.title("TDS Web App")
st.subheader("Made by Parampreet Singh and Anant Luthra")
st.markdown(
    "_This is an unofficial web app for the **TDS Graded Assignment 0**_.")

st.markdown('---\n#### Q1: What is the value in the "_answer_" column of `q1.csv`?')
with st.expander("Instructions"):
    st.markdown("""1. Download the ZIP file from the link provided in [portal](https://tools-in-data-science.pages.dev/ga0).
2. Upload the ZIP file below.""")

uploader, ans1 = st.columns([2, 1], gap="medium", vertical_alignment="center")
uploaded_file = uploader.file_uploader(
    "Upload ZIP file", type=["zip"], label_visibility="hidden")

if uploaded_file is not None:
    ans1.markdown("##### Answer: `Hello`")


st.markdown("---\n#### Q2: Paste the formula to calculate answer in Google Sheets.")
with st.expander("Instructions"):
    st.markdown("""**Original question**:
> Use Google Sheets
>
> Let's make sure you can write formulas in Google Sheets. Type this formula into Google Sheets. (It won't work in Excel)
""")
q2_input, ans2 = st.columns([2, 1], gap="medium", vertical_alignment="center")
q2_input.text_input("Paste the Formula below", placeholder="=SUM(ARRAY_CONSTRAIN(SEQUENCE(1, 2, 3, 4), 1, 2))", label_visibility="hidden")
ans2.markdown("##### Answer: `Hello`")


st.markdown("---\n#### Q3: DIY :)")


st.markdown("---\n#### Q4: DIY :)")


st.markdown("---\n#### Q5: Paste the following code in console panel of _Developer Tools_ in your browser.")
with st.expander("Instructions"):
    st.markdown("""1. Open the Developer Tools in your browser.
2. Go to the Console panel.
3. Paste the code below in the Console panel.
4. Press Enter to execute the code.
5. Copy paste the result into the portal.)
> **Note:** If you see a "_Don’t paste code into the DevTools Console..._" message, type `allow pasting` and hit Enter.

**Original question**:
> Use DevTools
> 
> Let's make sure you know how to use the browser's developer tools. Just above this paragraph and after the heading "5. Use DevTools", there's a hidden element with secret text.
> 
> What is the hidden text?
""")


st.markdown("---\n#### Q6: Prompt start date, end date, and day name to calculate the number of days.")
with st.expander("Instructions"):
    st.markdown("""**Original question**:
> Write Python code
> 
> Let's make sure you know basic Python. Write a program to count the number of Wednesdays between 2015-04-29 and 2017-03-10, including both days.
> 
> How many Wednesdays are there in this data range (including both days)?
""")
q6_day_box, q6_start_date_box, q6_end_date_box = st.columns([1, 1, 1])
q6_day = q6_day_box.selectbox("Select Day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], index=2)
q6_start_date = q6_start_date_box.date_input("Start Date")
q6_end_date = q6_end_date_box.date_input("End Date")
ans6 = st.empty()
if q6_day and q6_start_date and q6_end_date:
    ans6.markdown(f"##### Answer: `Hello` - {q6_start_date}")


st.markdown("---\n#### Q7: Paste the `JSON` data provided in the question below.")
with st.expander("Instructions"):
    st.markdown("""**Original question**:           
""")
json_input = st.text_area("Paste JSON data here", label_visibility="hidden")
if json_input:
    with st.container():
        st.markdown("##### Sorted JSON:")
        st.code("Hello")


