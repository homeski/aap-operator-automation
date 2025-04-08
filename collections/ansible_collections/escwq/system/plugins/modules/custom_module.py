#!/usr/bin/python

# Copyright: (c) 2021, Shane McDonald <shanemcd@redhat.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: custom_module

short_description: A custom module

version_added: "1.0.0"

description: This is a module that is custom

options:
    number:
        description: The number printed will be what is set + 1
        required: true
        type: int
    msg:
        description: Print a 'msg
        required: true
        type: str

author:
    - Homero Pawlowski
'''
