import json
import requests
from datetime import datetime, timedelta

def extract_csv_from_zip(zip_file:str) -> str:
    ...


def get_value_from_csv(csv_file:str) -> int:
    ...

def get_calculate_expression(expression:str) -> int:
    ...


def get_colab_code():
    ...


def get_hidden_text_code():
    ...


def calculate_days(day:str, start_date:str, end_date:str) -> int:
    
    """
    Example parameters
    sd = "2022-03-20"
    ed = "2022-08-10"
    day = "Wednesday"
    """
    # Define the date
    sd = list(map(int, start_date.split("-")))
    date = datetime(sd[0], sd[1], sd[2])
    target = 0 #count of that perticular day for which we're searching for

    while (str(date.date()) != end_date):

        # Get the day name
        if date.strftime("%A") == day.capitalize():
            target += 1
        
        # Increment the date by 1 day
        date = date + timedelta(days=1)
        
    ed = list(map(int, end_date.split("-")))
    date1 = datetime(ed[0], ed[1], ed[2])

    if date1.strftime("%A") == day.capitalize():
         target += 1

    return target


def get_sorted_json():
    # Function to read JSON data from a file
    def read_json(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data

    # Path to your JSON file
    file_path = 'data.json'
    
    # Read JSON data
    data = read_json(file_path)

    final = sorted(data, key=lambda x: (x['age'], x['name']))

    return json.dumps(final, separators=(',', ':'))


def get_css_selector_code():

    # Below is Javascript code for dataset value find question.
    # If possible use this also..
    # Or you can give show this javascript snippet and say user to copy and paste it in his console in which he is giving TDS GA0, executing this code answer will be printed on console.
    return """
    let foo_elements = Array.from(document.getElementsByClassName('div.foo'));
    let total = 0;

    for (let i of foo_elements) {
        for (let j of Array.from(i.children)) {
            total += Number.parseInt(j.dataset.value);
        }
    }
    """


def get_content_length_from_post_request(email:str, salt:str) -> str:
    
    # URL to which the POST request will be sent
    url = 'https://httpbin.org/response-headers'

    # Parameters to be sent in the GET request
    params = {
        'email': email,
        'salt': salt
    }

    # Sending the GET request
    response = requests.get(url, params=params)

    # Checking the response status code
    if response.status_code == 200:
        maal = response.json()
        return maal['Content-Length']
    else:
        return "Some error eccored"
