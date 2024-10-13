import json
import requests
from google.oauth2 import service_account
from google.auth.transport.requests import Request
import firebase_admin
from firebase_admin import credentials, firestore

# Path to your service account key file
SERVICE_ACCOUNT_FILE = '../serviceAccountKey.json'

# FCM endpoint
FCM_ENDPOINT = 'https://fcm.googleapis.com/v1/projects/superchat-a933e/messages:send'

# Initialize Firebase Admin SDK
cred = credentials.Certificate(SERVICE_ACCOUNT_FILE)
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

def send_fcm_message(title, body, alert_type):
    # Retrieve all tokens from the "users" collection
    tokens = []
    users_ref = db.collection('users')
    docs = users_ref.stream()

    for doc in docs:
        user_data = doc.to_dict()
        if 'notificationToken' in user_data:
            tokens.append(user_data['notificationToken'])

    # FCM message payload
    message_payload = {
        "message": {
            "data": {
                "title": title,
                "body": body,
                "alert_type": alert_type
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

    # Send the FCM message to each token
    for token in tokens:
        message_payload['message']['token'] = token
        response = requests.post(FCM_ENDPOINT, headers=headers, data=json.dumps(message_payload))
        
        # Print the response
        print(f'Status code for token {token}: {response.status_code}')
        print(response.json())

# Example usage
# send_fcm_message("Food Alert", "THE FOOD is gross haha", "warning")