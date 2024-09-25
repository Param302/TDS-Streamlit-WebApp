import streamlit as st
from utils import (date, json, extract_value_from_zip, calculate_gsheets_formula, calculate_ms_excel_formula, calculate_days, get_sorted_json, get_content_length_from_post_request, get_colab_code, get_hidden_text_code, get_css_selector_code, store_feedback)


st.set_page_config(
    page_title="TDS GA 0 Helper App",
    page_icon="🛠️"
)


st.title("TDS GA 0 Helper App")
st.markdown(
    "_This is an unofficial helper app for the **TDS Graded Assignment 0**_.")


def show_answer_1():
    heading1.markdown("##### Answer:")
    value = str(extract_value_from_zip(uploaded_file))
    ans1_box.code(value)


def show_answer_2():
    cloud_creds = json.loads(st.secrets["google_cloud"]["sheets_api_creds"])
    value = calculate_gsheets_formula(cloud_creds, q2_input)
    heading2.markdown("##### Answer:")
    ans2_box.code(value)


def show_answer_3():
    heading3.markdown("##### Answer:")
    ans3_box.code(str(calculate_ms_excel_formula(q3_input)))


def show_answer_4():
    ans4.code(get_colab_code(), line_numbers=True)


def show_answer_5():
    ans5.code(get_hidden_text_code(), language="javascript")


def collect_rating():
    cloud_creds = json.loads(st.secrets["google_cloud"]["sheets_api_creds"])

    if (f1:=st.session_state.get("feedbackarea1_ans", None)):
        store_feedback(cloud_creds, f1)
    
    if (f2:=st.session_state.get("feedbackarea2_ans", None)):
        store_feedback(cloud_creds, f2)


def show_answer_6():
    heading6.markdown("##### Answer:")
    ans6_box.code(str(calculate_days(q6_day, q6_start_date, q6_end_date)))


def show_answer_7():
    ans7.markdown("##### Sorted JSON:")
    ans7.code(get_sorted_json(json_input), language="json", wrap_lines=True)


def show_answer_8():
    ans8.code(get_css_selector_code(),
              language="javascript", line_numbers=True)


def show_answer_9():
    content_length = get_content_length_from_post_request(q9_email, q9_salt)
    heading9.markdown("##### Answer (`Content-Length`):")
    ans9_box.code(content_length)


st.markdown(
    '---\n#### Q1: Upload the ZIP file to get the answer.')
with st.expander("Instructions"):
    st.markdown("""**Original Question**:
> What is the value in the "_answer_" column of `q1.csv`?
1. Download the ZIP file from the link provided in portal.
2. Upload the ZIP file below.""")

uploaded_file = st.file_uploader(
    "Upload ZIP file", type=["zip"], label_visibility="hidden")
ans1 = st.empty()
heading1, ans1_box = ans1.columns([0.15, 0.8], vertical_alignment="center")
if uploaded_file is not None:
    show_answer_1()

st.markdown(
    "---\n#### Q2: Paste the _Google Sheet_ formula to calculate the answer.")
with st.expander("Instructions"):
    st.markdown("""**Original question**:
> Use Google Sheets
>
> Let's make sure you can write formulas in Google Sheets. Type this formula into Google Sheets. (It won't work in Excel)
""")
q2_input = st.text_input("Paste the Formula below",
                         placeholder="=SUM(ARRAY_CONSTRAIN(SEQUENCE(1, 2, 3, 4), 1, 2))", label_visibility="hidden")
ans2 = st.empty()
heading2, ans2_box = ans2.columns([0.15, 0.8], vertical_alignment="center")

if q2_input:
    show_answer_2()


st.markdown(
    "---\n#### Q3: Paste the _Microsoft 365 Excel_ formula to calculate the answer.")
with st.expander("Instructions"):
    st.markdown("""**Original question**:
> Use Excel
> 
> Let's make sure you can write formulas in Excel. Type this formula into Excel. (It won't work in Google Sheets)
""")
q3_input = st.text_input("Paste the Formula below",
                         placeholder="=SUM(TAKE(SORTBY({1,2,...,10}, {1,2,...,10}), 1, 2))", label_visibility="hidden", key="q3_input")
ans3 = st.empty()
heading3, ans3_box = ans3.columns([0.15, 0.8], vertical_alignment="center")
if q3_input:
    show_answer_3()


st.markdown(
    "---\n#### Q4: Paste the below code in Google Colab to get the answer.")
with st.expander("Instructions"):
    st.markdown("""1. Open [Google Colab](https://colab.research.google.com/) in student mail ID.
2. Create a new notebook.
2. Paste the provided code in 1st cell.
3. Run the cell (Shift + Enter).
4. Allow all the required access during code execution.
5. Copy the output and paste it in the portal.
""")
ans4 = st.empty()
show_answer_4()


st.markdown(
    "---\n#### Q5: Paste the code below into your browser's _Developer Tools_ console to reveal the hidden text.")
with st.expander("Instructions"):
    st.markdown("""**Original question**:
> Use DevTools
> 
> Let's make sure you know how to use the browser's developer tools. Just above this paragraph and after the heading "5. Use DevTools", there's a hidden element with secret text.
> 
> What is the hidden text?

1. Open the Developer Tools in your browser.
2. Go to the Console panel.
3. Paste the code below in the Console panel.
4. Press Enter to execute the code.
5. Copy paste the result into the portal.)
> **Note:** If you see a "_Don’t paste code into the DevTools Console..._" message, type `allow pasting` and hit Enter.""")
ans5 = st.empty()
show_answer_5()

