#!/bin/python
# upnp manager for darkflame lego universe

import json
import sys, traceback

import upnpy
from upnpy.exceptions import *

import logging
import time

# global logger settings
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

log = logging.getLogger("Brickkeeper")
log.setLevel(logging.DEBUG)


def get_portmapings():
    log.info("Getting Port Mappings from portmapping.json")
    portmaping_data = {}
    try:
        with open('portmapping.json', 'r') as f:
            portmaping_data = json.load(f)
    except FileNotFoundError:
        log.error("Something went wrong when getting the portmaps from the json file!")
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print(traceback.print_exception(exc_type, exc_value, exc_traceback))

    if portmaping_data != {}:
        return portmaping_data


if __name__ == '__main__':
    ports = {}
    mapping = get_portmapings()
    print(mapping)

    upnp = upnpy.UPnP()

    count = 0
    succes = False
    igd = None
    while not succes and count < 10:
        time.sleep(2)
        try:
            igd = upnp.get_igd()

        except:
            print(f"Failed to get IGD count is {count}")
            succes = False
            count += 1
    if succes:
        service = igd['WANPPPConnection.1']
        service.get_actions()
