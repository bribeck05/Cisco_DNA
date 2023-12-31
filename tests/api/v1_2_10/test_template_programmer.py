# -*- coding: utf-8 -*-
"""DNACenterAPI template_programmer API fixtures and tests.

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


def is_valid_gets_the_templates_available(json_schema_validate, obj):
    json_schema_validate('jsd_01b09a254b9ab259_v1_2_10').validate(obj)
    return True


def gets_the_templates_available(api):
    endpoint_result = api.template_programmer.gets_the_templates_available(
        filter_conflicting_templates=True,
        product_family='string',
        product_series='string',
        product_type='string',
        project_id='string',
        software_type='string',
        software_version='string'
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_gets_the_templates_available(api, validator):
    assert is_valid_gets_the_templates_available(
        validator,
        gets_the_templates_available(api)
    )


def gets_the_templates_available_default(api):
    endpoint_result = api.template_programmer.gets_the_templates_available(
        filter_conflicting_templates=None,
        product_family=None,
        product_series=None,
        product_type=None,
        project_id=None,
        software_type=None,
        software_version=None
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_gets_the_templates_available_default(api, validator):
    try:
        assert is_valid_gets_the_templates_available(
            validator,
            gets_the_templates_available_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_project(json_schema_validate, obj):
    json_schema_validate('jsd_00aec9b1422ab27e_v1_2_10').validate(obj)
    return True


def create_project(api):
    endpoint_result = api.template_programmer.create_project(
        active_validation=True,
        createTime=0,
        description='string',
        id='string',
        lastUpdateTime=0,
        name='string',
        payload=None,
        tags=['string'],
        templates={}
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_create_project(api, validator):
    assert is_valid_create_project(
        validator,
        create_project(api)
    )


def create_project_default(api):
    endpoint_result = api.template_programmer.create_project(
        active_validation=True,
        createTime=None,
        description=None,
        id=None,
        lastUpdateTime=None,
        name=None,
        payload=None,
        tags=None,
        templates=None
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_create_project_default(api, validator):
    try:
        assert is_valid_create_project(
            validator,
            create_project_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_template(json_schema_validate, obj):
    json_schema_validate('jsd_7781fa0548a98342_v1_2_10').validate(obj)
    return True


def update_template(api):
    endpoint_result = api.template_programmer.update_template(
        active_validation=True,
        author='string',
        composite=True,
        containingTemplates=[{'composite': True, 'id': 'string', 'name': 'string', 'version': 'string'}],
        createTime=0,
        description='string',
        deviceTypes=[{'productFamily': 'string', 'productSeries': 'string', 'productType': 'string'}],
        failurePolicy='ABORT_ON_ERROR',
        id='string',
        lastUpdateTime=0,
        name='string',
        parentTemplateId='string',
        payload=None,
        projectId='string',
        projectName='string',
        rollbackTemplateContent='string',
        rollbackTemplateParams=[{'binding': 'string', 'dataType': 'STRING', 'defaultValue': 'string', 'description': 'string', 'displayName': 'string', 'group': 'string', 'id': 'string', 'instructionText': 'string', 'key': 'string', 'notParam': True, 'order': 0, 'paramArray': True, 'parameterName': 'string', 'provider': 'string', 'range': [{'id': 'string', 'maxValue': 0, 'minValue': 0}], 'required': True, 'selection': {'id': 'string', 'selectionType': 'SINGLE_SELECT', 'selectionValues': {}}}],
        softwareType='string',
        softwareVariant='string',
        softwareVersion='string',
        tags=['string'],
        templateContent='string',
        templateParams=[{'binding': 'string', 'dataType': 'STRING', 'defaultValue': 'string', 'description': 'string', 'displayName': 'string', 'group': 'string', 'id': 'string', 'instructionText': 'string', 'key': 'string', 'notParam': True, 'order': 0, 'paramArray': True, 'parameterName': 'string', 'provider': 'string', 'range': [{'id': 'string', 'maxValue': 0, 'minValue': 0}], 'required': True, 'selection': {'id': 'string', 'selectionType': 'SINGLE_SELECT', 'selectionValues': {}}}],
        version='string'
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_update_template(api, validator):
    assert is_valid_update_template(
        validator,
        update_template(api)
    )


def update_template_default(api):
    endpoint_result = api.template_programmer.update_template(
        active_validation=True,
        author=None,
        composite=None,
        containingTemplates=None,
        createTime=None,
        description=None,
        deviceTypes=None,
        failurePolicy=None,
        id=None,
        lastUpdateTime=None,
        name=None,
        parentTemplateId=None,
        payload=None,
        projectId=None,
        projectName=None,
        rollbackTemplateContent=None,
        rollbackTemplateParams=None,
        softwareType=None,
        softwareVariant=None,
        softwareVersion=None,
        tags=None,
        templateContent=None,
        templateParams=None,
        version=None
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_update_template_default(api, validator):
    try:
        assert is_valid_update_template(
            validator,
            update_template_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_projects(json_schema_validate, obj):
    json_schema_validate('jsd_109d1b4f4289aecd_v1_2_10').validate(obj)
    return True


def get_projects(api):
    endpoint_result = api.template_programmer.get_projects(
        name='string'
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_get_projects(api, validator):
    assert is_valid_get_projects(
        validator,
        get_projects(api)
    )


def get_projects_default(api):
    endpoint_result = api.template_programmer.get_projects(
        name=None
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_get_projects_default(api, validator):
    try:
        assert is_valid_get_projects(
            validator,
            get_projects_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deploy_template(json_schema_validate, obj):
    json_schema_validate('jsd_6099da82477b858a_v1_2_10').validate(obj)
    return True


def deploy_template(api):
    endpoint_result = api.template_programmer.deploy_template(
        active_validation=True,
        forcePushTemplate=True,
        isComposite=True,
        mainTemplateId='string',
        memberTemplateDeploymentInfo=['string'],
        payload=None,
        targetInfo=[{'hostName': 'string', 'id': 'string', 'params': {}, 'type': 'MANAGED_DEVICE_IP'}],
        templateId='string'
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_deploy_template(api, validator):
    assert is_valid_deploy_template(
        validator,
        deploy_template(api)
    )


def deploy_template_default(api):
    endpoint_result = api.template_programmer.deploy_template(
        active_validation=True,
        forcePushTemplate=None,
        isComposite=None,
        mainTemplateId=None,
        memberTemplateDeploymentInfo=None,
        payload=None,
        targetInfo=None,
        templateId=None
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_deploy_template_default(api, validator):
    try:
        assert is_valid_deploy_template(
            validator,
            deploy_template_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_template_details(json_schema_validate, obj):
    json_schema_validate('jsd_83a3b9404cb88787_v1_2_10').validate(obj)
    return True


def get_template_details(api):
    endpoint_result = api.template_programmer.get_template_details(
        latest_version=True,
        template_id='string'
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_get_template_details(api, validator):
    assert is_valid_get_template_details(
        validator,
        get_template_details(api)
    )


def get_template_details_default(api):
    endpoint_result = api.template_programmer.get_template_details(
        latest_version=None,
        template_id='string'
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_get_template_details_default(api, validator):
    try:
        assert is_valid_get_template_details(
            validator,
            get_template_details_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_project(json_schema_validate, obj):
    json_schema_validate('jsd_9480fa1f47ca9254_v1_2_10').validate(obj)
    return True


def update_project(api):
    endpoint_result = api.template_programmer.update_project(
        active_validation=True,
        createTime=0,
        description='string',
        id='string',
        lastUpdateTime=0,
        name='string',
        payload=None,
        tags=['string'],
        templates={}
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_update_project(api, validator):
    assert is_valid_update_project(
        validator,
        update_project(api)
    )


def update_project_default(api):
    endpoint_result = api.template_programmer.update_project(
        active_validation=True,
        createTime=None,
        description=None,
        id=None,
        lastUpdateTime=None,
        name=None,
        payload=None,
        tags=None,
        templates=None
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_update_project_default(api, validator):
    try:
        assert is_valid_update_project(
            validator,
            update_project_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_template_deployment_status(json_schema_validate, obj):
    json_schema_validate('jsd_9c9a785741cbb41f_v1_2_10').validate(obj)
    return True


def get_template_deployment_status(api):
    endpoint_result = api.template_programmer.get_template_deployment_status(
        deployment_id='string'
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_get_template_deployment_status(api, validator):
    assert is_valid_get_template_deployment_status(
        validator,
        get_template_deployment_status(api)
    )


def get_template_deployment_status_default(api):
    endpoint_result = api.template_programmer.get_template_deployment_status(
        deployment_id='string'
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_get_template_deployment_status_default(api, validator):
    try:
        assert is_valid_get_template_deployment_status(
            validator,
            get_template_deployment_status_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_template(json_schema_validate, obj):
    json_schema_validate('jsd_a7b42836408a8e74_v1_2_10').validate(obj)
    return True


def delete_template(api):
    endpoint_result = api.template_programmer.delete_template(
        template_id='string'
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_delete_template(api, validator):
    assert is_valid_delete_template(
        validator,
        delete_template(api)
    )


def delete_template_default(api):
    endpoint_result = api.template_programmer.delete_template(
        template_id='string'
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_delete_template_default(api, validator):
    try:
        assert is_valid_delete_template(
            validator,
            delete_template_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_version_template(json_schema_validate, obj):
    json_schema_validate('jsd_62b05b2c40a9b216_v1_2_10').validate(obj)
    return True


def version_template(api):
    endpoint_result = api.template_programmer.version_template(
        active_validation=True,
        comments='string',
        payload=None,
        templateId='string'
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_version_template(api, validator):
    assert is_valid_version_template(
        validator,
        version_template(api)
    )


def version_template_default(api):
    endpoint_result = api.template_programmer.version_template(
        active_validation=True,
        comments=None,
        payload=None,
        templateId=None
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_version_template_default(api, validator):
    try:
        assert is_valid_version_template(
            validator,
            version_template_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_preview_template(json_schema_validate, obj):
    json_schema_validate('jsd_f393abe84989bb48_v1_2_10').validate(obj)
    return True


def preview_template(api):
    endpoint_result = api.template_programmer.preview_template(
        active_validation=True,
        params={},
        payload=None,
        templateId='string'
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_preview_template(api, validator):
    assert is_valid_preview_template(
        validator,
        preview_template(api)
    )


def preview_template_default(api):
    endpoint_result = api.template_programmer.preview_template(
        active_validation=True,
        params=None,
        payload=None,
        templateId=None
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_preview_template_default(api, validator):
    try:
        assert is_valid_preview_template(
            validator,
            preview_template_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_project(json_schema_validate, obj):
    json_schema_validate('jsd_d0a1abfa435b841d_v1_2_10').validate(obj)
    return True


def delete_project(api):
    endpoint_result = api.template_programmer.delete_project(
        project_id='string'
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_delete_project(api, validator):
    assert is_valid_delete_project(
        validator,
        delete_project(api)
    )


def delete_project_default(api):
    endpoint_result = api.template_programmer.delete_project(
        project_id='string'
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_delete_project_default(api, validator):
    try:
        assert is_valid_delete_project(
            validator,
            delete_project_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_template(json_schema_validate, obj):
    json_schema_validate('jsd_f6b119ad4d4aaf16_v1_2_10').validate(obj)
    return True


def create_template(api):
    endpoint_result = api.template_programmer.create_template(
        active_validation=True,
        author='string',
        composite=True,
        containingTemplates=[{'composite': True, 'id': 'string', 'name': 'string', 'version': 'string'}],
        createTime=0,
        description='string',
        deviceTypes=[{'productFamily': 'string', 'productSeries': 'string', 'productType': 'string'}],
        failurePolicy='ABORT_ON_ERROR',
        id='string',
        lastUpdateTime=0,
        name='string',
        parentTemplateId='string',
        payload=None,
        projectId='string',
        projectName='string',
        project_id='string',
        rollbackTemplateContent='string',
        rollbackTemplateParams=[{'binding': 'string', 'dataType': 'STRING', 'defaultValue': 'string', 'description': 'string', 'displayName': 'string', 'group': 'string', 'id': 'string', 'instructionText': 'string', 'key': 'string', 'notParam': True, 'order': 0, 'paramArray': True, 'parameterName': 'string', 'provider': 'string', 'range': [{'id': 'string', 'maxValue': 0, 'minValue': 0}], 'required': True, 'selection': {'id': 'string', 'selectionType': 'SINGLE_SELECT', 'selectionValues': {}}}],
        softwareType='string',
        softwareVariant='string',
        softwareVersion='string',
        tags=['string'],
        templateContent='string',
        templateParams=[{'binding': 'string', 'dataType': 'STRING', 'defaultValue': 'string', 'description': 'string', 'displayName': 'string', 'group': 'string', 'id': 'string', 'instructionText': 'string', 'key': 'string', 'notParam': True, 'order': 0, 'paramArray': True, 'parameterName': 'string', 'provider': 'string', 'range': [{'id': 'string', 'maxValue': 0, 'minValue': 0}], 'required': True, 'selection': {'id': 'string', 'selectionType': 'SINGLE_SELECT', 'selectionValues': {}}}],
        version='string'
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_create_template(api, validator):
    assert is_valid_create_template(
        validator,
        create_template(api)
    )


def create_template_default(api):
    endpoint_result = api.template_programmer.create_template(
        active_validation=True,
        author=None,
        composite=None,
        containingTemplates=None,
        createTime=None,
        description=None,
        deviceTypes=None,
        failurePolicy=None,
        id=None,
        lastUpdateTime=None,
        name=None,
        parentTemplateId=None,
        payload=None,
        projectId=None,
        projectName=None,
        project_id='string',
        rollbackTemplateContent=None,
        rollbackTemplateParams=None,
        softwareType=None,
        softwareVariant=None,
        softwareVersion=None,
        tags=None,
        templateContent=None,
        templateParams=None,
        version=None
    )
    return endpoint_result


@pytest.mark.template_programmer
def test_create_template_default(api, validator):
    try:
        assert is_valid_create_template(
            validator,
            create_template_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_template_versions(json_schema_validate, obj):
    return True if obj else False


def get_template_versions(api):
    endpoint_result = api.template_programmer.get_template_versions(
        template_id='string'
    )
    return endpoint_result


@pytest.mark.template_programmer
@pytest.mark.skip(reason="issues currently testing this")
def test_get_template_versions(api, validator):
    assert is_valid_get_template_versions(
        validator,
        get_template_versions(api)
    )


def get_template_versions_default(api):
    endpoint_result = api.template_programmer.get_template_versions(
        template_id='string'
    )
    return endpoint_result


@pytest.mark.template_programmer
@pytest.mark.skip(reason="issues currently testing this")
def test_get_template_versions_default(api, validator):
    try:
        assert is_valid_get_template_versions(
            validator,
            get_template_versions_default(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e
