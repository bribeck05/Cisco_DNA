# -*- coding: utf-8 -*-
"""DNACenterAPI sites API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.3.1', reason='version does not match')


def is_valid_get_site(json_schema_validate, obj):
    json_schema_validate('jsd_6fb4ab3643faa80f_v1_3_1').validate(obj)
    return True


def get_site(api):
    endpoint_result = api.sites.get_site(
        limit='string',
        name='string',
        offset='string',
        site_id='string',
        type='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site(api, validator):
    assert is_valid_get_site(
        validator,
        get_site(api)
    )


def get_site_default(api):
    endpoint_result = api.sites.get_site(
        limit=None,
        name=None,
        offset=None,
        site_id=None,
        type=None
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_default(api, validator):
    try:
        assert is_valid_get_site(
            validator,
            get_site_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_site(json_schema_validate, obj):
    json_schema_validate('jsd_eeb7eb4b4bd8a1dd_v1_3_1').validate(obj)
    return True


def update_site(api):
    endpoint_result = api.sites.update_site(
        active_validation=True,
        payload=None,
        site={'area': {'name': 'string', 'parentName': 'string'}, 'building': {'name': 'string', 'address': 'string', 'parentName': 'string', 'latitude': 0, 'longitude': 0}, 'floor': {'name': 'string', 'rfModel': 'Cubes And Walled Offices', 'width': 0, 'length': 0, 'height': 0}},
        site_id='string',
        type='area'
    )
    return endpoint_result


@pytest.mark.sites
def test_update_site(api, validator):
    assert is_valid_update_site(
        validator,
        update_site(api)
    )


def update_site_default(api):
    endpoint_result = api.sites.update_site(
        active_validation=True,
        payload=None,
        site=None,
        site_id='string',
        type=None
    )
    return endpoint_result


@pytest.mark.sites
def test_update_site_default(api, validator):
    try:
        assert is_valid_update_site(
            validator,
            update_site_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_membership(json_schema_validate, obj):
    json_schema_validate('jsd_eba669054e08a60e_v1_3_1').validate(obj)
    return True


def get_membership(api):
    endpoint_result = api.sites.get_membership(
        site_id='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_get_membership(api, validator):
    assert is_valid_get_membership(
        validator,
        get_membership(api)
    )


def get_membership_default(api):
    endpoint_result = api.sites.get_membership(
        site_id='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_get_membership_default(api, validator):
    try:
        assert is_valid_get_membership(
            validator,
            get_membership_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site_health(json_schema_validate, obj):
    json_schema_validate('jsd_15b7aa0c4dda8e85_v1_3_1').validate(obj)
    return True


def get_site_health(api):
    endpoint_result = api.sites.get_site_health(
        timestamp=0
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_health(api, validator):
    assert is_valid_get_site_health(
        validator,
        get_site_health(api)
    )


def get_site_health_default(api):
    endpoint_result = api.sites.get_site_health(
        timestamp=None
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_health_default(api, validator):
    try:
        assert is_valid_get_site_health(
            validator,
            get_site_health_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_site(json_schema_validate, obj):
    json_schema_validate('jsd_f083cb13484a8fae_v1_3_1').validate(obj)
    return True


def delete_site(api):
    endpoint_result = api.sites.delete_site(
        site_id='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_delete_site(api, validator):
    assert is_valid_delete_site(
        validator,
        delete_site(api)
    )


def delete_site_default(api):
    endpoint_result = api.sites.delete_site(
        site_id='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_delete_site_default(api, validator):
    try:
        assert is_valid_delete_site(
            validator,
            delete_site_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_assign_device_to_site(json_schema_validate, obj):
    json_schema_validate('jsd_eeb168eb41988e07_v1_3_1').validate(obj)
    return True


def assign_device_to_site(api):
    endpoint_result = api.sites.assign_device_to_site(
        active_validation=True,
        device=[{'ip': 'string'}],
        payload=None,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_assign_device_to_site(api, validator):
    assert is_valid_assign_device_to_site(
        validator,
        assign_device_to_site(api)
    )


def assign_device_to_site_default(api):
    endpoint_result = api.sites.assign_device_to_site(
        active_validation=True,
        device=None,
        payload=None,
        site_id='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_assign_device_to_site_default(api, validator):
    try:
        assert is_valid_assign_device_to_site(
            validator,
            assign_device_to_site_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_site(json_schema_validate, obj):
    json_schema_validate('jsd_50b589fd4c7a930a_v1_3_1').validate(obj)
    return True


def create_site(api):
    endpoint_result = api.sites.create_site(
        active_validation=True,
        payload=None,
        site={'area': {'name': 'string', 'parentName': 'string'}, 'building': {'name': 'string', 'address': 'string', 'parentName': 'string', 'latitude': 0, 'longitude': 0}, 'floor': {'name': 'string', 'parentName': 'string', 'rfModel': 'Cubes And Walled Offices', 'width': 0, 'length': 0, 'height': 0}},
        type='area'
    )
    return endpoint_result


@pytest.mark.sites
def test_create_site(api, validator):
    assert is_valid_create_site(
        validator,
        create_site(api)
    )


def create_site_default(api):
    endpoint_result = api.sites.create_site(
        active_validation=True,
        payload=None,
        site=None,
        type=None
    )
    return endpoint_result


@pytest.mark.sites
def test_create_site_default(api, validator):
    try:
        assert is_valid_create_site(
            validator,
            create_site_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_site_count(json_schema_validate, obj):
    return True if obj else False


def get_site_count(api):
    endpoint_result = api.sites.get_site_count(
        site_id='string'
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_count(api, validator):
    assert is_valid_get_site_count(
        validator,
        get_site_count(api)
    )


def get_site_count_default(api):
    endpoint_result = api.sites.get_site_count(
        site_id=None
    )
    return endpoint_result


@pytest.mark.sites
def test_get_site_count_default(api, validator):
    try:
        assert is_valid_get_site_count(
            validator,
            get_site_count_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
