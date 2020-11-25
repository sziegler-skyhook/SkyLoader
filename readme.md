# SkyLoader

Skyloader is a load testing tool designed to generate production like traffic patterns for use in testing Skyhook infrastructure

## Requirements 

- Locust

`pip install -r requirements.txt`

## Usage
```
usage: skyloader.py [-h] [--host HOST] [--users USERS] [--ramp RAMP] [--health] [--loc] [--ip_loc] [--tiling] [--rgeo]

optional arguments:
  -h, --help     show this help message and exit
  --host HOST    DNS name or IP address for host
  --users USERS  Number of users to simulate
  --ramp RAMP    Number of users to spawn per second
  --health       Enable health check testing
  --loc          Enable location testing
  --ip_loc       Enable IP location testing
  --tiling       Enable tiling testing
  --rgeo         Enable RGeo testing
```