feedbackarea1 = st.container(border=True)
feedbackarea1.write("#### Enjoying our app? Please rate it.\n_Your feedback is valuable to us._\n")
feedbackarea1_ans = feedbackarea1.feedback("stars", on_change=collect_rating, key="feedbackarea1_ans")

st.markdown(
    "#### Q6: Enter the start date, end date, and day of the week to calculate the total number of days.")
with st.expander("Instructions"):
    st.markdown("""**Original question**:
> Write Python code
> 
> Let's make sure you know basic Python. Write a program to count the number of Wednesdays between 2015-04-29 and 2017-03-10, including both days.
> 
> How many Wednesdays are there in this data range (including both days)?
""")
q6_day_box, q6_start_date_box, q6_end_date_box = st.columns([1, 1, 1])
q6_day = q6_day_box.selectbox("Select Day", [
                              "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], index=2)
q6_start_date = q6_start_date_box.date_input("Start Date", min_value=date(2000, 1, 1), max_value=date(2030, 12, 31))
q6_end_date = q6_end_date_box.date_input("End Date", min_value=date(2000, 1, 1), max_value=date(2030, 12, 31))
ans6 = st.empty()
heading6, ans6_box = ans6.columns([0.15, 0.8], vertical_alignment="center")
if q6_day and q6_start_date and q6_end_date:
    show_answer_6()


st.markdown(
    "---\n#### Q7: Paste the provided `JSON` data below to get it sorted.")
with st.expander("Instructions"):
    st.markdown("""**Original question**:
> Sort this JSON array of objects by the value of the `age` field. In case of a tie, sort by the `name` field. Paste the resulting JSON below without any spaces or newlines.""")
json_input = st.text_area("Paste JSON data here", height=150, label_visibility="hidden")
ans7 = st.empty()
if json_input:
    show_answer_7()


st.markdown(
    "---\n#### Q8: Paste the code below into your browser's _Developer Tools_ console to sum the `data-value` attributes.")
with st.expander("Instructions"):
    st.markdown("""**Original question**:
> Use CSS selectors
> 
> Let's make sure you know how to select elements using CSS selectors. Take all direct children of `<div>`s having a `foo` class. What's the sum of their `data-value` attributes?

1. Open the Developer Tools in your browser.
2. Go to the Console panel.
3. Paste the code below in the Console panel.
4. Press Enter to execute the code.
5. Copy paste the result into the portal.)
> **Note:** If you see a "_Don’t paste code into the DevTools Console..._" message, type `allow pasting` and hit Enter.""")
ans8 = st.empty()
show_answer_8()


st.markdown("---\n#### Q9: Paste your student mail ID and salt value below.")
with st.expander("Instructions"):
    st.markdown("""**Original question**:
> Make HTTP requests
> 
> Let's make sure you know how to make HTTP requests. Send a HTTP POST request to https://httpbin.org/response-headers with the URL encoded parameter email set to `<roll_no>@.ds.study.iitm.ac.in` and the parameter salt set to `abcdefghijklmnopqrstuvwxyz0123456789`. What is the value of the `Content-Length` HTTP header in the response?""")

q9_email_box, q9_salt_box = st.columns([1, 1], vertical_alignment="center")
q9_email = q9_email_box.text_input(
    "Enter Email ID", placeholder="<roll_no>@.ds.study.iitm.ac.in")
q9_salt = q9_salt_box.text_input(
    "Enter Salt", placeholder="abcdefghijklmnopqrstuvwxyz0123456789")
ans9 = st.empty()
heading9, ans9_box = ans9.columns([0.3, 0.5], vertical_alignment="center")
if q9_email and q9_salt:
    show_answer_9()

st.markdown("---\n#### Q10: How much interesting do you find TDS subject?")
ans10 = st.slider("From 1 (_lowest_) to 5 (_highest_)", 1, 5, 3)
st.markdown("---")

if not feedbackarea1_ans and ans10:
    feedbackarea2 = st.container(border=True)
    feedbackarea2.write("#### Do you like this app? Please rate it.\n_Your feedback is valuable to us._\n")
    feedbackarea2_ans = feedbackarea2.feedback("stars", on_change=collect_rating, key="feedbackarea2_ans")


# Footer
st.markdown("""
> **Disclaimer**: This web app is an unofficial tool created for the TDS Graded Assignment 0. It is intended solely for educational purposes, and we strongly discourage any form of academic dishonesty or unethical behavior. Additionally, we respect user privacy and do not store or collect any personal data shared throughout the app, except feedback rating.

#### [GitHub Repository 🔗](https://github.com/Param302/TDS-Streamlit-WebApp)
### Developed with 🤍 by<img src="https://avatars.githubusercontent.com/u/76559816?v=4" width="40" style="border-radius:50%;padding-bottom:10px;">[Parampreet Singh](https://github.com/Param302) and <img src="https://avatars.githubusercontent.com/u/92159216?v=4" width="40" style="border-radius:50%;padding-bottom:5px;"> [Anant Luthra](https://github.com/AnantLuthra)
""", unsafe_allow_html=True)
