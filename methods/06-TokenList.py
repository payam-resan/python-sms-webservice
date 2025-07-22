import requests
import json

def token_list():
    api_key = "e883424d-d70f-4e58-8ee3-4e21ea390ff1"

    data = {
        "ApiKey": api_key
    }

    url = "http://api.sms-webservice.com/api/V3/TokenList"

    try:
        response = requests.post(
            url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data),
            timeout=10
        )
        return response.text
    except requests.RequestException as e:
        return f"Error: {e}"
