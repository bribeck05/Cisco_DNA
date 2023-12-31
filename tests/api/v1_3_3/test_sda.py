# -*- coding: utf-8 -*-
"""DNACenterAPI sda API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.3.3', reason='version does not match')


def is_valid_delete_port_assignment_for_access_point(json_schema_validate, obj):
    json_schema_validate('jsd_07874a4c4c9aabd9_v1_3_3').validate(obj)
    return True


def delete_port_assignment_for_access_point(api):
    endpoint_result = api.sda.delete_port_assignment_for_access_point(
        device_ip='string',
        interface_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_port_assignment_for_access_point(api, validator):
    assert is_valid_delete_port_assignment_for_access_point(
        validator,
        delete_port_assignment_for_access_point(api)
    )


def delete_port_assignment_for_access_point_default(api):
    endpoint_result = api.sda.delete_port_assignment_for_access_point(
        device_ip=None,
        interface_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_port_assignment_for_access_point_default(api, validator):
    try:
        assert is_valid_delete_port_assignment_for_access_point(
            validator,
            delete_port_assignment_for_access_point_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_sda_fabric_info(json_schema_validate, obj):
    json_schema_validate('jsd_16a1bb5d48cb873d_v1_3_3').validate(obj)
    return True


def get_sda_fabric_info(api):
    endpoint_result = api.sda.get_sda_fabric_info(
        fabric_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_sda_fabric_info(api, validator):
    assert is_valid_get_sda_fabric_info(
        validator,
        get_sda_fabric_info(api)
    )


def get_sda_fabric_info_default(api):
    endpoint_result = api.sda.get_sda_fabric_info(
        fabric_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_sda_fabric_info_default(api, validator):
    try:
        assert is_valid_get_sda_fabric_info(
            validator,
            get_sda_fabric_info_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_vn(json_schema_validate, obj):
    json_schema_validate('jsd_2eb1fa1e49caa2b4_v1_3_3').validate(obj)
    return True


def get_vn(api):
    endpoint_result = api.sda.get_vn(
        site_name_hierarchy='string',
        virtual_network_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_vn(api, validator):
    assert is_valid_get_vn(
        validator,
        get_vn(api)
    )


def get_vn_default(api):
    endpoint_result = api.sda.get_vn(
        site_name_hierarchy=None,
        virtual_network_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_vn_default(api, validator):
    try:
        assert is_valid_get_vn(
            validator,
            get_vn_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_info(json_schema_validate, obj):
    json_schema_validate('jsd_138518e14069ab5f_v1_3_3').validate(obj)
    return True


def get_device_info(api):
    endpoint_result = api.sda.get_device_info(
        device_ipaddress='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_device_info(api, validator):
    assert is_valid_get_device_info(
        validator,
        get_device_info(api)
    )


def get_device_info_default(api):
    endpoint_result = api.sda.get_device_info(
        device_ipaddress=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_device_info_default(api, validator):
    try:
        assert is_valid_get_device_info(
            validator,
            get_device_info_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_ip_pool_in_sda_virtual_network(json_schema_validate, obj):
    json_schema_validate('jsd_208579ea4ed98f4f_v1_3_3').validate(obj)
    return True


def add_ip_pool_in_sda_virtual_network(api):
    endpoint_result = api.sda.add_ip_pool_in_sda_virtual_network(
        active_validation=True,
        payload=[{'virtualNetworkName': 'string', 'ipPoolName': 'string', 'trafficType': 'string', 'authenticationPolicyName': 'string', 'scalableGroupName': 'string', 'isL2FloodingEnabled': True, 'isThisCriticalPool': True, 'poolType': 'string'}]
    )
    return endpoint_result


@pytest.mark.sda
def test_add_ip_pool_in_sda_virtual_network(api, validator):
    assert is_valid_add_ip_pool_in_sda_virtual_network(
        validator,
        add_ip_pool_in_sda_virtual_network(api)
    )


def add_ip_pool_in_sda_virtual_network_default(api):
    endpoint_result = api.sda.add_ip_pool_in_sda_virtual_network(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_ip_pool_in_sda_virtual_network_default(api, validator):
    try:
        assert is_valid_add_ip_pool_in_sda_virtual_network(
            validator,
            add_ip_pool_in_sda_virtual_network_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_edge_device(json_schema_validate, obj):
    json_schema_validate('jsd_1fb8f9f24c998133_v1_3_3').validate(obj)
    return True


def delete_edge_device(api):
    endpoint_result = api.sda.delete_edge_device(
        device_ipaddress='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_edge_device(api, validator):
    assert is_valid_delete_edge_device(
        validator,
        delete_edge_device(api)
    )


def delete_edge_device_default(api):
    endpoint_result = api.sda.delete_edge_device(
        device_ipaddress=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_edge_device_default(api, validator):
    try:
        assert is_valid_delete_edge_device(
            validator,
            delete_edge_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_default_authentication_profile(json_schema_validate, obj):
    json_schema_validate('jsd_3ebcda3e4acbafb7_v1_3_3').validate(obj)
    return True


def delete_default_authentication_profile(api):
    endpoint_result = api.sda.delete_default_authentication_profile(
        site_name_hierarchy='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_default_authentication_profile(api, validator):
    assert is_valid_delete_default_authentication_profile(
        validator,
        delete_default_authentication_profile(api)
    )


def delete_default_authentication_profile_default(api):
    endpoint_result = api.sda.delete_default_authentication_profile(
        site_name_hierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_default_authentication_profile_default(api, validator):
    try:
        assert is_valid_delete_default_authentication_profile(
            validator,
            delete_default_authentication_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_port_assignment_for_access_point(json_schema_validate, obj):
    json_schema_validate('jsd_5097f8d445f98f51_v1_3_3').validate(obj)
    return True


def get_port_assignment_for_access_point(api):
    endpoint_result = api.sda.get_port_assignment_for_access_point(
        device_ip='string',
        interface_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_port_assignment_for_access_point(api, validator):
    assert is_valid_get_port_assignment_for_access_point(
        validator,
        get_port_assignment_for_access_point(api)
    )


def get_port_assignment_for_access_point_default(api):
    endpoint_result = api.sda.get_port_assignment_for_access_point(
        device_ip=None,
        interface_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_port_assignment_for_access_point_default(api, validator):
    try:
        assert is_valid_get_port_assignment_for_access_point(
            validator,
            get_port_assignment_for_access_point_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_site(json_schema_validate, obj):
    json_schema_validate('jsd_50864acf4ad8b54d_v1_3_3').validate(obj)
    return True


def delete_site(api):
    endpoint_result = api.sda.delete_site(
        site_name_hierarchy='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_site(api, validator):
    assert is_valid_delete_site(
        validator,
        delete_site(api)
    )


def delete_site_default(api):
    endpoint_result = api.sda.delete_site(
        site_name_hierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_site_default(api, validator):
    try:
        assert is_valid_delete_site(
            validator,
            delete_site_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_vn(json_schema_validate, obj):
    json_schema_validate('jsd_518c59cd441aa9fc_v1_3_3').validate(obj)
    return True


def add_vn(api):
    endpoint_result = api.sda.add_vn(
        active_validation=True,
        payload=[{'virtualNetworkName': 'string', 'siteNameHierarchy': 'string'}]
    )
    return endpoint_result


@pytest.mark.sda
def test_add_vn(api, validator):
    assert is_valid_add_vn(
        validator,
        add_vn(api)
    )


def add_vn_default(api):
    endpoint_result = api.sda.add_vn(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_vn_default(api, validator):
    try:
        assert is_valid_add_vn(
            validator,
            add_vn_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_ip_pool_from_sda_virtual_network(json_schema_validate, obj):
    json_schema_validate('jsd_549e4aff42bbb52a_v1_3_3').validate(obj)
    return True


def delete_ip_pool_from_sda_virtual_network(api):
    endpoint_result = api.sda.delete_ip_pool_from_sda_virtual_network(
        ip_pool_name='string',
        virtual_network_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_ip_pool_from_sda_virtual_network(api, validator):
    assert is_valid_delete_ip_pool_from_sda_virtual_network(
        validator,
        delete_ip_pool_from_sda_virtual_network(api)
    )


def delete_ip_pool_from_sda_virtual_network_default(api):
    endpoint_result = api.sda.delete_ip_pool_from_sda_virtual_network(
        ip_pool_name=None,
        virtual_network_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_ip_pool_from_sda_virtual_network_default(api, validator):
    try:
        assert is_valid_delete_ip_pool_from_sda_virtual_network(
            validator,
            delete_ip_pool_from_sda_virtual_network_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_fabric(json_schema_validate, obj):
    json_schema_validate('jsd_6db9292d4f28a26b_v1_3_3').validate(obj)
    return True


def add_fabric(api):
    endpoint_result = api.sda.add_fabric(
        active_validation=True,
        payload=[{'fabricName': 'string'}]
    )
    return endpoint_result


@pytest.mark.sda
def test_add_fabric(api, validator):
    assert is_valid_add_fabric(
        validator,
        add_fabric(api)
    )


def add_fabric_default(api):
    endpoint_result = api.sda.add_fabric(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_fabric_default(api, validator):
    try:
        assert is_valid_add_fabric(
            validator,
            add_fabric_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_edge_device(json_schema_validate, obj):
    json_schema_validate('jsd_87a8ba444ce9bc59_v1_3_3').validate(obj)
    return True


def add_edge_device(api):
    endpoint_result = api.sda.add_edge_device(
        active_validation=True,
        payload=[{'deviceManagementIpAddress': 'string', 'siteNameHierarchy': 'string'}]
    )
    return endpoint_result


@pytest.mark.sda
def test_add_edge_device(api, validator):
    assert is_valid_add_edge_device(
        validator,
        add_edge_device(api)
    )


def add_edge_device_default(api):
    endpoint_result = api.sda.add_edge_device(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_edge_device_default(api, validator):
    try:
        assert is_valid_add_edge_device(
            validator,
            add_edge_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site(json_schema_validate, obj):
    json_schema_validate('jsd_80b7f8e6406a8701_v1_3_3').validate(obj)
    return True


def get_site(api):
    endpoint_result = api.sda.get_site(
        site_name_hierarchy='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_site(api, validator):
    assert is_valid_get_site(
        validator,
        get_site(api)
    )


def get_site_default(api):
    endpoint_result = api.sda.get_site(
        site_name_hierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_site_default(api, validator):
    try:
        assert is_valid_get_site(
            validator,
            get_site_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_edge_device(json_schema_validate, obj):
    json_schema_validate('jsd_7683f90b4efab090_v1_3_3').validate(obj)
    return True


def get_edge_device(api):
    endpoint_result = api.sda.get_edge_device(
        device_ipaddress='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_edge_device(api, validator):
    assert is_valid_get_edge_device(
        validator,
        get_edge_device(api)
    )


def get_edge_device_default(api):
    endpoint_result = api.sda.get_edge_device(
        device_ipaddress=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_edge_device_default(api, validator):
    try:
        assert is_valid_get_edge_device(
            validator,
            get_edge_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_default_authentication_profile(json_schema_validate, obj):
    json_schema_validate('jsd_8b908a4e4c5a9a23_v1_3_3').validate(obj)
    return True


def get_default_authentication_profile(api):
    endpoint_result = api.sda.get_default_authentication_profile(
        site_name_hierarchy='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_default_authentication_profile(api, validator):
    assert is_valid_get_default_authentication_profile(
        validator,
        get_default_authentication_profile(api)
    )


def get_default_authentication_profile_default(api):
    endpoint_result = api.sda.get_default_authentication_profile(
        site_name_hierarchy=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_default_authentication_profile_default(api, validator):
    try:
        assert is_valid_get_default_authentication_profile(
            validator,
            get_default_authentication_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_port_assignment_for_user_device(json_schema_validate, obj):
    json_schema_validate('jsd_9582ab824ce8b29d_v1_3_3').validate(obj)
    return True


def add_port_assignment_for_user_device(api):
    endpoint_result = api.sda.add_port_assignment_for_user_device(
        active_validation=True,
        payload=[{'siteNameHierarchy': 'string', 'deviceManagementIpAddress': 'string', 'interfaceName': 'string', 'dataIpAddressPoolName': 'string', 'voiceIpAddressPoolName': 'string', 'authenticateTemplateName': 'string'}]
    )
    return endpoint_result


@pytest.mark.sda
def test_add_port_assignment_for_user_device(api, validator):
    assert is_valid_add_port_assignment_for_user_device(
        validator,
        add_port_assignment_for_user_device(api)
    )


def add_port_assignment_for_user_device_default(api):
    endpoint_result = api.sda.add_port_assignment_for_user_device(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_port_assignment_for_user_device_default(api, validator):
    try:
        assert is_valid_add_port_assignment_for_user_device(
            validator,
            add_port_assignment_for_user_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_gets_border_device_detail(json_schema_validate, obj):
    json_schema_validate('jsd_98a39bf4485a9871_v1_3_3').validate(obj)
    return True


def gets_border_device_detail(api):
    endpoint_result = api.sda.gets_border_device_detail(
        device_ipaddress='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_gets_border_device_detail(api, validator):
    assert is_valid_gets_border_device_detail(
        validator,
        gets_border_device_detail(api)
    )


def gets_border_device_detail_default(api):
    endpoint_result = api.sda.gets_border_device_detail(
        device_ipaddress=None
    )
    return endpoint_result


@pytest.mark.sda
def test_gets_border_device_detail_default(api, validator):
    try:
        assert is_valid_gets_border_device_detail(
            validator,
            gets_border_device_detail_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_default_authentication_profile(json_schema_validate, obj):
    json_schema_validate('jsd_8984ea7744d98a54_v1_3_3').validate(obj)
    return True


def update_default_authentication_profile(api):
    endpoint_result = api.sda.update_default_authentication_profile(
        active_validation=True,
        payload=[{'siteNameHierarchy': 'string', 'authenticateTemplateName': 'string'}]
    )
    return endpoint_result


@pytest.mark.sda
def test_update_default_authentication_profile(api, validator):
    assert is_valid_update_default_authentication_profile(
        validator,
        update_default_authentication_profile(api)
    )


def update_default_authentication_profile_default(api):
    endpoint_result = api.sda.update_default_authentication_profile(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_update_default_authentication_profile_default(api, validator):
    try:
        assert is_valid_update_default_authentication_profile(
            validator,
            update_default_authentication_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_control_plane_device(json_schema_validate, obj):
    json_schema_validate('jsd_aba4991d4e9b8747_v1_3_3').validate(obj)
    return True


def get_control_plane_device(api):
    endpoint_result = api.sda.get_control_plane_device(
        device_ipaddress='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_control_plane_device(api, validator):
    assert is_valid_get_control_plane_device(
        validator,
        get_control_plane_device(api)
    )


def get_control_plane_device_default(api):
    endpoint_result = api.sda.get_control_plane_device(
        device_ipaddress=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_control_plane_device_default(api, validator):
    try:
        assert is_valid_get_control_plane_device(
            validator,
            get_control_plane_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_port_assignment_for_user_device(json_schema_validate, obj):
    json_schema_validate('jsd_a4a1e8ed41cb9653_v1_3_3').validate(obj)
    return True


def get_port_assignment_for_user_device(api):
    endpoint_result = api.sda.get_port_assignment_for_user_device(
        device_ip='string',
        interface_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_port_assignment_for_user_device(api, validator):
    assert is_valid_get_port_assignment_for_user_device(
        validator,
        get_port_assignment_for_user_device(api)
    )


def get_port_assignment_for_user_device_default(api):
    endpoint_result = api.sda.get_port_assignment_for_user_device(
        device_ip=None,
        interface_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_port_assignment_for_user_device_default(api, validator):
    try:
        assert is_valid_get_port_assignment_for_user_device(
            validator,
            get_port_assignment_for_user_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_adds_border_device(json_schema_validate, obj):
    json_schema_validate('jsd_bead7b3443b996a7_v1_3_3').validate(obj)
    return True


def adds_border_device(api):
    endpoint_result = api.sda.adds_border_device(
        active_validation=True,
        payload=[{'deviceManagementIpAddress': 'string', 'siteNameHierarchy': 'string', 'externalDomainRoutingProtocolName': 'string', 'externalConnectivityIpPoolName': 'string', 'internalAutonomouSystemNumber': 'string', 'borderSessionType': 'string', 'connectedToInternet': True, 'externalConnectivitySettings': [{'interfaceName': 'string', 'externalAutonomouSystemNumber': 'string', 'l3Handoff': [{'virtualNetwork': {'virtualNetworkName': 'string'}}]}]}]
    )
    return endpoint_result


@pytest.mark.sda
def test_adds_border_device(api, validator):
    assert is_valid_adds_border_device(
        validator,
        adds_border_device(api)
    )


def adds_border_device_default(api):
    endpoint_result = api.sda.adds_border_device(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_adds_border_device_default(api, validator):
    try:
        assert is_valid_adds_border_device(
            validator,
            adds_border_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_vn(json_schema_validate, obj):
    json_schema_validate('jsd_c78c9ad245bb9657_v1_3_3').validate(obj)
    return True


def delete_vn(api):
    endpoint_result = api.sda.delete_vn(
        site_name_hierarchy='string',
        virtual_network_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_vn(api, validator):
    assert is_valid_delete_vn(
        validator,
        delete_vn(api)
    )


def delete_vn_default(api):
    endpoint_result = api.sda.delete_vn(
        site_name_hierarchy=None,
        virtual_network_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_vn_default(api, validator):
    try:
        assert is_valid_delete_vn(
            validator,
            delete_vn_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_port_assignment_for_user_device(json_schema_validate, obj):
    json_schema_validate('jsd_cba5b8b14edb81f4_v1_3_3').validate(obj)
    return True


def delete_port_assignment_for_user_device(api):
    endpoint_result = api.sda.delete_port_assignment_for_user_device(
        device_ip='string',
        interface_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_port_assignment_for_user_device(api, validator):
    assert is_valid_delete_port_assignment_for_user_device(
        validator,
        delete_port_assignment_for_user_device(api)
    )


def delete_port_assignment_for_user_device_default(api):
    endpoint_result = api.sda.delete_port_assignment_for_user_device(
        device_ip=None,
        interface_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_port_assignment_for_user_device_default(api, validator):
    try:
        assert is_valid_delete_port_assignment_for_user_device(
            validator,
            delete_port_assignment_for_user_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_port_assignment_for_access_point(json_schema_validate, obj):
    json_schema_validate('jsd_c2a43ad24098baa7_v1_3_3').validate(obj)
    return True


def add_port_assignment_for_access_point(api):
    endpoint_result = api.sda.add_port_assignment_for_access_point(
        active_validation=True,
        payload=[{'siteNameHierarchy': 'string', 'deviceManagementIpAddress': 'string', 'interfaceName': 'string', 'dataIpAddressPoolName': 'string', 'voiceIpAddressPoolName': 'string', 'authenticateTemplateName': 'string'}]
    )
    return endpoint_result


@pytest.mark.sda
def test_add_port_assignment_for_access_point(api, validator):
    assert is_valid_add_port_assignment_for_access_point(
        validator,
        add_port_assignment_for_access_point(api)
    )


def add_port_assignment_for_access_point_default(api):
    endpoint_result = api.sda.add_port_assignment_for_access_point(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_port_assignment_for_access_point_default(api, validator):
    try:
        assert is_valid_add_port_assignment_for_access_point(
            validator,
            add_port_assignment_for_access_point_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_default_authentication_profile(json_schema_validate, obj):
    json_schema_validate('jsd_bca339d844c8a3c0_v1_3_3').validate(obj)
    return True


def add_default_authentication_profile(api):
    endpoint_result = api.sda.add_default_authentication_profile(
        active_validation=True,
        payload=[{'siteNameHierarchy': 'string', 'authenticateTemplateName': 'string'}]
    )
    return endpoint_result


@pytest.mark.sda
def test_add_default_authentication_profile(api, validator):
    assert is_valid_add_default_authentication_profile(
        validator,
        add_default_authentication_profile(api)
    )


def add_default_authentication_profile_default(api):
    endpoint_result = api.sda.add_default_authentication_profile(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_default_authentication_profile_default(api, validator):
    try:
        assert is_valid_add_default_authentication_profile(
            validator,
            add_default_authentication_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_sda_fabric(json_schema_validate, obj):
    json_schema_validate('jsd_d0aafa694f4b9d7b_v1_3_3').validate(obj)
    return True


def delete_sda_fabric(api):
    endpoint_result = api.sda.delete_sda_fabric(
        fabric_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_sda_fabric(api, validator):
    assert is_valid_delete_sda_fabric(
        validator,
        delete_sda_fabric(api)
    )


def delete_sda_fabric_default(api):
    endpoint_result = api.sda.delete_sda_fabric(
        fabric_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_sda_fabric_default(api, validator):
    try:
        assert is_valid_delete_sda_fabric(
            validator,
            delete_sda_fabric_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deletes_border_device(json_schema_validate, obj):
    json_schema_validate('jsd_cb81b93540baaab0_v1_3_3').validate(obj)
    return True


def deletes_border_device(api):
    endpoint_result = api.sda.deletes_border_device(
        device_ipaddress='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_deletes_border_device(api, validator):
    assert is_valid_deletes_border_device(
        validator,
        deletes_border_device(api)
    )


def deletes_border_device_default(api):
    endpoint_result = api.sda.deletes_border_device(
        device_ipaddress=None
    )
    return endpoint_result


@pytest.mark.sda
def test_deletes_border_device_default(api, validator):
    try:
        assert is_valid_deletes_border_device(
            validator,
            deletes_border_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_control_plane_device(json_schema_validate, obj):
    json_schema_validate('jsd_dd85c91042489a3f_v1_3_3').validate(obj)
    return True


def add_control_plane_device(api):
    endpoint_result = api.sda.add_control_plane_device(
        active_validation=True,
        payload=[{'deviceManagementIpAddress': 'string', 'siteNameHierarchy': 'string'}]
    )
    return endpoint_result


@pytest.mark.sda
def test_add_control_plane_device(api, validator):
    assert is_valid_add_control_plane_device(
        validator,
        add_control_plane_device(api)
    )


def add_control_plane_device_default(api):
    endpoint_result = api.sda.add_control_plane_device(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_control_plane_device_default(api, validator):
    try:
        assert is_valid_add_control_plane_device(
            validator,
            add_control_plane_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_control_plane_device(json_schema_validate, obj):
    json_schema_validate('jsd_f6bd6bf64e6890be_v1_3_3').validate(obj)
    return True


def delete_control_plane_device(api):
    endpoint_result = api.sda.delete_control_plane_device(
        device_ipaddress='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_control_plane_device(api, validator):
    assert is_valid_delete_control_plane_device(
        validator,
        delete_control_plane_device(api)
    )


def delete_control_plane_device_default(api):
    endpoint_result = api.sda.delete_control_plane_device(
        device_ipaddress=None
    )
    return endpoint_result


@pytest.mark.sda
def test_delete_control_plane_device_default(api, validator):
    try:
        assert is_valid_delete_control_plane_device(
            validator,
            delete_control_plane_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_site(json_schema_validate, obj):
    json_schema_validate('jsd_d2b4d9d04a4b884c_v1_3_3').validate(obj)
    return True


def add_site(api):
    endpoint_result = api.sda.add_site(
        active_validation=True,
        payload=[{'fabricName': 'string', 'siteNameHierarchy': 'string'}]
    )
    return endpoint_result


@pytest.mark.sda
def test_add_site(api, validator):
    assert is_valid_add_site(
        validator,
        add_site(api)
    )


def add_site_default(api):
    endpoint_result = api.sda.add_site(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.sda
def test_add_site_default(api, validator):
    try:
        assert is_valid_add_site(
            validator,
            add_site_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_ip_pool_from_sda_virtual_network(json_schema_validate, obj):
    json_schema_validate('jsd_fa9219bf45c8b43b_v1_3_3').validate(obj)
    return True


def get_ip_pool_from_sda_virtual_network(api):
    endpoint_result = api.sda.get_ip_pool_from_sda_virtual_network(
        ip_pool_name='string',
        virtual_network_name='string'
    )
    return endpoint_result


@pytest.mark.sda
def test_get_ip_pool_from_sda_virtual_network(api, validator):
    assert is_valid_get_ip_pool_from_sda_virtual_network(
        validator,
        get_ip_pool_from_sda_virtual_network(api)
    )


def get_ip_pool_from_sda_virtual_network_default(api):
    endpoint_result = api.sda.get_ip_pool_from_sda_virtual_network(
        ip_pool_name=None,
        virtual_network_name=None
    )
    return endpoint_result


@pytest.mark.sda
def test_get_ip_pool_from_sda_virtual_network_default(api, validator):
    try:
        assert is_valid_get_ip_pool_from_sda_virtual_network(
            validator,
            get_ip_pool_from_sda_virtual_network_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
