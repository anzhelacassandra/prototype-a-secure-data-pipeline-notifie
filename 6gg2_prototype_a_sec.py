import hashlib
import hmac
import os
import json
import requests

# Configuration
DATA_PIPELINE_API_KEY = 'YOUR_API_KEY'
DATA_PIPELINE_API_SECRET = 'YOUR_API_SECRET'
NOTIFICATION_ENDPOINT = 'https://example.com/notify'

# Secure Data Pipeline Notifier class
class SecureNotifier:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def notify(self, data):
        # Create a JSON payload
        payload = json.dumps(data)

        # Calculate the HMAC signature
        signature = hmac.new(self.api_secret.encode(), payload.encode(), hashlib.sha256).hexdigest()

        # Set the Authorization header
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'X-Signature': signature
        }

        # Send the notification request
        response = requests.post(NOTIFICATION_ENDPOINT, headers=headers, data=payload)

        # Check the response status code
        if response.status_code == 200:
            print('Notification sent successfully!')
        else:
            print('Failed to send notification.')

# Test case: Notify a data pipeline update
if __name__ == '__main__':
    notifier = SecureNotifier(DATA_PIPELINE_API_KEY, DATA_PIPELINE_API_SECRET)

    data = {
        'pipeline_id': 'my_pipeline',
        'status': 'UPDATE_COMPLETED',
        'message': 'Data pipeline updated successfully!'
    }

    notifier.notify(data)