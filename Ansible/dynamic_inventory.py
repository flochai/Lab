#!/usr/bin/env python3

'''
Dynamic inventory for Ansible in Python
'''

# Use print functionality from Python 3 for compatibility
from __future__ import print_function

import argparse
import logging

# Attempt to import json, if it fails, import simplejson
try:
    import json
except ImportError:
    import simplejson as json

# Inherit from object for Python 2/3 compatibility
class Inventory(object):

    # Constructor
    def __init__(self, include_hostvars_in_list):

        # Configure logger
        self.configure_logger()

        # Capture and store include_hostvars_in_list
        self.include_hostvars_in_list = include_hostvars_in_list

        # Capture the script command line arguments
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action='store_true',
                            help='list inventory')
        parser.add_argument('--host', action='store',
                            help='show HOST variables')
        self.args = parser.parse_args()

        # If not called with --host or --list, show usage and exit
        if not (self.args.list or self.args.host):
            parser.print_usage()
            raise SystemExit

        # Capture and store the inventory
        self.define_inventory()

        # When called with --list, print the inventory
        if self.args.list:
            self.print_json(self.list())

        # If called with --host, print host information
        elif self.args.host:
            self.print_json(self.host())

    def define_inventory(self):
        self.groups = {
            "centos": {
                "hosts": ["centos1", "centos2", "centos3"],
                "vars": {
                    "ansible_user": 'root'
                }
            },
            "control": {
                "hosts": ["ubuntu-c"],
"inventory.py" 135L, 14932B                                                                                                                                                                                      1,1           Top
