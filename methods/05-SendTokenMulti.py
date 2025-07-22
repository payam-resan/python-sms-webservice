import requests
import json

def send_token_multi(template_key, destination, user_trace_id, parameters):
    api_key = "e883424d-d70f-4e58-8ee3-4e21ea390ff1"

    recipient = {
        "Destination": destination,
        "UserTraceId": user_trace_id,
        "Parameters": parameters  # باید لیستی از پارامترها باشه
    }

    data = {
        "ApiKey": api_key,
        "TemplateKey": template_key,
        "Recipients": [recipient]
    }

    url = "http://api.sms-webservice.com/api/V3/SendTokenMulti"

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
