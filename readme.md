# SkyLoader

Skyloader is a load testing tool designed to generate production like traffic patterns for use in testing Skyhook infrastructure

## Requirements 

- Locust
- Emoji (Please forgive me of my sins)

`pip install -r requirements.txt`

## Usage
```
usage: skyloader [-h] [--host HOST] [--users USERS] [--ramp RAMP] [--workers WORKERS] [--headless] [--health] [--loc] [--ip_loc] [--tiling] [--rgeo] [--no_emoji]

optional arguments:
  -h, --help         show this help message and exit
  --host HOST        DNS name or IP address for host
  --users USERS      Number of users to simulate
  --ramp RAMP        Number of users to spawn per second
  --workers WORKERS  Number of docker compose workers to spawn
  --headless         Do not open a web browser
  --health           Enable health check testing
  --loc              Enable location testing
  --ip_loc           Enable IP location testing
  --tiling           Enable tiling testing
  --rgeo             Enable RGeo testing
  --no_emoji         Disable emoji output on startup
```
