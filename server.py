from flask import Flask, request, send_from_directory
from flask_cors import CORS
from datetime import datetime
import requests
import os

app = Flask(__name__, static_folder="static")
CORS(app)

@app.route('/location', methods=['POST'])
def location():
    data = request.json
    ip = data.get("ip")
    ua = data.get("userAgent")
    ip_type = "IPv6" if ":" in ip else "IPv4"

    # Get location info from ip-api
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        location_data = response.json()
        city = location_data.get("city", "Unknown")
        region = location_data.get("regionName", "")
        country = location_data.get("country", "")
    except:
        city = region = country = "Unknown"

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("visitor_logs.txt", "a") as f:
        f.write(f"[{time}] IP: {ip} ({ip_type}), Location: {city}, {region}, {country}, UA: {ua}\n")

    return "Logged", 200

@app.route('/track.html')
def track_page():
    return send_from_directory(app.static_folder, "track.html")

@app.route('/')
def home():
    return "<h3>✅ Flask server is running</h3>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

