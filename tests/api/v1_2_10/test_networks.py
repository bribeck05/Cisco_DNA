# -*- coding: utf-8 -*-
"""DNACenterAPI networks API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.2.10', reason='version does not match')


def is_valid_get_vlan_details(json_schema_validate, obj):
    json_schema_validate('jsd_6284db4649aa8d31_v1_2_10').validate(obj)
    return True


def get_vlan_details(api):
    endpoint_result = api.networks.get_vlan_details(

    )
    return endpoint_result


@pytest.mark.networks
def test_get_vlan_details(api, validator):
    assert is_valid_get_vlan_details(
        validator,
        get_vlan_details(api)
    )


def get_vlan_details_default(api):
    endpoint_result = api.networks.get_vlan_details(

    )
    return endpoint_result


@pytest.mark.networks
def test_get_vlan_details_default(api, validator):
    try:
        assert is_valid_get_vlan_details(
            validator,
            get_vlan_details_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site_topology(json_schema_validate, obj):
    json_schema_validate('jsd_9ba14a9e441b8a60_v1_2_10').validate(obj)
    return True


def get_site_topology(api):
    endpoint_result = api.networks.get_site_topology(

    )
    return endpoint_result


@pytest.mark.networks
def test_get_site_topology(api, validator):
    assert is_valid_get_site_topology(
        validator,
        get_site_topology(api)
    )


def get_site_topology_default(api):
    endpoint_result = api.networks.get_site_topology(

    )
    return endpoint_result


@pytest.mark.networks
def test_get_site_topology_default(api, validator):
    try:
        assert is_valid_get_site_topology(
            validator,
            get_site_topology_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_physical_topology(json_schema_validate, obj):
    json_schema_validate('jsd_b2b8cb91459aa58f_v1_2_10').validate(obj)
    return True


def get_physical_topology(api):
    endpoint_result = api.networks.get_physical_topology(
        node_type='string'
    )
    return endpoint_result


@pytest.mark.networks
def test_get_physical_topology(api, validator):
    assert is_valid_get_physical_topology(
        validator,
        get_physical_topology(api)
    )


def get_physical_topology_default(api):
    endpoint_result = api.networks.get_physical_topology(
        node_type=None
    )
    return endpoint_result


@pytest.mark.networks
def test_get_physical_topology_default(api, validator):
    try:
        assert is_valid_get_physical_topology(
            validator,
            get_physical_topology_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_l3_topology_details(json_schema_validate, obj):
    json_schema_validate('jsd_c2b5fb764d888375_v1_2_10').validate(obj)
    return True


def get_l3_topology_details(api):
    endpoint_result = api.networks.get_l3_topology_details(
        topology_type='string'
    )
    return endpoint_result


@pytest.mark.networks
def test_get_l3_topology_details(api, validator):
    assert is_valid_get_l3_topology_details(
        validator,
        get_l3_topology_details(api)
    )


def get_l3_topology_details_default(api):
    endpoint_result = api.networks.get_l3_topology_details(
        topology_type='string'
    )
    return endpoint_result


@pytest.mark.networks
def test_get_l3_topology_details_default(api, validator):
    try:
        assert is_valid_get_l3_topology_details(
            validator,
            get_l3_topology_details_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_topology_details(json_schema_validate, obj):
    json_schema_validate('jsd_b9b48ac8463a8aba_v1_2_10').validate(obj)
    return True


def get_topology_details(api):
    endpoint_result = api.networks.get_topology_details(
        vlan_id='string'
    )
    return endpoint_result


@pytest.mark.networks
def test_get_topology_details(api, validator):
    assert is_valid_get_topology_details(
        validator,
        get_topology_details(api)
    )


def get_topology_details_default(api):
    endpoint_result = api.networks.get_topology_details(
        vlan_id='string'
    )
    return endpoint_result


@pytest.mark.networks
def test_get_topology_details_default(api, validator):
    try:
        assert is_valid_get_topology_details(
            validator,
            get_topology_details_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_overall_network_health(json_schema_validate, obj):
    json_schema_validate('jsd_ca91da84401abba1_v1_2_10').validate(obj)
    return True


def get_overall_network_health(api):
    endpoint_result = api.networks.get_overall_network_health(
        timestamp=0
    )
    return endpoint_result


@pytest.mark.networks
def test_get_overall_network_health(api, validator):
    assert is_valid_get_overall_network_health(
        validator,
        get_overall_network_health(api)
    )


def get_overall_network_health_default(api):
    endpoint_result = api.networks.get_overall_network_health(
        timestamp=None
    )
    return endpoint_result


@pytest.mark.networks
def test_get_overall_network_health_default(api, validator):
    try:
        assert is_valid_get_overall_network_health(
            validator,
            get_overall_network_health_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
