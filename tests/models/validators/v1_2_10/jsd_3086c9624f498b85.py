# -*- coding: utf-8 -*-
"""Cisco DNA Center Update Workflow data model.

Copyright (c) 2019-2021 Cisco Systems.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import json
from builtins import *

import fastjsonschema

from dnacentersdk.exceptions import MalformedRequest


class JSONSchemaValidator3086C9624F498B85(object):
    """Update Workflow request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator3086C9624F498B85, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "_id": {
                "type": [
                "string",
                "null"
                ]
                },
                "addToInventory": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "addedOn": {
                "type": [
                "number",
                "null"
                ]
                },
                "configId": {
                "type": [
                "string",
                "null"
                ]
                },
                "currTaskIdx": {
                "type": [
                "number",
                "null"
                ]
                },
                "description":
                 {
                "type": [
                "string",
                "null"
                ]
                },
                "endTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "execTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "imageId": {
                "type": [
                "string",
                "null"
                ]
                },
                "instanceType": {
                "type": [
                "string",
                "null"
                ]
                },
                "lastupdateOn": {
                "type": [
                "number",
                "null"
                ]
                },
                "name": {
                "type": [
                "string",
                "null"
                ]
                },
                "startTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "state": {
                "type": [
                "string",
                "null"
                ]
                },
                "tasks": {
                "items": {
                "properties": {
                "currWorkItemIdx": {
                "type": [
                "number",
                "null"
                ]
                },
                "endTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "name": {
                "type": [
                "string",
                "null"
                ]
                },
                "startTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "state": {
                "type": [
                "string",
                "null"
                ]
                },
                "taskSeqNo": {
                "type": [
                "number",
                "null"
                ]
                },
                "timeTaken": {
                "type": [
                "number",
                "null"
                ]
                },
                "type": {
                "type": [
                "string",
                "null"
                ]
                },
                "workItemList": {
                "items": {
                "properties": {
                "command": {
                "type": [
                "string",
                "null"
                ]
                },
                "endTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "outputStr": {
                "type": [
                "string",
                "null"
                ]
                },
                "startTime": {
                "type": [
                "number",
                "null"
                ]
                },
                "state": {
                "type": [
                "string",
                "null"
                ]
                },
                "timeTaken": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                }
                },
                "type": [
                "object",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "tenantId": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": {
                "type": [
                "string",
                "null"
                ]
                },
                "useState": {
                "type": [
                "string",
                "null"
                ]
                },
                "version": {
                "type": [
                "number",
                "null"
                ]
                }
                },
                "type": "object"
                }'''.replace("\n" + ' ' * 16, '')
        ))

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                '{} is invalid. Reason: {}'.format(request, e.message)
            )
