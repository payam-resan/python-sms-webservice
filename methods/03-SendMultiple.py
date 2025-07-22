import requests
import json

def send_multiple(destination, user_trace_id, text):
    api_key = "e883424d-d70f-4e58-8ee3-4e21ea390ff1"
    sender = 30007546464646

    recipient = {
        "Sender": sender,
        "Text": text,
        "Destination": destination,
        "UserTraceId": user_trace_id
    }

    data = {
        "ApiKey": api_key,
        "Recipients": [recipient]
    }

    url = "http://api.sms-webservice.com/api/V3/SendMultiple"

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
