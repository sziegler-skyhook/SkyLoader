#! /bin/python3
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--host', help='DNS name or IP address for host', type = str)
parser.add_argument('--users', help='Number of users to simulate', type = int)
parser.add_argument('--ramp', help='Number of users to spawn per second', type = int)


# Request Types
parser.add_argument('--health', help='Enable health check testing', action="store_true")
parser.add_argument('--loc', help='Enable location testing', action="store_true")
parser.add_argument('--ip_loc', help='Enable IP location testing', action="store_true")
parser.add_argument('--tiling', help='Enable tiling testing', action="store_true")
parser.add_argument('--rgeo', help='Enable RGeo testing', action="store_true")

parser.parse_args()