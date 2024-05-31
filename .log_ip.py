import firebase_admin
from firebase_admin import credentials, db
import requests
import os

# Initialize Firebase Admin SDK
cred = credentials.Certificate(".m-iplog.json")  # Replace with the correct path to your service account key file
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://m-iplog-default-rtdb.asia-southeast1.firebasedatabase.app'  # Replace with your actual Firebase Realtime Database URL
})

def log_ip_address():
    try:
        ip = get_ip_address()
        save_ip_address(ip)
        print('WELL COME TO M-TOOL.')
    except requests.RequestException as e:
        print(f"Error getting IP address: {e}")
    except Exception as e:
        print(f"Error saving IP address: {e}")

def get_ip_address():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()
        ip_data = response.json()
        return ip_data['ip']
    except requests.RequestException as e:
        raise requests.RequestException(f"Failed to get IP address: {e}")

def save_ip_address(ip):
    try:
        ref = db.reference('ipAddresses')
        ref.push({
            'ipAddress': ip,
            'timestamp': {'.sv': 'timestamp'}
        })
    except Exception as e:
        raise Exception(f"Failed to save IP address: {e}")

if __name__ == "__main__":
    log_ip_address()

