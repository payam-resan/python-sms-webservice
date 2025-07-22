import requests
import urllib.parse

def send_token_single(template_key, destination, param1, param2, param3):
    api_key = "e883424d-d70f-4e58-8ee3-4e21ea390ff1"

    params = {
        "ApiKey": api_key,
        "TemplateKey": template_key,
        "Destination": destination,
        "p1": param1,
        "p2": param2,
        "p3": param3
    }

    url = "http://api.sms-webservice.com/api/V3/SendTokenSingle?" + urllib.parse.urlencode(params)

    try:
        response = requests.get(url, timeout=10)
        return response.text
    except requests.RequestException as e:
        return f"Error: {e}"
