import firebase_admin
from firebase_admin import credentials, firestore
import requests
import time

# Initialize Firebase
try:
    cred = credentials.Certificate(".m-iplog.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
except Exception as e:
    print("Error initializing Firebase:", e)
    exit(1)

# Function to log IP address
def log_ip():
    try:
        ip_address = requests.get('https://api.ipify.org').text
        db.collection('ip_logs').add({'ip_address': ip_address})
    except Exception as e:
        print("Error logging IP address:", e)

if __name__ == "__main__":
    log_ip()
