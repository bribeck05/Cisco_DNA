# -*- coding: utf-8 -*-
"""DNACenterAPI devices API fixtures and tests.

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


def is_valid_get_module_info_by_id(json_schema_validate, obj):
    return True if obj else False


def get_module_info_by_id(api):
    endpoint_result = api.devices.get_module_info_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_module_info_by_id(api, validator):
    assert is_valid_get_module_info_by_id(
        validator,
        get_module_info_by_id(api)
    )


def get_module_info_by_id_default(api):
    endpoint_result = api.devices.get_module_info_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_module_info_by_id_default(api, validator):
    try:
        assert is_valid_get_module_info_by_id(
            validator,
            get_module_info_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_device_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_1c894b5848eab214_v1_3_0').validate(obj)
    return True


def delete_device_by_id(api):
    endpoint_result = api.devices.delete_device_by_id(
        id='string',
        is_force_delete=True
    )
    return endpoint_result


@pytest.mark.devices
def test_delete_device_by_id(api, validator):
    assert is_valid_delete_device_by_id(
        validator,
        delete_device_by_id(api)
    )


def delete_device_by_id_default(api):
    endpoint_result = api.devices.delete_device_by_id(
        id='string',
        is_force_delete=None
    )
    return endpoint_result


@pytest.mark.devices
def test_delete_device_by_id_default(api, validator):
    try:
        assert is_valid_delete_device_by_id(
            validator,
            delete_device_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_sync_devices_using_forcesync(json_schema_validate, obj):
    json_schema_validate('jsd_3b9ef9674429be4c_v1_3_0').validate(obj)
    return True


def sync_devices_using_forcesync(api):
    endpoint_result = api.devices.sync_devices_using_forcesync(
        active_validation=True,
        force_sync=True,
        payload=[{}]
    )
    return endpoint_result


@pytest.mark.devices
def test_sync_devices_using_forcesync(api, validator):
    assert is_valid_sync_devices_using_forcesync(
        validator,
        sync_devices_using_forcesync(api)
    )


def sync_devices_using_forcesync_default(api):
    endpoint_result = api.devices.sync_devices_using_forcesync(
        active_validation=True,
        force_sync=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_sync_devices_using_forcesync_default(api, validator):
    try:
        assert is_valid_sync_devices_using_forcesync(
            validator,
            sync_devices_using_forcesync_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_list(json_schema_validate, obj):
    json_schema_validate('jsd_20b19b52464b8972_v1_3_0').validate(obj)
    return True


def get_device_list(api):
    endpoint_result = api.devices.get_device_list(
        associated_wlc_ip='value1,value2',
        collection_interval='value1,value2',
        collection_status='value1,value2',
        error_code='value1,value2',
        error_description='value1,value2',
        family='value1,value2',
        hostname='value1,value2',
        id='string',
        license_name='value1,value2',
        license_status='value1,value2',
        license_type='value1,value2',
        location='value1,value2',
        location_name='value1,value2',
        mac_address='value1,value2',
        management_ip_address='value1,value2',
        module_equpimenttype='value1,value2',
        module_name='value1,value2',
        module_operationstatecode='value1,value2',
        module_partnumber='value1,value2',
        module_servicestate='value1,value2',
        module_vendorequipmenttype='value1,value2',
        not_synced_for_minutes='value1,value2',
        platform_id='value1,value2',
        reachability_status='value1,value2',
        role='value1,value2',
        serial_number='value1,value2',
        series='value1,value2',
        software_type='value1,value2',
        software_version='value1,value2',
        type='value1,value2',
        up_time='value1,value2'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_list(api, validator):
    assert is_valid_get_device_list(
        validator,
        get_device_list(api)
    )


def get_device_list_default(api):
    endpoint_result = api.devices.get_device_list(
        associated_wlc_ip=None,
        collection_interval=None,
        collection_status=None,
        error_code=None,
        error_description=None,
        family=None,
        hostname=None,
        id=None,
        license_name=None,
        license_status=None,
        license_type=None,
        location=None,
        location_name=None,
        mac_address=None,
        management_ip_address=None,
        module_equpimenttype=None,
        module_name=None,
        module_operationstatecode=None,
        module_partnumber=None,
        module_servicestate=None,
        module_vendorequipmenttype=None,
        not_synced_for_minutes=None,
        platform_id=None,
        reachability_status=None,
        role=None,
        serial_number=None,
        series=None,
        software_type=None,
        software_version=None,
        type=None,
        up_time=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_list_default(api, validator):
    try:
        assert is_valid_get_device_list(
            validator,
            get_device_list_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_interface_vlans(json_schema_validate, obj):
    json_schema_validate('jsd_288df9494f2a9746_v1_3_0').validate(obj)
    return True


def get_device_interface_vlans(api):
    endpoint_result = api.devices.get_device_interface_vlans(
        id='string',
        interface_type='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interface_vlans(api, validator):
    assert is_valid_get_device_interface_vlans(
        validator,
        get_device_interface_vlans(api)
    )


def get_device_interface_vlans_default(api):
    endpoint_result = api.devices.get_device_interface_vlans(
        id='string',
        interface_type=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interface_vlans_default(api, validator):
    try:
        assert is_valid_get_device_interface_vlans(
            validator,
            get_device_interface_vlans_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_polling_interval_for_all_devices(json_schema_validate, obj):
    return True if obj else False


def get_polling_interval_for_all_devices(api):
    endpoint_result = api.devices.get_polling_interval_for_all_devices(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_polling_interval_for_all_devices(api, validator):
    assert is_valid_get_polling_interval_for_all_devices(
        validator,
        get_polling_interval_for_all_devices(api)
    )


def get_polling_interval_for_all_devices_default(api):
    endpoint_result = api.devices.get_polling_interval_for_all_devices(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_polling_interval_for_all_devices_default(api, validator):
    try:
        assert is_valid_get_polling_interval_for_all_devices(
            validator,
            get_polling_interval_for_all_devices_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_interfaces_by_specified_range(json_schema_validate, obj):
    json_schema_validate('jsd_349c888443b89a58_v1_3_0').validate(obj)
    return True


def get_device_interfaces_by_specified_range(api):
    endpoint_result = api.devices.get_device_interfaces_by_specified_range(
        device_id='string',
        records_to_return=0,
        start_index=0
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interfaces_by_specified_range(api, validator):
    assert is_valid_get_device_interfaces_by_specified_range(
        validator,
        get_device_interfaces_by_specified_range(api)
    )


def get_device_interfaces_by_specified_range_default(api):
    endpoint_result = api.devices.get_device_interfaces_by_specified_range(
        device_id='string',
        records_to_return=0,
        start_index=0
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interfaces_by_specified_range_default(api, validator):
    try:
        assert is_valid_get_device_interfaces_by_specified_range(
            validator,
            get_device_interfaces_by_specified_range_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_interface_count(json_schema_validate, obj):
    json_schema_validate('jsd_3d923b184dc9a4ca_v1_3_0').validate(obj)
    return True


def get_device_interface_count(api):
    endpoint_result = api.devices.get_device_interface_count(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interface_count(api, validator):
    assert is_valid_get_device_interface_count(
        validator,
        get_device_interface_count(api)
    )


def get_device_interface_count_default(api):
    endpoint_result = api.devices.get_device_interface_count(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interface_count_default(api, validator):
    try:
        assert is_valid_get_device_interface_count(
            validator,
            get_device_interface_count_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_add_device(json_schema_validate, obj):
    json_schema_validate('jsd_4bb22af046fa8f08_v1_3_0').validate(obj)
    return True


def add_device(api):
    endpoint_result = api.devices.add_device(
        active_validation=True,
        cliTransport='string',
        computeDevice=True,
        enablePassword='string',
        extendedDiscoveryInfo='string',
        httpPassword='string',
        httpPort='string',
        httpSecure=True,
        httpUserName='string',
        ipAddress=['string'],
        merakiOrgId=['string'],
        netconfPort='string',
        password='string',
        payload=None,
        serialNumber='string',
        snmpAuthPassphrase='string',
        snmpAuthProtocol='string',
        snmpMode='string',
        snmpPrivPassphrase='string',
        snmpPrivProtocol='string',
        snmpROCommunity='string',
        snmpRWCommunity='string',
        snmpRetry=0,
        snmpTimeout=0,
        snmpUserName='string',
        snmpVersion='string',
        type='COMPUTE_DEVICE',
        updateMgmtIPaddressList=[{'existMgmtIpAddress': 'string', 'newMgmtIpAddress': 'string'}],
        userName='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_add_device(api, validator):
    assert is_valid_add_device(
        validator,
        add_device(api)
    )


def add_device_default(api):
    endpoint_result = api.devices.add_device(
        active_validation=True,
        cliTransport=None,
        computeDevice=None,
        enablePassword=None,
        extendedDiscoveryInfo=None,
        httpPassword=None,
        httpPort=None,
        httpSecure=None,
        httpUserName=None,
        ipAddress=None,
        merakiOrgId=None,
        netconfPort=None,
        password=None,
        payload=None,
        serialNumber=None,
        snmpAuthPassphrase=None,
        snmpAuthProtocol=None,
        snmpMode=None,
        snmpPrivPassphrase=None,
        snmpPrivProtocol=None,
        snmpROCommunity=None,
        snmpRWCommunity=None,
        snmpRetry=None,
        snmpTimeout=None,
        snmpUserName=None,
        snmpVersion=None,
        type=None,
        updateMgmtIPaddressList=None,
        userName=None
    )
    return endpoint_result


@pytest.mark.devices
def test_add_device_default(api, validator):
    try:
        assert is_valid_add_device(
            validator,
            add_device_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_interface_details(json_schema_validate, obj):
    json_schema_validate('jsd_4eb56a614cc9a2d2_v1_3_0').validate(obj)
    return True


def get_interface_details(api):
    endpoint_result = api.devices.get_interface_details(
        device_id='string',
        name='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_interface_details(api, validator):
    assert is_valid_get_interface_details(
        validator,
        get_interface_details(api)
    )


def get_interface_details_default(api):
    endpoint_result = api.devices.get_interface_details(
        device_id='string',
        name=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_interface_details_default(api, validator):
    try:
        assert is_valid_get_interface_details(
            validator,
            get_interface_details_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_interface_count_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_5b8639224cd88ea7_v1_3_0').validate(obj)
    return True


def get_device_interface_count_by_id(api):
    endpoint_result = api.devices.get_device_interface_count_by_id(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interface_count_by_id(api, validator):
    assert is_valid_get_device_interface_count_by_id(
        validator,
        get_device_interface_count_by_id(api)
    )


def get_device_interface_count_by_id_default(api):
    endpoint_result = api.devices.get_device_interface_count_by_id(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_interface_count_by_id_default(api, validator):
    try:
        assert is_valid_get_device_interface_count_by_id(
            validator,
            get_device_interface_count_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_count(json_schema_validate, obj):
    return True if obj else False


def get_device_count(api):
    endpoint_result = api.devices.get_device_count(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_count(api, validator):
    assert is_valid_get_device_count(
        validator,
        get_device_count(api)
    )


def get_device_count_default(api):
    endpoint_result = api.devices.get_device_count(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_count_default(api, validator):
    try:
        assert is_valid_get_device_count(
            validator,
            get_device_count_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_ospf_interfaces(json_schema_validate, obj):
    json_schema_validate('jsd_70ad397649e9b4d3_v1_3_0').validate(obj)
    return True


def get_ospf_interfaces(api):
    endpoint_result = api.devices.get_ospf_interfaces(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_ospf_interfaces(api, validator):
    assert is_valid_get_ospf_interfaces(
        validator,
        get_ospf_interfaces(api)
    )


def get_ospf_interfaces_default(api):
    endpoint_result = api.devices.get_ospf_interfaces(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_ospf_interfaces_default(api, validator):
    try:
        assert is_valid_get_ospf_interfaces(
            validator,
            get_ospf_interfaces_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_polling_interval_by_id(json_schema_validate, obj):
    return True if obj else False


def get_polling_interval_by_id(api):
    endpoint_result = api.devices.get_polling_interval_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_polling_interval_by_id(api, validator):
    assert is_valid_get_polling_interval_by_id(
        validator,
        get_polling_interval_by_id(api)
    )


def get_polling_interval_by_id_default(api):
    endpoint_result = api.devices.get_polling_interval_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_polling_interval_by_id_default(api, validator):
    try:
        assert is_valid_get_polling_interval_by_id(
            validator,
            get_polling_interval_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_organization_list_for_meraki(json_schema_validate, obj):
    return True if obj else False


def get_organization_list_for_meraki(api):
    endpoint_result = api.devices.get_organization_list_for_meraki(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_organization_list_for_meraki(api, validator):
    assert is_valid_get_organization_list_for_meraki(
        validator,
        get_organization_list_for_meraki(api)
    )


def get_organization_list_for_meraki_default(api):
    endpoint_result = api.devices.get_organization_list_for_meraki(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_organization_list_for_meraki_default(api, validator):
    try:
        assert is_valid_get_organization_list_for_meraki(
            validator,
            get_organization_list_for_meraki_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_functional_capability_by_id(json_schema_validate, obj):
    return True if obj else False


def get_functional_capability_by_id(api):
    endpoint_result = api.devices.get_functional_capability_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_functional_capability_by_id(api, validator):
    assert is_valid_get_functional_capability_by_id(
        validator,
        get_functional_capability_by_id(api)
    )


def get_functional_capability_by_id_default(api):
    endpoint_result = api.devices.get_functional_capability_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_functional_capability_by_id_default(api, validator):
    try:
        assert is_valid_get_functional_capability_by_id(
            validator,
            get_functional_capability_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_isis_interfaces(json_schema_validate, obj):
    json_schema_validate('jsd_84ad8b0e42cab48a_v1_3_0').validate(obj)
    return True


def get_isis_interfaces(api):
    endpoint_result = api.devices.get_isis_interfaces(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_isis_interfaces(api, validator):
    assert is_valid_get_isis_interfaces(
        validator,
        get_isis_interfaces(api)
    )


def get_isis_interfaces_default(api):
    endpoint_result = api.devices.get_isis_interfaces(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_isis_interfaces_default(api, validator):
    try:
        assert is_valid_get_isis_interfaces(
            validator,
            get_isis_interfaces_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_config_by_id(json_schema_validate, obj):
    return True if obj else False


def get_device_config_by_id(api):
    endpoint_result = api.devices.get_device_config_by_id(
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_config_by_id(api, validator):
    assert is_valid_get_device_config_by_id(
        validator,
        get_device_config_by_id(api)
    )


def get_device_config_by_id_default(api):
    endpoint_result = api.devices.get_device_config_by_id(
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_config_by_id_default(api, validator):
    try:
        assert is_valid_get_device_config_by_id(
            validator,
            get_device_config_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_summary(json_schema_validate, obj):
    return True if obj else False


def get_device_summary(api):
    endpoint_result = api.devices.get_device_summary(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_summary(api, validator):
    assert is_valid_get_device_summary(
        validator,
        get_device_summary(api)
    )


def get_device_summary_default(api):
    endpoint_result = api.devices.get_device_summary(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_summary_default(api, validator):
    try:
        assert is_valid_get_device_summary(
            validator,
            get_device_summary_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_by_id(json_schema_validate, obj):
    return True if obj else False


def get_device_by_id(api):
    endpoint_result = api.devices.get_device_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_by_id(api, validator):
    assert is_valid_get_device_by_id(
        validator,
        get_device_by_id(api)
    )


def get_device_by_id_default(api):
    endpoint_result = api.devices.get_device_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_by_id_default(api, validator):
    try:
        assert is_valid_get_device_by_id(
            validator,
            get_device_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_interface_info_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_ba9dc85b4b8a9a17_v1_3_0').validate(obj)
    return True


def get_interface_info_by_id(api):
    endpoint_result = api.devices.get_interface_info_by_id(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_interface_info_by_id(api, validator):
    assert is_valid_get_interface_info_by_id(
        validator,
        get_interface_info_by_id(api)
    )


def get_interface_info_by_id_default(api):
    endpoint_result = api.devices.get_interface_info_by_id(
        device_id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_interface_info_by_id_default(api, validator):
    try:
        assert is_valid_get_interface_info_by_id(
            validator,
            get_interface_info_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_register_device_for_wsa(json_schema_validate, obj):
    return True if obj else False


def register_device_for_wsa(api):
    endpoint_result = api.devices.register_device_for_wsa(
        macaddress='string',
        serial_number='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_register_device_for_wsa(api, validator):
    assert is_valid_register_device_for_wsa(
        validator,
        register_device_for_wsa(api)
    )


def register_device_for_wsa_default(api):
    endpoint_result = api.devices.register_device_for_wsa(
        macaddress=None,
        serial_number=None
    )
    return endpoint_result


@pytest.mark.devices
def test_register_device_for_wsa_default(api, validator):
    try:
        assert is_valid_register_device_for_wsa(
            validator,
            register_device_for_wsa_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_device_role(json_schema_validate, obj):
    json_schema_validate('jsd_b9855ad54ae98156_v1_3_0').validate(obj)
    return True


def update_device_role(api):
    endpoint_result = api.devices.update_device_role(
        active_validation=True,
        id='string',
        payload=None,
        role='string',
        roleSource='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_update_device_role(api, validator):
    assert is_valid_update_device_role(
        validator,
        update_device_role(api)
    )


def update_device_role_default(api):
    endpoint_result = api.devices.update_device_role(
        active_validation=True,
        id=None,
        payload=None,
        role=None,
        roleSource=None
    )
    return endpoint_result


@pytest.mark.devices
def test_update_device_role_default(api, validator):
    try:
        assert is_valid_update_device_role(
            validator,
            update_device_role_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_config_for_all_devices(json_schema_validate, obj):
    return True if obj else False


def get_device_config_for_all_devices(api):
    endpoint_result = api.devices.get_device_config_for_all_devices(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_config_for_all_devices(api, validator):
    assert is_valid_get_device_config_for_all_devices(
        validator,
        get_device_config_for_all_devices(api)
    )


def get_device_config_for_all_devices_default(api):
    endpoint_result = api.devices.get_device_config_for_all_devices(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_config_for_all_devices_default(api, validator):
    try:
        assert is_valid_get_device_config_for_all_devices(
            validator,
            get_device_config_for_all_devices_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_export_device_list(json_schema_validate, obj):
    json_schema_validate('jsd_cd98780f4888a66d_v1_3_0').validate(obj)
    return True


def export_device_list(api):
    endpoint_result = api.devices.export_device_list(
        active_validation=True,
        deviceUuids=['string'],
        id='string',
        operationEnum='CREDENTIALDETAILS',
        parameters=['string'],
        password='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_export_device_list(api, validator):
    assert is_valid_export_device_list(
        validator,
        export_device_list(api)
    )


def export_device_list_default(api):
    endpoint_result = api.devices.export_device_list(
        active_validation=True,
        deviceUuids=None,
        id=None,
        operationEnum=None,
        parameters=None,
        password=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.devices
def test_export_device_list_default(api, validator):
    try:
        assert is_valid_export_device_list(
            validator,
            export_device_list_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_interface_by_ip(json_schema_validate, obj):
    json_schema_validate('jsd_cd8469e647caab0e_v1_3_0').validate(obj)
    return True


def get_interface_by_ip(api):
    endpoint_result = api.devices.get_interface_by_ip(
        ip_address='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_interface_by_ip(api, validator):
    assert is_valid_get_interface_by_ip(
        validator,
        get_interface_by_ip(api)
    )


def get_interface_by_ip_default(api):
    endpoint_result = api.devices.get_interface_by_ip(
        ip_address='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_interface_by_ip_default(api, validator):
    try:
        assert is_valid_get_interface_by_ip(
            validator,
            get_interface_by_ip_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_device_by_ip(json_schema_validate, obj):
    return True if obj else False


def get_network_device_by_ip(api):
    endpoint_result = api.devices.get_network_device_by_ip(
        ip_address='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_network_device_by_ip(api, validator):
    assert is_valid_get_network_device_by_ip(
        validator,
        get_network_device_by_ip(api)
    )


def get_network_device_by_ip_default(api):
    endpoint_result = api.devices.get_network_device_by_ip(
        ip_address='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_network_device_by_ip_default(api, validator):
    try:
        assert is_valid_get_network_device_by_ip(
            validator,
            get_network_device_by_ip_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_config_count(json_schema_validate, obj):
    return True if obj else False


def get_device_config_count(api):
    endpoint_result = api.devices.get_device_config_count(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_config_count(api, validator):
    assert is_valid_get_device_config_count(
        validator,
        get_device_config_count(api)
    )


def get_device_config_count_default(api):
    endpoint_result = api.devices.get_device_config_count(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_config_count_default(api, validator):
    try:
        assert is_valid_get_device_config_count(
            validator,
            get_device_config_count_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_by_serial_number(json_schema_validate, obj):
    return True if obj else False


def get_device_by_serial_number(api):
    endpoint_result = api.devices.get_device_by_serial_number(
        serial_number='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_by_serial_number(api, validator):
    assert is_valid_get_device_by_serial_number(
        validator,
        get_device_by_serial_number(api)
    )


def get_device_by_serial_number_default(api):
    endpoint_result = api.devices.get_device_by_serial_number(
        serial_number='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_by_serial_number_default(api, validator):
    try:
        assert is_valid_get_device_by_serial_number(
            validator,
            get_device_by_serial_number_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_all_interfaces(json_schema_validate, obj):
    json_schema_validate('jsd_f5947a4c439a8bf0_v1_3_0').validate(obj)
    return True


def get_all_interfaces(api):
    endpoint_result = api.devices.get_all_interfaces(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_all_interfaces(api, validator):
    assert is_valid_get_all_interfaces(
        validator,
        get_all_interfaces(api)
    )


def get_all_interfaces_default(api):
    endpoint_result = api.devices.get_all_interfaces(

    )
    return endpoint_result


@pytest.mark.devices
def test_get_all_interfaces_default(api, validator):
    try:
        assert is_valid_get_all_interfaces(
            validator,
            get_all_interfaces_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_module_count(json_schema_validate, obj):
    return True if obj else False


def get_module_count(api):
    endpoint_result = api.devices.get_module_count(
        device_id='string',
        name_list='value1,value2',
        operational_state_code_list='value1,value2',
        part_number_list='value1,value2',
        vendor_equipment_type_list='value1,value2'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_module_count(api, validator):
    assert is_valid_get_module_count(
        validator,
        get_module_count(api)
    )


def get_module_count_default(api):
    endpoint_result = api.devices.get_module_count(
        device_id=None,
        name_list=None,
        operational_state_code_list=None,
        part_number_list=None,
        vendor_equipment_type_list=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_module_count_default(api, validator):
    try:
        assert is_valid_get_module_count(
            validator,
            get_module_count_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_modules(json_schema_validate, obj):
    json_schema_validate('jsd_eb8249e34f69b0f1_v1_3_0').validate(obj)
    return True


def get_modules(api):
    endpoint_result = api.devices.get_modules(
        device_id='string',
        limit='string',
        name_list='value1,value2',
        offset='string',
        operational_state_code_list='value1,value2',
        part_number_list='value1,value2',
        vendor_equipment_type_list='value1,value2'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_modules(api, validator):
    assert is_valid_get_modules(
        validator,
        get_modules(api)
    )


def get_modules_default(api):
    endpoint_result = api.devices.get_modules(
        device_id=None,
        limit=None,
        name_list=None,
        offset=None,
        operational_state_code_list=None,
        part_number_list=None,
        vendor_equipment_type_list=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_modules_default(api, validator):
    try:
        assert is_valid_get_modules(
            validator,
            get_modules_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_wireless_lan_controller_details_by_id(json_schema_validate, obj):
    return True if obj else False


def get_wireless_lan_controller_details_by_id(api):
    endpoint_result = api.devices.get_wireless_lan_controller_details_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_wireless_lan_controller_details_by_id(api, validator):
    assert is_valid_get_wireless_lan_controller_details_by_id(
        validator,
        get_wireless_lan_controller_details_by_id(api)
    )


def get_wireless_lan_controller_details_by_id_default(api):
    endpoint_result = api.devices.get_wireless_lan_controller_details_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_wireless_lan_controller_details_by_id_default(api, validator):
    try:
        assert is_valid_get_wireless_lan_controller_details_by_id(
            validator,
            get_wireless_lan_controller_details_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_sync_devices(json_schema_validate, obj):
    json_schema_validate('jsd_aeb9eb67460b92df_v1_3_0').validate(obj)
    return True


def sync_devices(api):
    endpoint_result = api.devices.sync_devices(
        active_validation=True,
        cliTransport='string',
        computeDevice=True,
        enablePassword='string',
        extendedDiscoveryInfo='string',
        httpPassword='string',
        httpPort='string',
        httpSecure=True,
        httpUserName='string',
        ipAddress=['string'],
        merakiOrgId=['string'],
        netconfPort='string',
        password='string',
        payload=None,
        serialNumber='string',
        snmpAuthPassphrase='string',
        snmpAuthProtocol='string',
        snmpMode='string',
        snmpPrivPassphrase='string',
        snmpPrivProtocol='string',
        snmpROCommunity='string',
        snmpRWCommunity='string',
        snmpRetry=0,
        snmpTimeout=0,
        snmpUserName='string',
        snmpVersion='string',
        type='COMPUTE_DEVICE',
        updateMgmtIPaddressList=[{'existMgmtIpAddress': 'string', 'newMgmtIpAddress': 'string'}],
        userName='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_sync_devices(api, validator):
    assert is_valid_sync_devices(
        validator,
        sync_devices(api)
    )


def sync_devices_default(api):
    endpoint_result = api.devices.sync_devices(
        active_validation=True,
        cliTransport=None,
        computeDevice=None,
        enablePassword=None,
        extendedDiscoveryInfo=None,
        httpPassword=None,
        httpPort=None,
        httpSecure=None,
        httpUserName=None,
        ipAddress=None,
        merakiOrgId=None,
        netconfPort=None,
        password=None,
        payload=None,
        serialNumber=None,
        snmpAuthPassphrase=None,
        snmpAuthProtocol=None,
        snmpMode=None,
        snmpPrivPassphrase=None,
        snmpPrivProtocol=None,
        snmpROCommunity=None,
        snmpRWCommunity=None,
        snmpRetry=None,
        snmpTimeout=None,
        snmpUserName=None,
        snmpVersion=None,
        type=None,
        updateMgmtIPaddressList=None,
        userName=None
    )
    return endpoint_result


@pytest.mark.devices
def test_sync_devices_default(api, validator):
    try:
        assert is_valid_sync_devices(
            validator,
            sync_devices_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_interface_by_id(json_schema_validate, obj):
    return True if obj else False


def get_interface_by_id(api):
    endpoint_result = api.devices.get_interface_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_interface_by_id(api, validator):
    assert is_valid_get_interface_by_id(
        validator,
        get_interface_by_id(api)
    )


def get_interface_by_id_default(api):
    endpoint_result = api.devices.get_interface_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_interface_by_id_default(api, validator):
    try:
        assert is_valid_get_interface_by_id(
            validator,
            get_interface_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_functional_capability_for_devices(json_schema_validate, obj):
    json_schema_validate('jsd_c3b3c9ef4e6b8a09_v1_3_0').validate(obj)
    return True


def get_functional_capability_for_devices(api):
    endpoint_result = api.devices.get_functional_capability_for_devices(
        device_id='string',
        function_name='value1,value2'
    )
    return endpoint_result


@pytest.mark.devices
def test_get_functional_capability_for_devices(api, validator):
    assert is_valid_get_functional_capability_for_devices(
        validator,
        get_functional_capability_for_devices(api)
    )


def get_functional_capability_for_devices_default(api):
    endpoint_result = api.devices.get_functional_capability_for_devices(
        device_id=None,
        function_name=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_functional_capability_for_devices_default(api, validator):
    try:
        assert is_valid_get_functional_capability_for_devices(
            validator,
            get_functional_capability_for_devices_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_detail(json_schema_validate, obj):
    json_schema_validate('jsd_89b2fb144f5bb09b_v1_3_0').validate(obj)
    return True


def get_device_detail(api):
    endpoint_result = api.devices.get_device_detail(
        identifier='string',
        search_by='string',
        timestamp=0
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_detail(api, validator):
    assert is_valid_get_device_detail(
        validator,
        get_device_detail(api)
    )


def get_device_detail_default(api):
    endpoint_result = api.devices.get_device_detail(
        identifier=None,
        search_by=None,
        timestamp=None
    )
    return endpoint_result


@pytest.mark.devices
def test_get_device_detail_default(api, validator):
    try:
        assert is_valid_get_device_detail(
            validator,
            get_device_detail_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_device_by_pagination_range(json_schema_validate, obj):
    json_schema_validate('jsd_f49548c54be8a3e2_v1_3_0').validate(obj)
    return True


def get_network_device_by_pagination_range(api):
    endpoint_result = api.devices.get_network_device_by_pagination_range(
        records_to_return=0,
        start_index=0
    )
    return endpoint_result


@pytest.mark.devices
def test_get_network_device_by_pagination_range(api, validator):
    assert is_valid_get_network_device_by_pagination_range(
        validator,
        get_network_device_by_pagination_range(api)
    )


def get_network_device_by_pagination_range_default(api):
    endpoint_result = api.devices.get_network_device_by_pagination_range(
        records_to_return=0,
        start_index=0
    )
    return endpoint_result


@pytest.mark.devices
def test_get_network_device_by_pagination_range_default(api, validator):
    try:
        assert is_valid_get_network_device_by_pagination_range(
            validator,
            get_network_device_by_pagination_range_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_retrieves_all_network_devices(json_schema_validate, obj):
    json_schema_validate('jsd_ffa748cc44e9a437_v1_3_0').validate(obj)
    return True


def retrieves_all_network_devices(api):
    endpoint_result = api.devices.retrieves_all_network_devices(
        associated_wlc_ip='string',
        collection_interval='string',
        collection_status='string',
        error_code='string',
        family='string',
        hostname='string',
        limit='string',
        mac_address='string',
        management_ip_address='string',
        offset='string',
        platform_id='string',
        reachability_failure_reason='string',
        reachability_status='string',
        role='string',
        role_source='string',
        serial_number='string',
        series='string',
        software_type='string',
        software_version='string',
        type='string',
        up_time='string',
        vrf_name='string'
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_all_network_devices(api, validator):
    assert is_valid_retrieves_all_network_devices(
        validator,
        retrieves_all_network_devices(api)
    )


def retrieves_all_network_devices_default(api):
    endpoint_result = api.devices.retrieves_all_network_devices(
        associated_wlc_ip=None,
        collection_interval=None,
        collection_status=None,
        error_code=None,
        family=None,
        hostname=None,
        limit=None,
        mac_address=None,
        management_ip_address=None,
        offset=None,
        platform_id=None,
        reachability_failure_reason=None,
        reachability_status=None,
        role=None,
        role_source=None,
        serial_number=None,
        series=None,
        software_type=None,
        software_version=None,
        type=None,
        up_time=None,
        vrf_name=None
    )
    return endpoint_result


@pytest.mark.devices
def test_retrieves_all_network_devices_default(api, validator):
    try:
        assert is_valid_retrieves_all_network_devices(
            validator,
            retrieves_all_network_devices_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
