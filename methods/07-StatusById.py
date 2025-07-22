import requests
import json

def status_by_id(ids):
    api_key = "e883424d-d70f-4e58-8ee3-4e21ea390ff1"

    data = {
        "ApiKey": api_key,
        "Ids": ids  # باید لیستی از ID ها باشه
    }

    url = "http://api.sms-webservice.com/api/V3/StatusById"

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
