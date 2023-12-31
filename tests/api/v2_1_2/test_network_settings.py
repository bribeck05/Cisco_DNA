# -*- coding: utf-8 -*-
"""DNACenterAPI network_settings API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.1.2', reason='version does not match')


def is_valid_update_global_pool(json_schema_validate, obj):
    json_schema_validate('jsd_03b4c8b44919b964_v2_1_2').validate(obj)
    return True


def update_global_pool(api):
    endpoint_result = api.network_settings.update_global_pool(
        active_validation=True,
        payload=None,
        settings={'ippool': [{'ipPoolName': 'string', 'gateway': 'string', 'dhcpServerIps': ['string'], 'dnsServerIps': ['string'], 'id': 'string'}]}
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_global_pool(api, validator):
    assert is_valid_update_global_pool(
        validator,
        update_global_pool(api)
    )


def update_global_pool_default(api):
    endpoint_result = api.network_settings.update_global_pool(
        active_validation=True,
        payload=None,
        settings=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_global_pool_default(api, validator):
    try:
        assert is_valid_update_global_pool(
            validator,
            update_global_pool_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_global_ip_pool(json_schema_validate, obj):
    json_schema_validate('jsd_1eaa8b2148ab81de_v2_1_2').validate(obj)
    return True


def delete_global_ip_pool(api):
    endpoint_result = api.network_settings.delete_global_ip_pool(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_delete_global_ip_pool(api, validator):
    assert is_valid_delete_global_ip_pool(
        validator,
        delete_global_ip_pool(api)
    )


def delete_global_ip_pool_default(api):
    endpoint_result = api.network_settings.delete_global_ip_pool(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_delete_global_ip_pool_default(api, validator):
    try:
        assert is_valid_delete_global_ip_pool(
            validator,
            delete_global_ip_pool_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_device_credential(json_schema_validate, obj):
    json_schema_validate('jsd_259eab3045988958_v2_1_2').validate(obj)
    return True


def delete_device_credential(api):
    endpoint_result = api.network_settings.delete_device_credential(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_delete_device_credential(api, validator):
    assert is_valid_delete_device_credential(
        validator,
        delete_device_credential(api)
    )


def delete_device_credential_default(api):
    endpoint_result = api.network_settings.delete_device_credential(
        id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_delete_device_credential_default(api, validator):
    try:
        assert is_valid_delete_device_credential(
            validator,
            delete_device_credential_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network(json_schema_validate, obj):
    json_schema_validate('jsd_38b7eb13449b9471_v2_1_2').validate(obj)
    return True


def get_network(api):
    endpoint_result = api.network_settings.get_network(
        site_id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_network(api, validator):
    assert is_valid_get_network(
        validator,
        get_network(api)
    )


def get_network_default(api):
    endpoint_result = api.network_settings.get_network(
        site_id=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_network_default(api, validator):
    try:
        assert is_valid_get_network(
            validator,
            get_network_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_sp_profile(json_schema_validate, obj):
    json_schema_validate('jsd_4ca2db1143ebb5d7_v2_1_2').validate(obj)
    return True


def delete_sp_profile(api):
    endpoint_result = api.network_settings.delete_sp_profile(
        sp_profile_name='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_delete_sp_profile(api, validator):
    assert is_valid_delete_sp_profile(
        validator,
        delete_sp_profile(api)
    )


def delete_sp_profile_default(api):
    endpoint_result = api.network_settings.delete_sp_profile(
        sp_profile_name='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_delete_sp_profile_default(api, validator):
    try:
        assert is_valid_delete_sp_profile(
            validator,
            delete_sp_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_sp_profile(json_schema_validate, obj):
    json_schema_validate('jsd_5087daae4cc98566_v2_1_2').validate(obj)
    return True


def update_sp_profile(api):
    endpoint_result = api.network_settings.update_sp_profile(
        active_validation=True,
        payload=None,
        settings={'qos': [{'profileName': 'string', 'model': 'string', 'wanProvider': 'string', 'oldProfileName': 'string'}]}
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_sp_profile(api, validator):
    assert is_valid_update_sp_profile(
        validator,
        update_sp_profile(api)
    )


def update_sp_profile_default(api):
    endpoint_result = api.network_settings.update_sp_profile(
        active_validation=True,
        payload=None,
        settings=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_sp_profile_default(api, validator):
    try:
        assert is_valid_update_sp_profile(
            validator,
            update_sp_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_service_provider_details(json_schema_validate, obj):
    json_schema_validate('jsd_70847bdc4d89a437_v2_1_2').validate(obj)
    return True


def get_service_provider_details(api):
    endpoint_result = api.network_settings.get_service_provider_details(

    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_service_provider_details(api, validator):
    assert is_valid_get_service_provider_details(
        validator,
        get_service_provider_details(api)
    )


def get_service_provider_details_default(api):
    endpoint_result = api.network_settings.get_service_provider_details(

    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_service_provider_details_default(api, validator):
    try:
        assert is_valid_get_service_provider_details(
            validator,
            get_service_provider_details_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_device_credentials(json_schema_validate, obj):
    json_schema_validate('jsd_4f947a1c4fc884f6_v2_1_2').validate(obj)
    return True


def update_device_credentials(api):
    endpoint_result = api.network_settings.update_device_credentials(
        active_validation=True,
        payload=None,
        settings={'cliCredential': {'description': 'string', 'username': 'string', 'password': 'string', 'enablePassword': 'string', 'id': 'string'}, 'snmpV2cRead': {'description': 'string', 'readCommunity': 'string', 'id': 'string'}, 'snmpV2cWrite': {'description': 'string', 'writeCommunity': 'string', 'id': 'string'}, 'snmpV3': {'authPassword': 'string', 'authType': 'string', 'snmpMode': 'string', 'privacyPassword': 'string', 'privacyType': 'string', 'username': 'string', 'description': 'string', 'id': 'string'}, 'httpsRead': {'name': 'string', 'username': 'string', 'password': 'string', 'port': 'string', 'id': 'string'}, 'httpsWrite': {'name': 'string', 'username': 'string', 'password': 'string', 'port': 'string', 'id': 'string'}}
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_device_credentials(api, validator):
    assert is_valid_update_device_credentials(
        validator,
        update_device_credentials(api)
    )


def update_device_credentials_default(api):
    endpoint_result = api.network_settings.update_device_credentials(
        active_validation=True,
        payload=None,
        settings=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_device_credentials_default(api, validator):
    try:
        assert is_valid_update_device_credentials(
            validator,
            update_device_credentials_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_assign_credential_to_site(json_schema_validate, obj):
    json_schema_validate('jsd_4da91a544e29842d_v2_1_2').validate(obj)
    return True


def assign_credential_to_site(api):
    endpoint_result = api.network_settings.assign_credential_to_site(
        active_validation=True,
        cliId='string',
        httpRead='string',
        httpWrite='string',
        payload=None,
        site_id='string',
        snmpV2ReadId='string',
        snmpV2WriteId='string',
        snmpV3Id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_assign_credential_to_site(api, validator):
    assert is_valid_assign_credential_to_site(
        validator,
        assign_credential_to_site(api)
    )


def assign_credential_to_site_default(api):
    endpoint_result = api.network_settings.assign_credential_to_site(
        active_validation=True,
        cliId=None,
        httpRead=None,
        httpWrite=None,
        payload=None,
        site_id='string',
        snmpV2ReadId=None,
        snmpV2WriteId=None,
        snmpV3Id=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_assign_credential_to_site_default(api, validator):
    try:
        assert is_valid_assign_credential_to_site(
            validator,
            assign_credential_to_site_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_network(json_schema_validate, obj):
    json_schema_validate('jsd_698bfbb44dcb9fca_v2_1_2').validate(obj)
    return True


def update_network(api):
    endpoint_result = api.network_settings.update_network(
        active_validation=True,
        payload=None,
        settings={'dhcpServer': ['string'], 'dnsServer': {'domainName': 'string', 'primaryIpAddress': 'string', 'secondaryIpAddress': 'string'}, 'syslogServer': {'ipAddresses': ['string'], 'configureDnacIP': True}, 'snmpServer': {'ipAddresses': ['string'], 'configureDnacIP': True}, 'netflowcollector': {'ipAddress': 'string', 'port': 0}, 'ntpServer': ['string'], 'timezone': 'string', 'messageOfTheday': {'bannerMessage': 'string', 'retainExistingBanner': True}, 'network_aaa': {'servers': 'string', 'ipAddress': 'string', 'network': 'string', 'protocol': 'string', 'sharedSecret': 'string'}, 'clientAndEndpoint_aaa': {'servers': 'string', 'ipAddress': 'string', 'network': 'string', 'protocol': 'string', 'sharedSecret': 'string'}},
        site_id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_network(api, validator):
    assert is_valid_update_network(
        validator,
        update_network(api)
    )


def update_network_default(api):
    endpoint_result = api.network_settings.update_network(
        active_validation=True,
        payload=None,
        settings=None,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_update_network_default(api, validator):
    try:
        assert is_valid_update_network(
            validator,
            update_network_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_sp_profile(json_schema_validate, obj):
    json_schema_validate('jsd_a39a1a214debb781_v2_1_2').validate(obj)
    return True


def create_sp_profile(api):
    endpoint_result = api.network_settings.create_sp_profile(
        active_validation=True,
        payload=None,
        settings={'qos': [{'profileName': 'string', 'model': 'string', 'wanProvider': 'string'}]}
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_sp_profile(api, validator):
    assert is_valid_create_sp_profile(
        validator,
        create_sp_profile(api)
    )


def create_sp_profile_default(api):
    endpoint_result = api.network_settings.create_sp_profile(
        active_validation=True,
        payload=None,
        settings=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_sp_profile_default(api, validator):
    try:
        assert is_valid_create_sp_profile(
            validator,
            create_sp_profile_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_global_pool(json_schema_validate, obj):
    json_schema_validate('jsd_c0bca85643c8b58d_v2_1_2').validate(obj)
    return True


def get_global_pool(api):
    endpoint_result = api.network_settings.get_global_pool(
        limit='string',
        offset='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_global_pool(api, validator):
    assert is_valid_get_global_pool(
        validator,
        get_global_pool(api)
    )


def get_global_pool_default(api):
    endpoint_result = api.network_settings.get_global_pool(
        limit=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_global_pool_default(api, validator):
    try:
        assert is_valid_get_global_pool(
            validator,
            get_global_pool_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_credential_details(json_schema_validate, obj):
    json_schema_validate('jsd_899f08e7401b82dd_v2_1_2').validate(obj)
    return True


def get_device_credential_details(api):
    endpoint_result = api.network_settings.get_device_credential_details(
        site_id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_device_credential_details(api, validator):
    assert is_valid_get_device_credential_details(
        validator,
        get_device_credential_details(api)
    )


def get_device_credential_details_default(api):
    endpoint_result = api.network_settings.get_device_credential_details(
        site_id=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_get_device_credential_details_default(api, validator):
    try:
        assert is_valid_get_device_credential_details(
            validator,
            get_device_credential_details_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_network(json_schema_validate, obj):
    json_schema_validate('jsd_be892bd84a78865a_v2_1_2').validate(obj)
    return True


def create_network(api):
    endpoint_result = api.network_settings.create_network(
        active_validation=True,
        payload=None,
        settings={'dhcpServer': ['string'], 'dnsServer': {'domainName': 'string', 'primaryIpAddress': 'string', 'secondaryIpAddress': 'string'}, 'syslogServer': {'ipAddresses': ['string'], 'configureDnacIP': True}, 'snmpServer': {'ipAddresses': ['string'], 'configureDnacIP': True}, 'netflowcollector': {'ipAddress': 'string', 'port': 0}, 'ntpServer': ['string'], 'timezone': 'string', 'messageOfTheday': {'bannerMessage': 'string', 'retainExistingBanner': True}, 'network_aaa': {'servers': 'string', 'ipAddress': 'string', 'network': 'string', 'protocol': 'string', 'sharedSecret': 'string'}, 'clientAndEndpoint_aaa': {'servers': 'string', 'ipAddress': 'string', 'network': 'string', 'protocol': 'string', 'sharedSecret': 'string'}},
        site_id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_network(api, validator):
    assert is_valid_create_network(
        validator,
        create_network(api)
    )


def create_network_default(api):
    endpoint_result = api.network_settings.create_network(
        active_validation=True,
        payload=None,
        settings=None,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_network_default(api, validator):
    try:
        assert is_valid_create_network(
            validator,
            create_network_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_device_credentials(json_schema_validate, obj):
    json_schema_validate('jsd_fbb95b37484a9fce_v2_1_2').validate(obj)
    return True


def create_device_credentials(api):
    endpoint_result = api.network_settings.create_device_credentials(
        active_validation=True,
        payload=None,
        settings={'cliCredential': [{'description': 'string', 'username': 'string', 'password': 'string', 'enablePassword': 'string'}], 'snmpV2cRead': [{'description': 'string', 'readCommunity': 'string'}], 'snmpV2cWrite': [{'description': 'string', 'writeCommunity': 'string'}], 'snmpV3': [{'description': 'string', 'username': 'string', 'privacyType': 'AES128', 'privacyPassword': 'string', 'authType': 'SHA', 'authPassword': 'string', 'snmpMode': 'AUTHPRIV'}], 'httpsRead': [{'name': 'string', 'username': 'string', 'password': 'string', 'port': 0}], 'httpsWrite': [{'name': 'string', 'username': 'string', 'password': 'string', 'port': 0}]}
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_device_credentials(api, validator):
    assert is_valid_create_device_credentials(
        validator,
        create_device_credentials(api)
    )


def create_device_credentials_default(api):
    endpoint_result = api.network_settings.create_device_credentials(
        active_validation=True,
        payload=None,
        settings=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_device_credentials_default(api, validator):
    try:
        assert is_valid_create_device_credentials(
            validator,
            create_device_credentials_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_global_pool(json_schema_validate, obj):
    json_schema_validate('jsd_f793192a43dabed9_v2_1_2').validate(obj)
    return True


def create_global_pool(api):
    endpoint_result = api.network_settings.create_global_pool(
        active_validation=True,
        payload=None,
        settings={'ippool': [{'ipPoolName': 'string', 'type': 'Generic', 'ipPoolCidr': 'string', 'gateway': 'string', 'dhcpServerIps': ['string'], 'dnsServerIps': ['string'], 'IpAddressSpace': 'string'}]}
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_global_pool(api, validator):
    assert is_valid_create_global_pool(
        validator,
        create_global_pool(api)
    )


def create_global_pool_default(api):
    endpoint_result = api.network_settings.create_global_pool(
        active_validation=True,
        payload=None,
        settings=None
    )
    return endpoint_result


@pytest.mark.network_settings
def test_create_global_pool_default(api, validator):
    try:
        assert is_valid_create_global_pool(
            validator,
            create_global_pool_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
