import requests

user_message = "Describe humanity's future after 300-400 in 3-4 lines"

request_message = {"message": user_message}

url = "https://votive-overably-novella.ngrok-free.dev/webhook-test/ca9a65b6-7975-4c23-ba8d-2b5b6e3d417f"


response = requests.post(url, json=request_message)


print(response.status_code)
try:
    print(response.json())
except Exception:
    print("Invalid JSON response:", response.text)
