
from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

import argparse
parser = argparse.ArgumentParser(description='Commands vehicle using vehicle.simple_goto.')
parser.add_argument('--connect',
                   help="Vehicle connection target string. If not specified, SITL automatically started and used.")

parser.add_argument('--destination',
                   help="la destination pour go to.")

args = parser.parse_args()

connection_string = args.connect
home_string =args.home
sitl = None

connection_string = '127.0.0.1:14550'
# @nounou tcp:127.0.0.1:5760


# Connect to the Vehicle
print 'Connecting to vehicle on: %s' % connection_string
vehicle = connect(connection_string, wait_ready=True)
#vehicle.airspeed = 60

print "Going towards first point for 30 seconds ..."

destination = args.destination
point1 = LocationGlobalRelative(destination)
vehicle.simple_goto(point1)
print " Global Location: %s" % vehicle.location.global_frame
print " Global Location (relative altitude): %s" % vehicle.location.global_relative_frame
print " Local Location: %s" % vehicle.location.local_frame
time.sleep(30)

