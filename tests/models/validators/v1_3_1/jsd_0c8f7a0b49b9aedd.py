# -*- coding: utf-8 -*-
"""Cisco DNA Center Get software image details data model.

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


class JSONSchemaValidator0C8F7A0B49B9Aedd(object):
    """Get software image details request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator0C8F7A0B49B9Aedd, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "properties": {
                "response": {
                "items": {
                "properties": {
                "applicableDevicesForImage": {
                "items": {
                "properties": {
                "mdfId": {
                "type": [
                "string",
                "null"
                ]
                },
                "productId": {
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "productName": {
                "type": [
                "string",
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
                "applicationType": {
                "type": [
                "string",
                "null"
                ]
                },
                "createdTime": {
                "type": [
                "string",
                "null"
                ]
                },
                "extendedAttributes": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "family": {
                "type": [
                "string",
                "null"
                ]
                },
                "feature": {
                "type": [
                "string",
                "null"
                ]
                },
                "fileServiceId": {
                "type": [
                "string",
                "null"
                ]
                },
                "fileSize": {
                "type": [
                "string",
                "null"
                ]
                },
                "imageIntegrityStatus": {
                "type": [
                "string",
                "null"
                ]
                },
                "imageName": {
                "type": [
                "string",
                "null"
                ]
                },
                "imageSeries": {
                "items": {
                "type": [
                "string",
                "null"
                ]
                },
                "type": [
                "array",
                "null"
                ]
                },
                "imageSource": {
                "type": [
                "string",
                "null"
                ]
                },
                "imageType": {
                "type": [
                "string",
                "null"
                ]
                },
                "imageUuid": {
                "type": [
                "string",
                "null"
                ]
                },
                "importSourceType": {
                "enum": [
                "DEVICE",
                "REMOTEURL",
                "CCO",
                "FILESYSTEM",
                null
                ],
                "type": [
                "string",
                "null"
                ]
                },
                "isTaggedGolden": {
                "type": [
                "boolean",
                "null"
                ]
                },
                "md5Checksum": {
                "type": [
                "string",
                "null"
                ]
                },
                "name": {
                "type": [
                "string",
                "null"
                ]
                },
                "profileInfo": {
                "items": {
                "properties": {
                "description":
                 {
                "type": [
                "string",
                "null"
                ]
                },
                "extendedAttributes": {
                "properties": {},
                "type": [
                "object",
                "null"
                ]
                },
                "memory": {
                "type": [
                "number",
                "null"
                ]
                },
                "productType": {
                "type": [
                "string",
                "null"
                ]
                },
                "profileName": {
                "type": [
                "string",
                "null"
                ]
                },
                "shares": {
                "type": [
                "number",
                "null"
                ]
                },
                "vCpu": {
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
                },
                "shaCheckSum": {
                "type": [
                "string",
                "null"
                ]
                },
                "vendor": {
                "type": [
                "string",
                "null"
                ]
                },
                "version": {
                "type": [
                "string",
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
                "version": {
                "type": [
                "string",
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
