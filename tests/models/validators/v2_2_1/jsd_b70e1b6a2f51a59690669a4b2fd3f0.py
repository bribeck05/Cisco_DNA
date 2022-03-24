# -*- coding: utf-8 -*-
"""Cisco DNA Center complianceDetailsOfDevice data model.

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


class JSONSchemaValidatorB70E1B6A2F51A59690669A4B2Fd3F0(object):
    """complianceDetailsOfDevice request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorB70E1B6A2F51A59690669A4B2Fd3F0, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "deviceUuid": {
                "type": "string"
                },
                "response": {
                "items": {
                "properties": {
                "additionalDataURL": {
                "type": "string"
                },
                "category": {
                "type": "string"
                },
                "complianceType": {
                "type": "string"
                },
                "deviceUuid": {
                "type": "string"
                },
                "displayName": {
                "type": "string"
                },
                "lastSyncTime": {
                "type": "string"
                },
                "lastUpdateTime": {
                "type": "string"
                },
                "message": {
                "type": "string"
                },
                "sourceInfoList": {
                "items": {
                "properties": {
                "appName": {
                "type": "string"
                },
                "businessKey": {
                "properties": {
                "businessKeyAttributes": {
                "type": "string"
                },
                "otherAttributes": {
                "properties": {
                "cfsAttributes": {
                "type": "string"
                },
                "name": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "resourceName": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "count": {
                "type": "number"
                },
                "diffList": {
                "items": {
                "properties": {
                "businessKey": {
                "type": "string"
                },
                "configuredValue": {
                "type": "string"
                },
                "displayName": {
                "type": "string"
                },
                "extendedAttributes": {
                "type": "string"
                },
                "intendedValue": {
                "type": "string"
                },
                "moveFromPath": {
                "type": "string"
                },
                "op": {
                "type": "string"
                },
                "path": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "displayName": {
                "type": "string"
                },
                "licenseAppName": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "nameWithBusinessKey": {
                "type": "string"
                },
                "networkProfileName": {
                "type": "string"
                },
                "provisioningArea": {
                "type": "string"
                },
                "sourceEnum": {
                "type": "string"
                },
                "type": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "state": {
                "type": "string"
                },
                "status": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "version": {
                "type": "string"
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
