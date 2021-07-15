# -*- coding: utf-8 -*-
"""Cisco DNA Center getSiteHealth data model.

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


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import fastjsonschema
import json
from dnacentersdk.exceptions import MalformedRequest

from builtins import *


class JSONSchemaValidatorAe4B592F66035F24B55028F79C1B7290(object):
    """getSiteHealth request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorAe4B592F66035F24B55028F79C1B7290, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "items": {
                "properties": {
                "accessGoodCount": {
                "type": "object"
                },
                "accessTotalCount": {
                "type": "object"
                },
                "applicationBytesTotalCount": {
                "type": "object"
                },
                "applicationGoodCount": {
                "type": "object"
                },
                "applicationHealth": {
                "type": "object"
                },
                "applicationHealthStats": {
                "properties": {
                "appTotalCount": {
                "type": "number"
                },
                "businessIrrelevantAppCount": {
                "properties": {
                "fair": {
                "type": "number"
                },
                "good": {
                "type": "number"
                },
                "poor": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "businessRelevantAppCount": {
                "properties": {
                "fair": {
                "type": "number"
                },
                "good": {
                "type": "number"
                },
                "poor": {
                "type": "number"
                }
                },
                "type": "object"
                },
                "defaultHealthAppCount": {
                "properties": {
                "fair": {
                "type": "number"
                },
                "good": {
                "type": "number"
                },
                "poor": {
                "type": "number"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "applicationTotalCount": {
                "type": "object"
                },
                "clientHealthWired": {
                "type": "object"
                },
                "clientHealthWireless": {
                "type": "object"
                },
                "coreGoodCount": {
                "type": "object"
                },
                "coreTotalCount": {
                "type": "object"
                },
                "distributionGoodCount": {
                "type": "object"
                },
                "distributionTotalCount": {
                "type": "object"
                },
                "dnacInfo": {
                "type": "object"
                },
                "healthyClientsPercentage": {
                "type": "object"
                },
                "healthyNetworkDevicePercentage": {
                "type": "object"
                },
                "latitude": {
                "type": "number"
                },
                "longitude": {
                "type": "number"
                },
                "networkHealthAccess": {
                "type": "object"
                },
                "networkHealthAverage": {
                "type": "object"
                },
                "networkHealthCore": {
                "type": "object"
                },
                "networkHealthDistribution": {
                "type": "object"
                },
                "networkHealthOthers": {
                "type": "object"
                },
                "networkHealthRouter": {
                "type": "object"
                },
                "networkHealthWireless": {
                "type": "object"
                },
                "numberOfClients": {
                "type": "object"
                },
                "numberOfNetworkDevice": {
                "type": "object"
                },
                "numberOfWiredClients": {
                "type": "object"
                },
                "numberOfWirelessClients": {
                "type": "object"
                },
                "overallGoodDevices": {
                "type": "object"
                },
                "parentSiteId": {
                "type": "string"
                },
                "parentSiteName": {
                "type": "string"
                },
                "routerGoodCount": {
                "type": "object"
                },
                "routerTotalCount": {
                "type": "object"
                },
                "siteId": {
                "type": "string"
                },
                "siteName": {
                "type": "string"
                },
                "siteType": {
                "type": "string"
                },
                "totalNumberOfActiveWirelessClients": {
                "type": "object"
                },
                "totalNumberOfConnectedWiredClients": {
                "type": "object"
                },
                "wiredGoodClients": {
                "type": "object"
                },
                "wirelessDeviceGoodCount": {
                "type": "object"
                },
                "wirelessDeviceTotalCount": {
                "type": "object"
                },
                "wirelessGoodClients": {
                "type": "object"
                }
                },
                "type": "object"
                },
                "type": "array"
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