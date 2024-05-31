import firebase_admin
from firebase_admin import credentials, db
import requests

# Initialize Firebase Admin SDK
cred = credentials.Certificate(".m-iplog.json")  # Replace "path/to/serviceAccountKey.json" with the path to your service account key file
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://m-iplog-default-rtdb.asia-southeast1.firebasedatabase.app'
})

def log_ip_address():
    try:
        ip = get_ip_address()
        save_ip_address(ip)
        print('WELLCOME TO M-TOOL.')
    except requests.RequestException as e:
        print(f"Error logging IP address: {e}")

def get_ip_address():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_data = response.json()
        return ip_data['ip']
    except requests.RequestException as e:
        raise e

def save_ip_address(ip):
    try:
        ref = db.reference('ipAddresses')
        ref.push({
            'ipAddress': ip
        })
    except Exception as e:
        raise e

if __name__ == "__main__":
    log_ip_address()
