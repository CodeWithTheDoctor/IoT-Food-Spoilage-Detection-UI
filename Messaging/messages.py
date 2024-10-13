import json
import requests
from google.oauth2 import service_account
from google.auth.transport.requests import Request

# Path to your service account key file
SERVICE_ACCOUNT_FILE = '../serviceAccountKey.json'

# FCM endpoint
FCM_ENDPOINT = 'https://fcm.googleapis.com/v1/projects/superchat-a933e/messages:send'

# FCM message payload
message_payload = {
    "message": {
        "token": "fcCnCC9UOKJLMoYSDWTJcL:APA91bGa5RUyLxohluLHJ7_3spUS2mM1CDFLZbYpM_Bhk5pZPd6XbtYq6yjQhYZekj30fvdakM9k_qyu8U3CPR4exvC05YAwD3BH8Kk7_NOsCRO4ldxqvrQ",
        "notification": {
            "title": "Food Alert",
            "body": "THE FOOD IS SPOILT! DO NOT EAT!",
        },
        "webpush": {
            "fcm_options": {
                "link": "https://google.com"
            }
        }
    }
}

# Load the service account key file
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=['https://www.googleapis.com/auth/firebase.messaging']
)

# Request an access token
request = Request()
credentials.refresh(request)
access_token = credentials.token

# Set up headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {access_token}'
}

# Send the FCM message
response = requests.post(FCM_ENDPOINT, headers=headers, data=json.dumps(message_payload))

# Print the response
print(response.status_code)
print(response.json())