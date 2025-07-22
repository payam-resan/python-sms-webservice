import requests
import json

def send_bulk(destination, user_trace_id, text):
    api_key = "e883424d-d70f-4e58-8ee3-4e21ea390ff1"
    sender = 30007546464646

    recipients = [{
        "Destination": destination,
        "UserTraceId": user_trace_id
    }]

    data = {
        "ApiKey": api_key,
        "Text": text,
        "Sender": sender,
        "Recipients": recipients
    }

    url = "http://api.sms-webservice.com/api/V3/SendBulk"

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
