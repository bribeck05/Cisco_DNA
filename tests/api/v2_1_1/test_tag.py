# -*- coding: utf-8 -*-
"""DNACenterAPI tag API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.1.1', reason='version does not match')


def is_valid_add_members_to_the_tag(json_schema_validate, obj):
    json_schema_validate('jsd_00a2fa6146089317_v2_1_1').validate(obj)
    return True


def add_members_to_the_tag(api):
    endpoint_result = api.tag.add_members_to_the_tag(
        active_validation=True,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.tag
def test_add_members_to_the_tag(api, validator):
    assert is_valid_add_members_to_the_tag(
        validator,
        add_members_to_the_tag(api)
    )


def add_members_to_the_tag_default(api):
    endpoint_result = api.tag.add_members_to_the_tag(
        active_validation=True,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.tag
def test_add_members_to_the_tag_default(api, validator):
    try:
        assert is_valid_add_members_to_the_tag(
            validator,
            add_members_to_the_tag_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_tag(json_schema_validate, obj):
    json_schema_validate('jsd_1399891c42a8be64_v2_1_1').validate(obj)
    return True


def create_tag(api):
    endpoint_result = api.tag.create_tag(
        active_validation=True,
        description='string',
        dynamicRules=[{'memberType': 'string', 'rules': {'values': ['string'], 'items': ['string'], 'operation': 'string', 'name': 'string', 'value': 'string'}}],
        id='string',
        instanceTenantId='string',
        name='string',
        payload=None,
        systemTag=True
    )
    return endpoint_result


@pytest.mark.tag
def test_create_tag(api, validator):
    assert is_valid_create_tag(
        validator,
        create_tag(api)
    )


def create_tag_default(api):
    endpoint_result = api.tag.create_tag(
        active_validation=True,
        description=None,
        dynamicRules=None,
        id=None,
        instanceTenantId=None,
        name=None,
        payload=None,
        systemTag=None
    )
    return endpoint_result


@pytest.mark.tag
def test_create_tag_default(api, validator):
    try:
        assert is_valid_create_tag(
            validator,
            create_tag_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_tag_member_count(json_schema_validate, obj):
    json_schema_validate('jsd_2e9db85840fbb1cf_v2_1_1').validate(obj)
    return True


def get_tag_member_count(api):
    endpoint_result = api.tag.get_tag_member_count(
        id='string',
        level='0',
        member_association_type='string',
        member_type='string'
    )
    return endpoint_result


@pytest.mark.tag
def test_get_tag_member_count(api, validator):
    assert is_valid_get_tag_member_count(
        validator,
        get_tag_member_count(api)
    )


def get_tag_member_count_default(api):
    endpoint_result = api.tag.get_tag_member_count(
        id='string',
        level=None,
        member_association_type=None,
        member_type=None
    )
    return endpoint_result


@pytest.mark.tag
def test_get_tag_member_count_default(api, validator):
    try:
        assert is_valid_get_tag_member_count(
            validator,
            get_tag_member_count_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_tag(json_schema_validate, obj):
    json_schema_validate('jsd_429c28154bdaa13d_v2_1_1').validate(obj)
    return True


def delete_tag(api):
    endpoint_result = api.tag.delete_tag(
        id='string'
    )
    return endpoint_result


@pytest.mark.tag
def test_delete_tag(api, validator):
    assert is_valid_delete_tag(
        validator,
        delete_tag(api)
    )


def delete_tag_default(api):
    endpoint_result = api.tag.delete_tag(
        id='string'
    )
    return endpoint_result


@pytest.mark.tag
def test_delete_tag_default(api, validator):
    try:
        assert is_valid_delete_tag(
            validator,
            delete_tag_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_updates_tag_membership(json_schema_validate, obj):
    return True if obj else False


def updates_tag_membership(api):
    endpoint_result = api.tag.updates_tag_membership(
        active_validation=True,
        memberToTags=[{'key': ['string']}],
        memberType='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.tag
def test_updates_tag_membership(api, validator):
    assert is_valid_updates_tag_membership(
        validator,
        updates_tag_membership(api)
    )


def updates_tag_membership_default(api):
    endpoint_result = api.tag.updates_tag_membership(
        active_validation=True,
        memberToTags=None,
        memberType=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.tag
def test_updates_tag_membership_default(api, validator):
    try:
        assert is_valid_updates_tag_membership(
            validator,
            updates_tag_membership_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_tag_resource_types(json_schema_validate, obj):
    return True if obj else False


def get_tag_resource_types(api):
    endpoint_result = api.tag.get_tag_resource_types(

    )
    return endpoint_result


@pytest.mark.tag
def test_get_tag_resource_types(api, validator):
    assert is_valid_get_tag_resource_types(
        validator,
        get_tag_resource_types(api)
    )


def get_tag_resource_types_default(api):
    endpoint_result = api.tag.get_tag_resource_types(

    )
    return endpoint_result


@pytest.mark.tag
def test_get_tag_resource_types_default(api, validator):
    try:
        assert is_valid_get_tag_resource_types(
            validator,
            get_tag_resource_types_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_tag(json_schema_validate, obj):
    json_schema_validate('jsd_4d86a993469a9da9_v2_1_1').validate(obj)
    return True


def update_tag(api):
    endpoint_result = api.tag.update_tag(
        active_validation=True,
        description='string',
        dynamicRules=[{'memberType': 'string', 'rules': {'values': ['string'], 'items': ['string'], 'operation': 'string', 'name': 'string', 'value': 'string'}}],
        id='string',
        instanceTenantId='string',
        name='string',
        payload=None,
        systemTag=True
    )
    return endpoint_result


@pytest.mark.tag
def test_update_tag(api, validator):
    assert is_valid_update_tag(
        validator,
        update_tag(api)
    )


def update_tag_default(api):
    endpoint_result = api.tag.update_tag(
        active_validation=True,
        description=None,
        dynamicRules=None,
        id=None,
        instanceTenantId=None,
        name=None,
        payload=None,
        systemTag=None
    )
    return endpoint_result


@pytest.mark.tag
def test_update_tag_default(api, validator):
    try:
        assert is_valid_update_tag(
            validator,
            update_tag_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_tag_count(json_schema_validate, obj):
    json_schema_validate('jsd_8091a9b84bfba53b_v2_1_1').validate(obj)
    return True


def get_tag_count(api):
    endpoint_result = api.tag.get_tag_count(
        attribute_name='string',
        level='string',
        name='string',
        name_space='string',
        size='string',
        system_tag='string'
    )
    return endpoint_result


@pytest.mark.tag
def test_get_tag_count(api, validator):
    assert is_valid_get_tag_count(
        validator,
        get_tag_count(api)
    )


def get_tag_count_default(api):
    endpoint_result = api.tag.get_tag_count(
        attribute_name=None,
        level=None,
        name=None,
        name_space=None,
        size=None,
        system_tag=None
    )
    return endpoint_result


@pytest.mark.tag
def test_get_tag_count_default(api, validator):
    try:
        assert is_valid_get_tag_count(
            validator,
            get_tag_count_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_tag_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_c1a359b14c89b573_v2_1_1').validate(obj)
    return True


def get_tag_by_id(api):
    endpoint_result = api.tag.get_tag_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.tag
def test_get_tag_by_id(api, validator):
    assert is_valid_get_tag_by_id(
        validator,
        get_tag_by_id(api)
    )


def get_tag_by_id_default(api):
    endpoint_result = api.tag.get_tag_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.tag
def test_get_tag_by_id_default(api, validator):
    try:
        assert is_valid_get_tag_by_id(
            validator,
            get_tag_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_remove_tag_member(json_schema_validate, obj):
    json_schema_validate('jsd_caa3ea704d78b37e_v2_1_1').validate(obj)
    return True


def remove_tag_member(api):
    endpoint_result = api.tag.remove_tag_member(
        id='string',
        member_id='string'
    )
    return endpoint_result


@pytest.mark.tag
def test_remove_tag_member(api, validator):
    assert is_valid_remove_tag_member(
        validator,
        remove_tag_member(api)
    )


def remove_tag_member_default(api):
    endpoint_result = api.tag.remove_tag_member(
        id='string',
        member_id='string'
    )
    return endpoint_result


@pytest.mark.tag
def test_remove_tag_member_default(api, validator):
    try:
        assert is_valid_remove_tag_member(
            validator,
            remove_tag_member_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_tag_members_by_id(json_schema_validate, obj):
    return True if obj else False


def get_tag_members_by_id(api):
    endpoint_result = api.tag.get_tag_members_by_id(
        id='string',
        level='0',
        limit='string',
        member_association_type='string',
        member_type='string',
        offset='string'
    )
    return endpoint_result


@pytest.mark.tag
def test_get_tag_members_by_id(api, validator):
    assert is_valid_get_tag_members_by_id(
        validator,
        get_tag_members_by_id(api)
    )


def get_tag_members_by_id_default(api):
    endpoint_result = api.tag.get_tag_members_by_id(
        id='string',
        level=None,
        limit=None,
        member_association_type=None,
        member_type=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.tag
def test_get_tag_members_by_id_default(api, validator):
    try:
        assert is_valid_get_tag_members_by_id(
            validator,
            get_tag_members_by_id_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_tag(json_schema_validate, obj):
    json_schema_validate('jsd_ee9aab01487a8896_v2_1_1').validate(obj)
    return True


def get_tag(api):
    endpoint_result = api.tag.get_tag(
        additional_info_attributes='string',
        additional_info_name_space='string',
        field='string',
        level='string',
        limit='string',
        name='string',
        offset='string',
        order='string',
        size='string',
        sort_by='string',
        system_tag='string'
    )
    return endpoint_result


@pytest.mark.tag
def test_get_tag(api, validator):
    assert is_valid_get_tag(
        validator,
        get_tag(api)
    )


def get_tag_default(api):
    endpoint_result = api.tag.get_tag(
        additional_info_attributes=None,
        additional_info_name_space=None,
        field=None,
        level=None,
        limit=None,
        name=None,
        offset=None,
        order=None,
        size=None,
        sort_by=None,
        system_tag=None
    )
    return endpoint_result


@pytest.mark.tag
def test_get_tag_default(api, validator):
    try:
        assert is_valid_get_tag(
            validator,
            get_tag_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
