# -*- coding: utf-8 -*-
"""DNACenterAPI file API fixtures and tests.

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


def is_valid_get_list_of_available_namespaces(json_schema_validate, obj):
    json_schema_validate('jsd_3f89bbfc4f6b8b50_v2_1_1').validate(obj)
    return True


def get_list_of_available_namespaces(api):
    endpoint_result = api.file.get_list_of_available_namespaces(

    )
    return endpoint_result


@pytest.mark.file
def test_get_list_of_available_namespaces(api, validator):
    assert is_valid_get_list_of_available_namespaces(
        validator,
        get_list_of_available_namespaces(api)
    )


def get_list_of_available_namespaces_default(api):
    endpoint_result = api.file.get_list_of_available_namespaces(

    )
    return endpoint_result


@pytest.mark.file
def test_get_list_of_available_namespaces_default(api, validator):
    try:
        assert is_valid_get_list_of_available_namespaces(
            validator,
            get_list_of_available_namespaces_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_list_of_files(json_schema_validate, obj):
    return True if obj else False


def get_list_of_files(api):
    endpoint_result = api.file.get_list_of_files(
        name_space='string'
    )
    return endpoint_result


@pytest.mark.file
def test_get_list_of_files(api, validator):
    assert is_valid_get_list_of_files(
        validator,
        get_list_of_files(api)
    )


def get_list_of_files_default(api):
    endpoint_result = api.file.get_list_of_files(
        name_space='string'
    )
    return endpoint_result


@pytest.mark.file
def test_get_list_of_files_default(api, validator):
    try:
        assert is_valid_get_list_of_files(
            validator,
            get_list_of_files_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_download_a_file_by_fileid(json_schema_validate, obj):
    json_schema_validate('jsd_9698c8ec4a0b8c1a_v2_1_1').validate(obj)
    return True


def download_a_file_by_fileid(api):
    endpoint_result = api.file.download_a_file_by_fileid(
        dirpath=None,
        save_file=None,
        filename=None,
        file_id='string'
    )
    return endpoint_result


@pytest.mark.file
def test_download_a_file_by_fileid(api, validator):
    assert is_valid_download_a_file_by_fileid(
        validator,
        download_a_file_by_fileid(api)
    )


def download_a_file_by_fileid_default(api):
    endpoint_result = api.file.download_a_file_by_fileid(
        dirpath=None,
        save_file=None,
        filename=None,
        file_id='string'
    )
    return endpoint_result


@pytest.mark.file
def test_download_a_file_by_fileid_default(api, validator):
    try:
        assert is_valid_download_a_file_by_fileid(
            validator,
            download_a_file_by_fileid_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
