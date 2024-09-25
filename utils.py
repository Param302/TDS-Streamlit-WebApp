import json
import re
import gspread
import zipfile
import requests
import numpy as np
import pandas as pd
from datetime import date, datetime, timedelta
from oauth2client.service_account import ServiceAccountCredentials

row = 1
col = "A"

def extract_value_from_zip(zip_file: str) -> str:
    with zipfile.ZipFile(zip_file) as z:
        file_list = z.namelist()

        csv_files = [file_name for file_name in file_list if file_name.endswith(".csv")]

        if not csv_files:
            return "No CSV file found in the ZIP."

        if len(csv_files) > 1:
            return "Multiple CSV files found. Please upload a ZIP with only one CSV file."

        with z.open(csv_files[0]) as f:
            df = pd.read_csv(f)
            if "answer" not in df.columns:
                return "The CSV file does not contain a column named 'answer'."

            return df.loc[0, "answer"]


def validate_expression(expression: str) -> bool:
    return expression.count("=") == 1 and expression.count("(") == expression.count(")")


def calculate_gsheets_formula(gcloud_creds, expression: str) -> int:
    global row, col

    expression = f"={expression}" if not expression.startswith("=") else expression
    expression = expression.strip()
    if not validate_expression(expression):
        return "Invalid formula"
    
    if row > 100:
        row = 1
        col = chr(ord(col) + 1)
    cell = f"{col}{row}"

    scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
    
    creds = ServiceAccountCredentials.from_json_keyfile_dict(gcloud_creds, scope)
    client = gspread.authorize(creds)
    sheet = client.open('TDS Streamlit Web App').sheet1
    sheet.update_acell(cell, expression)
    row += 1
    value = sheet.get_values(cell)[0][0]
    if value.isdigit():
        return int(value)
    return f"Some error occurred: {value}"


def calculate_ms_excel_formula(formula: str) -> int:
    ...



def sum_sorted_taken(array1, array2, y):
    # Convert lists to numpy arrays if they aren't already
    array1 = np.array(array1)
    array2 = np.array(array2)

    # Sort array1 by array2
    sorted_indices = np.argsort(array2)
    sorted_array1 = array1[sorted_indices]

    # Take the first y elements
    taken_elements = sorted_array1[:y]

    # Sum the taken elements
    total_sum = np.sum(taken_elements)

    return total_sum


def get_colab_code() -> str:
    return """import hashlib
import requests
from google.colab import auth
from oauth2client.client import GoogleCredentials

auth.authenticate_user()
creds = GoogleCredentials.get_application_default()
token = creds.get_access_token().access_token
response = requests.get(
    'https://www.googleapis.com/oauth2/v1/userinfo',
    params={'alt': 'json'},
    headers={'Authorization': f'Bearer {token}'}
)
email = response.json()['email']
hashlib.sha256(f'{email} {creds.token_expiry.year}'.encode()).hexdigest()[-5:]"""


def get_hidden_text_code() -> str:
    return """document.getElementById("q5-message").innerText;"""


def calculate_days(day: str, start_date: date, end_date: date) -> int:
    if start_date > end_date:
        return "Invalid date range"

    target = 0  # count of that particular day for which we're searching for

    while (start_date <= end_date):
        if start_date.strftime("%A") == day.capitalize():
            target += 1
        start_date = start_date + timedelta(days=1)

    return target


def get_sorted_json(json_data: str) -> str:
    json_data = json_data.strip()
    data = json.loads(json_data)

    sorted_data = sorted(data, key=lambda x: (x['age'], x['name']))
    return json.dumps(sorted_data, separators=(',', ':'))


def get_css_selector_code() -> str:
    return """(() => {
    let foo_elements = Array.from(document.getElementsByClassName('foo'));
    let total = 0;
    foo_elements.forEach(i => {
        Array.from(i.children).forEach(j => {
            total += Number.parseInt(j.dataset.value);
        });
    });
    return total;
})();"""


def valid_email(email: str) -> bool:
    pattern = re.compile(r'^(2[1-9])(f|ds|dp)[1-3]\d{6}@(ds|es)\.study\.iitm\.ac\.in$')
    return bool(pattern.match(email))


def get_content_length_from_post_request(email: str, salt: str) -> str:
    email = email.strip()
    if not valid_email(email):
        return "Invalid email, please enter valid Student email ID"

    url = 'https://httpbin.org/response-headers'
    params = {
        'email': email,
        'salt': salt
    }

    response = requests.post(url, params=params)
    if response.status_code == 200:
        json_response = response.json()
        return json_response['Content-Length']
    else:
        return f"Some error occurred: {response.status_code} - {response.text}"
