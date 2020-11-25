#! /bin/python3
import argparse
import os
import webbrowser

parser = argparse.ArgumentParser()

parser.add_argument('--host', help='DNS name or IP address for host', type = str)
parser.add_argument('--users', help='Number of users to simulate', type = int)
parser.add_argument('--ramp', help='Number of users to spawn per second', type = int)
parser.add_argument('--workers', help='Number of docker compose workers to spawn', type = int)
parser.add_argument('--headless', help='Do not open a web browser', action="store_true")

# Request Types
parser.add_argument('--health', help='Enable health check testing', action="store_true")
parser.add_argument('--loc', help='Enable location testing', action="store_true")
parser.add_argument('--ip_loc', help='Enable IP location testing', action="store_true")
parser.add_argument('--tiling', help='Enable tiling testing', action="store_true")
parser.add_argument('--rgeo', help='Enable RGeo testing', action="store_true")

args = parser.parse_args()

# Construct locust command base on Skyloader args
if not args.health and not args.loc and not args.ip_loc and not args.tiling and not args.rgeo:
    tags = ""
else:
    tags = "--tags "

if args.health:
    tags = tags + "HealthCheck "
if args.loc:
    tags = tags + "LocationRQ "
if args.ip_loc:
    tags = tags + "IPLocationRQ "
if args.tiling:
    tags = tags + "TilingRQ "
if args.rgeo:
    tags = tags + "RGeoRQ"

if args.headless:
    headless = "--headless"
    if not args.host or not args.users or not args.ramp:
        raise AttributeError('Host, users, and ramp args must be specified if headless mode is enabled')
else:
    webbrowser.open("http://localhost:8089")
    headless = ""

if args.workers:
    raise AttributeError('Sorry, SkyLoader doesnt support Docker workers yet')
else:
    os.system("locust {headless} {tags}".format(tags=tags, headless=headless))



