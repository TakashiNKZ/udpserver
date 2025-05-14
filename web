from flask import Flask, render_template, jsonify
from collections import defaultdict, deque
import os

app = Flask(__name__)

LOG_FILE = 'logs.txt'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logs')
def get_logs():
    logs_by_point = defaultdict(lambda: deque(maxlen=10))

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) >= 4:
                    point = parts[0]
                    logs_by_point[point].append(line.strip())

    grouped_logs = []
    for point in sorted(logs_by_point.keys()):
        grouped_logs.append(f"--- {point} ---")
        grouped_logs.extend(logs_by_point[point])
        grouped_logs.append("")  

    return jsonify(logs=grouped_logs)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

