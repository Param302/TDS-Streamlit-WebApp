
<div align="center">

# [TDS GA 0 Helper App 🛠️](https://tds-webapp.streamlit.app)

This is an unofficial helper app for the **TDS Graded Assignment 0** in the IIT Madras BS Degree program. It is made to help students by sharing the approach and detailed steps to approach the questions in TDS Assignments.

[![Streamlit](https://img.shields.io/badge/Streamlit-%23FF4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/) 
[![Python](https://img.shields.io/badge/Python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Google Sheets](https://img.shields.io/badge/Google_Sheets-%234285F4.svg?style=for-the-badge&logo=google-sheets&logoColor=white)](https://www.google.com/sheets/about/)
[![Deployed on Streamlit](https://img.shields.io/badge/Streamlit-Deployed-brightgreen?style=for-the-badge)](https://tds-webapp.streamlit.app)

</div>

## Features
- Detailed step-by-step approach for **TDS GA 0**.
- Real-time calculations using **Google Sheets** integration.
- User-friendly interface developed with **Streamlit**.
- Lightweight and easy to use.

## Installation

### Clone the project
```bash
git clone https://github.com/Param302/TDS-Streamlit-WebApp.git
cd TDS-Streamlit-WebApp
```

### Dependencies
- Python >= `3.10.12`
- Create a virtual environment:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

- Install required modules:
    ```bash
    pip install -r requirements.txt
    ```

### Configuration
You'll need to set up **Google Cloud** for Google Sheets API integration and configure your app's secrets.

1. **Create the `.streamlit` folder**:
    ```bash
    mkdir .streamlit
    cd .streamlit
    ```
2. **Create the `secrets.toml` inside `.secrets` folder**:
    ```bash
    touch secrets.toml
    ```
3. **Create an app in Google Cloud console, enable `Google Sheets` and `Google Drive` APIs, download credentials and add json credentials in `secrets.toml` file.**
    ```bash
    [google_cloud]
    sheets_api_creds="""<your_json_creds>"""
    ```

## Running the App

After installing dependencies and configuring your secrets, run the app with the following command:

```bash
streamlit run app.py
```

## Contact Information
### Developed with 🤍 by [Parampreet Singh](https://github.com/Param302) and [Anant Luthra](https://github.com/AnantLuthra)

For enquiries, kindly reach out to [Parampreet Singh](https://param302.bio.link)