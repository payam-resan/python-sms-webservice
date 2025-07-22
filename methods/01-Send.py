import requests
import urllib.parse

def send_sms(recipients, text):
    api_key = "e883424d-d70f-4e58-8ee3-4e21ea390ff1"
    sender = "30007546464646"

    params = {
        'ApiKey': api_key,
        'Text': urllib.parse.quote(text),
        'Sender': sender,
        'Recipients': recipients
    }

    url = f"http://api.sms-webservice.com/api/V3/Send?ApiKey={params['ApiKey']}&Text={params['Text']}&Sender={params['Sender']}&Recipients={params['Recipients']}"

    try:
        response = requests.get(url, timeout=10)
        return response.text
    except requests.RequestException as e:
        return f"Error: {e}"
