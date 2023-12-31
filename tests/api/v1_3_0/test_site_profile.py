# -*- coding: utf-8 -*-
"""DNACenterAPI site_profile API fixtures and tests.

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
import pytest
from fastjsonschema.exceptions import JsonSchemaException
from dnacentersdk.exceptions import MalformedRequest
from tests.environment import DNA_CENTER_VERSION

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.3.0', reason='version does not match')


def is_valid_get_device_details_by_ip(json_schema_validate, obj):
    json_schema_validate('jsd_7fbe4b804879baa4_v1_3_0').validate(obj)
    return True


def get_device_details_by_ip(api):
    endpoint_result = api.site_profile.get_device_details_by_ip(
        device_ip='string'
    )
    return endpoint_result


@pytest.mark.site_profile
def test_get_device_details_by_ip(api, validator):
    assert is_valid_get_device_details_by_ip(
        validator,
        get_device_details_by_ip(api)
    )


def get_device_details_by_ip_default(api):
    endpoint_result = api.site_profile.get_device_details_by_ip(
        device_ip=None
    )
    return endpoint_result


@pytest.mark.site_profile
def test_get_device_details_by_ip_default(api, validator):
    try:
        assert is_valid_get_device_details_by_ip(
            validator,
            get_device_details_by_ip_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_provision_nfv(json_schema_validate, obj):
    json_schema_validate('jsd_828828f44f28bd0d_v1_3_0').validate(obj)
    return True


def provision_nfv(api):
    endpoint_result = api.site_profile.provision_nfv(
        active_validation=True,
        payload=None,
        provisioning=[{'site': {'siteProfileName': 'string', 'area': {'name': 'string', 'parentName': 'string'}, 'building': {'name': 'string', 'address': 'string', 'latitude': 0, 'longitude': 0, 'parentName': 'string'}, 'floor': {'name': 'string', 'parentName': 'string', 'rfModel': 'string', 'width': 0, 'length': 0, 'height': 0}}, 'device': [{'ip': 'string', 'deviceSerialNumber': 'string', 'tagName': 'string', 'serviceProviders': [{'serviceProvider': 'string', 'wanInterface': {'ipAddress': 'string', 'interfaceName': 'string', 'subnetmask': 'string', 'bandwidth': 'string', 'gateway': 'string'}}], 'services': [{'type': 'string', 'mode': 'string', 'systemIp': 'string', 'centralManagerIP': 'string', 'centralRegistrationKey': 'string', 'commonKey': 'string', 'adminPasswordHash': 'string'}], 'vlan': [{'type': 'string', 'id': 'string', 'interfaces': 'string', 'network': 'string'}], 'subPools': [{'type': 'Lan', 'name': 'string', 'ipSubnet': 'string', 'gateway': 'string', 'parentPoolName': 'string'}], 'customNetworks': [{'name': 'string', 'port': 'string', 'ipAddressPool': 'string'}], 'templateParam': {'nfvis': {'var1': 'string'}, 'asav': {'var1': 'string'}}}]}],
        siteProfile=[{'siteProfileName': 'string', 'device': [{'deviceType': 'ENCS5100', 'tagName': 'string', 'serviceProviders': [{'serviceProvider': 'string', 'linkType': 'GigabitEthernet', 'connect': True, 'defaultGateway': True}], 'dia': True, 'services': [{'type': 'isr', 'profile': 'string', 'mode': 'string'}], 'customServices': [{'name': 'string', 'applicationType': 'string', 'profile': 'string'}], 'customNetworks': [{'name': 'string', 'servicesToConnect': [{'service': 'string'}], 'connectionType': 'string', 'networkMode': 'string', 'vlan': 'string'}], 'vlan': [{'type': 'string', 'id': 'string'}], 'customTemplate': [{'deviceType': 'NFVIS', 'template': 'string'}]}]}]
    )
    return endpoint_result


@pytest.mark.site_profile
def test_provision_nfv(api, validator):
    assert is_valid_provision_nfv(
        validator,
        provision_nfv(api)
    )


def provision_nfv_default(api):
    endpoint_result = api.site_profile.provision_nfv(
        active_validation=True,
        payload=None,
        provisioning=None,
        siteProfile=None
    )
    return endpoint_result


@pytest.mark.site_profile
def test_provision_nfv_default(api, validator):
    try:
        assert is_valid_provision_nfv(
            validator,
            provision_nfv_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_nfv_provisioning_detail(json_schema_validate, obj):
    json_schema_validate('jsd_2f97e8fa45f8b2a3_v1_3_0').validate(obj)
    return True


def nfv_provisioning_detail(api):
    endpoint_result = api.site_profile.nfv_provisioning_detail(
        active_validation=True,
        device_ip='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.site_profile
def test_nfv_provisioning_detail(api, validator):
    assert is_valid_nfv_provisioning_detail(
        validator,
        nfv_provisioning_detail(api)
    )


def nfv_provisioning_detail_default(api):
    endpoint_result = api.site_profile.nfv_provisioning_detail(
        active_validation=True,
        device_ip=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.site_profile
def test_nfv_provisioning_detail_default(api, validator):
    try:
        assert is_valid_nfv_provisioning_detail(
            validator,
            nfv_provisioning_detail_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
