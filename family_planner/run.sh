#!/usr/bin/with-contenv bashio

bashio::log.info "Starting Family Planner..."

# Get port from config
PORT=$(bashio::config 'port')

bashio::log.info "Data will be stored in /data/data.json"
bashio::log.info "Web interface available on port ${PORT}"

# Create data directory if it doesn't exist
mkdir -p /data

# Copy HTML to data directory so it's accessible
cp /app/family-planner.html /data/

# Start Flask server
cd /data
exec python3 /app/server.py
