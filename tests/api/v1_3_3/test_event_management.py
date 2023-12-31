# -*- coding: utf-8 -*-
"""DNACenterAPI event_management API fixtures and tests.

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


def is_valid_count_of_event_subscriptions(json_schema_validate, obj):
    json_schema_validate('jsd_149b7ba04e5890b2_v1_3_3').validate(obj)
    return True


def count_of_event_subscriptions(api):
    endpoint_result = api.event_management.count_of_event_subscriptions(
        event_ids='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_count_of_event_subscriptions(api, validator):
    assert is_valid_count_of_event_subscriptions(
        validator,
        count_of_event_subscriptions(api)
    )


def count_of_event_subscriptions_default(api):
    endpoint_result = api.event_management.count_of_event_subscriptions(
        event_ids=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_count_of_event_subscriptions_default(api, validator):
    try:
        assert is_valid_count_of_event_subscriptions(
            validator,
            count_of_event_subscriptions_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_events(json_schema_validate, obj):
    json_schema_validate('jsd_44a39a074a6a82a2_v1_3_3').validate(obj)
    return True


def get_events(api):
    endpoint_result = api.event_management.get_events(
        event_id=' ',
        limit=10,
        offset=0,
        order='string',
        sort_by='string',
        tags='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_events(api, validator):
    assert is_valid_get_events(
        validator,
        get_events(api)
    )


def get_events_default(api):
    endpoint_result = api.event_management.get_events(
        event_id=None,
        limit=None,
        offset=None,
        order=None,
        sort_by=None,
        tags=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_events_default(api, validator):
    try:
        assert is_valid_get_events(
            validator,
            get_events_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_event_subscriptions(json_schema_validate, obj):
    json_schema_validate('jsd_4f9f7a7b40f990de_v1_3_3').validate(obj)
    return True


def create_event_subscriptions(api):
    endpoint_result = api.event_management.create_event_subscriptions(
        active_validation=True,
        payload=[{'subscriptionId': 'string', 'version': 'string', 'name': 'string', 'description': 'string', 'subscriptionEndpoints': [{'instanceId': 'string', 'subscriptionDetails': {'name': 'string', 'url': 'string', 'method': 'string', 'connectorType': 'string'}}], 'filter': {'eventIds': ['string']}}]
    )
    return endpoint_result


@pytest.mark.event_management
def test_create_event_subscriptions(api, validator):
    assert is_valid_create_event_subscriptions(
        validator,
        create_event_subscriptions(api)
    )


def create_event_subscriptions_default(api):
    endpoint_result = api.event_management.create_event_subscriptions(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_create_event_subscriptions_default(api, validator):
    try:
        assert is_valid_create_event_subscriptions(
            validator,
            create_event_subscriptions_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_event_subscriptions(json_schema_validate, obj):
    json_schema_validate('jsd_579a6a7248cb94cf_v1_3_3').validate(obj)
    return True


def update_event_subscriptions(api):
    endpoint_result = api.event_management.update_event_subscriptions(
        active_validation=True,
        payload=[{'subscriptionId': 'string', 'version': 'string', 'name': 'string', 'description': 'string', 'subscriptionEndpoints': [{'instanceId': 'string', 'subscriptionDetails': {'name': 'string', 'url': 'string', 'method': 'string', 'connectorType': 'string'}}], 'filter': {'eventIds': ['string']}}]
    )
    return endpoint_result


@pytest.mark.event_management
def test_update_event_subscriptions(api, validator):
    assert is_valid_update_event_subscriptions(
        validator,
        update_event_subscriptions(api)
    )


def update_event_subscriptions_default(api):
    endpoint_result = api.event_management.update_event_subscriptions(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_update_event_subscriptions_default(api, validator):
    try:
        assert is_valid_update_event_subscriptions(
            validator,
            update_event_subscriptions_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_count_of_events(json_schema_validate, obj):
    return True if obj else False


def count_of_events(api):
    endpoint_result = api.event_management.count_of_events(
        event_id='string',
        tags='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_count_of_events(api, validator):
    assert is_valid_count_of_events(
        validator,
        count_of_events(api)
    )


def count_of_events_default(api):
    endpoint_result = api.event_management.count_of_events(
        event_id=None,
        tags=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_count_of_events_default(api, validator):
    try:
        assert is_valid_count_of_events(
            validator,
            count_of_events_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_count_of_notifications(json_schema_validate, obj):
    json_schema_validate('jsd_8f93dbe54b2aa1fd_v1_3_3').validate(obj)
    return True


def count_of_notifications(api):
    endpoint_result = api.event_management.count_of_notifications(
        category='string',
        domain='string',
        end_time='string',
        event_ids='string',
        severity='string',
        source='string',
        start_time='string',
        sub_domain='string',
        type='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_count_of_notifications(api, validator):
    assert is_valid_count_of_notifications(
        validator,
        count_of_notifications(api)
    )


def count_of_notifications_default(api):
    endpoint_result = api.event_management.count_of_notifications(
        category=None,
        domain=None,
        end_time=None,
        event_ids=None,
        severity=None,
        source=None,
        start_time=None,
        sub_domain=None,
        type=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_count_of_notifications_default(api, validator):
    try:
        assert is_valid_count_of_notifications(
            validator,
            count_of_notifications_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_event_subscriptions(json_schema_validate, obj):
    json_schema_validate('jsd_93981baa40799483_v1_3_3').validate(obj)
    return True


def delete_event_subscriptions(api):
    endpoint_result = api.event_management.delete_event_subscriptions(
        subscriptions='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_delete_event_subscriptions(api, validator):
    assert is_valid_delete_event_subscriptions(
        validator,
        delete_event_subscriptions(api)
    )


def delete_event_subscriptions_default(api):
    endpoint_result = api.event_management.delete_event_subscriptions(
        subscriptions=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_delete_event_subscriptions_default(api, validator):
    try:
        assert is_valid_delete_event_subscriptions(
            validator,
            delete_event_subscriptions_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_event_subscriptions(json_schema_validate, obj):
    json_schema_validate('jsd_dcaa6bde4feb9152_v1_3_3').validate(obj)
    return True


def get_event_subscriptions(api):
    endpoint_result = api.event_management.get_event_subscriptions(
        event_ids='string',
        limit=10,
        offset=0,
        order='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_event_subscriptions(api, validator):
    assert is_valid_get_event_subscriptions(
        validator,
        get_event_subscriptions(api)
    )


def get_event_subscriptions_default(api):
    endpoint_result = api.event_management.get_event_subscriptions(
        event_ids=None,
        limit=None,
        offset=None,
        order=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_event_subscriptions_default(api, validator):
    try:
        assert is_valid_get_event_subscriptions(
            validator,
            get_event_subscriptions_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_status_api_for_events(json_schema_validate, obj):
    json_schema_validate('jsd_f9bd99c74bba8832_v1_3_3').validate(obj)
    return True


def get_status_api_for_events(api):
    endpoint_result = api.event_management.get_status_api_for_events(
        execution_id='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_status_api_for_events(api, validator):
    assert is_valid_get_status_api_for_events(
        validator,
        get_status_api_for_events(api)
    )


def get_status_api_for_events_default(api):
    endpoint_result = api.event_management.get_status_api_for_events(
        execution_id='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_status_api_for_events_default(api, validator):
    try:
        assert is_valid_get_status_api_for_events(
            validator,
            get_status_api_for_events_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_notifications(json_schema_validate, obj):
    json_schema_validate('jsd_f5a13ab24c5aaa91_v1_3_3').validate(obj)
    return True


def get_notifications(api):
    endpoint_result = api.event_management.get_notifications(
        category='string',
        domain='string',
        end_time='string',
        event_ids='string',
        limit=20,
        offset=0,
        order='string',
        severity='string',
        sort_by='string',
        source='string',
        start_time='string',
        sub_domain='string',
        type='string'
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_notifications(api, validator):
    assert is_valid_get_notifications(
        validator,
        get_notifications(api)
    )


def get_notifications_default(api):
    endpoint_result = api.event_management.get_notifications(
        category=None,
        domain=None,
        end_time=None,
        event_ids=None,
        limit=None,
        offset=None,
        order=None,
        severity=None,
        sort_by=None,
        source=None,
        start_time=None,
        sub_domain=None,
        type=None
    )
    return endpoint_result


@pytest.mark.event_management
def test_get_notifications_default(api, validator):
    try:
        assert is_valid_get_notifications(
            validator,
            get_notifications_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
