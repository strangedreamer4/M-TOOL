import firebase_admin
from firebase_admin import credentials, firestore
import requests

# Initialize Firebase
cred = credentials.Certificate(".m-iplog.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Function to log IP address
def log_ip():
    ip_address = requests.get('https://api.ipify.org').text
    db.collection('ip_logs').add({'ip_address': ip_address})

if __name__ == "__main__":
    log_ip()
