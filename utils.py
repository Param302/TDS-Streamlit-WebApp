import json
import requests
from datetime import datetime, timedelta


def extract_csv_from_zip(zip_file: str) -> str:
    ...


def get_value_from_csv(csv_file: str) -> int:
    ...


def calculate_gsheets_formula(expression: str) -> int:
    ...


def calculate_ms_excel_formula(formula: str) -> int:
    ...

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
