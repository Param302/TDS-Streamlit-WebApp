import json
import zipfile
import requests
import numpy as np
import pandas as pd
from datetime import datetime, timedelta


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


def calculate_gsheets_formula(expression: str) -> int:
    ...


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


def get_hidden_text_code():
    return """document.getElementById("q5-message").innerText;"""


def calculate_days(day: str, start_date: str, end_date: str) -> int:
    """
    Example parameters
    sd = "2022-03-20"
    ed = "2022-08-10"
    day = "Wednesday"
    """
    sd = list(map(int, start_date.split("-")))
    date = datetime(sd[0], sd[1], sd[2])
    target = 0  # count of that particular day for which we're searching for

    while (str(date.date()) != end_date):
        if date.strftime("%A") == day.capitalize():
            target += 1
        date = date + timedelta(days=1)

    ed = list(map(int, end_date.split("-")))
    date1 = datetime(ed[0], ed[1], ed[2])
    if date1.strftime("%A") == day.capitalize():
        target += 1

    return target


def get_sorted_json(json_data: str) -> str:
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


def get_content_length_from_post_request(email: str, salt: str) -> str:
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
        return "Some error eccored"
