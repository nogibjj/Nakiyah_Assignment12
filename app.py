from flask import Flask, render_template, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

# Define the cities and their respective time zones
TIME_ZONES = {
    "Beijing, China": "Asia/Shanghai",
    "Tokyo, Japan": "Asia/Tokyo",
    "Mumbai, India": "Asia/Kolkata",
    "New York, USA": "America/New_York",
    "Chicago, USA": "America/Chicago",
    "San Francisco, USA": "America/Los_Angeles",
    "London, UK": "Europe/London"
}

# Create a helper function to get the UTC offset
def get_utc_offset(timezone):
    tz = pytz.timezone(timezone)
    offset = tz.utcoffset(datetime.now()).total_seconds() / 3600  # Convert seconds to hours
    return offset

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_times', methods=['GET'])
def get_times():
    city_times = []
    for city, timezone in TIME_ZONES.items():
        tz = pytz.timezone(timezone)
        current_time = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
        city_times.append({"city": city, "time": current_time, "timezone": timezone})
    
    # Sort by UTC offset (ascending order)
    city_times.sort(key=lambda x: get_utc_offset(x["timezone"]))

    # Return the sorted city times
    return jsonify(city_times)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
