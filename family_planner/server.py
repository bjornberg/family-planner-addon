#!/usr/bin/env python3
"""
Family Planner Backend Server - Home Assistant Add-on versie
Simpel Flask server voor het opslaan van Family Planner data in een JSON bestand.
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # Staat API calls toe vanaf de HTML pagina

# Data wordt opgeslagen in /data directory (persistent in HA add-on)
DATA_DIR = '/data' if os.path.exists('/data') else '.'
DATA_FILE = os.path.join(DATA_DIR, 'data.json')

def load_data():
    """Laad data uit JSON bestand"""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return get_empty_data()
    return get_empty_data()

def save_data(data):
    """Sla data op in JSON bestand"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def get_empty_data():
    """Retourneer lege data structuur"""
    return {
        'events': [],
        'tasks': [],
        'recurring': [],
        'completed': {},
        'history': {}
    }

@app.route('/')
def index():
    """Serve de Family Planner HTML"""
    return send_from_directory(DATA_DIR, 'family-planner.html')

@app.route('/family-planner.html')
def app_page():
    """Serve de Family Planner HTML"""
    return send_from_directory(DATA_DIR, 'family-planner.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    """Haal alle data op"""
    data = load_data()
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def update_data():
    """Sla alle data op"""
    data = request.json
    save_data(data)
    return jsonify({'status': 'success'})

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok', 'message': 'Family Planner Server is running'})

if __name__ == '__main__':
    # Maak leeg data bestand aan als het niet bestaat
    if not os.path.exists(DATA_FILE):
        save_data(get_empty_data())
        print(f"✓ {DATA_FILE} aangemaakt")

    print("=" * 50)
    print("🚀 Family Planner Server gestart!")
    print("=" * 50)
    print(f"📁 Data bestand: {DATA_FILE}")
    print(f"🌐 Server draait op: http://0.0.0.0:5000")
    print("=" * 50)

    # Start server op alle netwerk interfaces
    app.run(host='0.0.0.0', port=5000, debug=False)
