
# -*- coding: utf-8 -*-
"""Test suite for the community-developed Python SDK for the DNA Center APIs.

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

import dnacentersdk
import requests
from tests.environment import (
    DNA_CENTER_USERNAME, DNA_CENTER_PASSWORD,
    DNA_CENTER_ENCODED_AUTH, DNA_CENTER_VERSION,
)

from dnacentersdk.api.authentication import Authentication
from dnacentersdk.api.v1_2_10.clients import \
    Clients as Clients_v1_2_10
from dnacentersdk.api.v1_2_10.command_runner import \
    CommandRunner as CommandRunner_v1_2_10
from dnacentersdk.api.v1_2_10.devices import \
    Devices as Devices_v1_2_10
from dnacentersdk.api.v1_2_10.fabric_wired import \
    FabricWired as FabricWired_v1_2_10
from dnacentersdk.api.v1_2_10.file import \
    File as File_v1_2_10
from dnacentersdk.api.v1_2_10.network_discovery import \
    NetworkDiscovery as NetworkDiscovery_v1_2_10
from dnacentersdk.api.v1_2_10.networks import \
    Networks as Networks_v1_2_10
from dnacentersdk.api.v1_2_10.non_fabric_wireless import \
    NonFabricWireless as NonFabricWireless_v1_2_10
from dnacentersdk.api.v1_2_10.path_trace import \
    PathTrace as PathTrace_v1_2_10
from dnacentersdk.api.v1_2_10.pnp import \
    Pnp as Pnp_v1_2_10
from dnacentersdk.api.v1_2_10.swim import \
    Swim as Swim_v1_2_10
from dnacentersdk.api.v1_2_10.site_profile import \
    SiteProfile as SiteProfile_v1_2_10
from dnacentersdk.api.v1_2_10.sites import \
    Sites as Sites_v1_2_10
from dnacentersdk.api.v1_2_10.tag import \
    Tag as Tag_v1_2_10
from dnacentersdk.api.v1_2_10.task import \
    Task as Task_v1_2_10
from dnacentersdk.api.v1_2_10.template_programmer import \
    TemplateProgrammer as TemplateProgrammer_v1_2_10
from dnacentersdk.api.v1_3_0.clients import \
    Clients as Clients_v1_3_0
from dnacentersdk.api.v1_3_0.command_runner import \
    CommandRunner as CommandRunner_v1_3_0
from dnacentersdk.api.v1_3_0.devices import \
    Devices as Devices_v1_3_0
from dnacentersdk.api.v1_3_0.fabric_wired import \
    FabricWired as FabricWired_v1_3_0
from dnacentersdk.api.v1_3_0.file import \
    File as File_v1_3_0
from dnacentersdk.api.v1_3_0.network_discovery import \
    NetworkDiscovery as NetworkDiscovery_v1_3_0
from dnacentersdk.api.v1_3_0.networks import \
    Networks as Networks_v1_3_0
from dnacentersdk.api.v1_3_0.non_fabric_wireless import \
    NonFabricWireless as NonFabricWireless_v1_3_0
from dnacentersdk.api.v1_3_0.path_trace import \
    PathTrace as PathTrace_v1_3_0
from dnacentersdk.api.v1_3_0.pnp import \
    Pnp as Pnp_v1_3_0
from dnacentersdk.api.v1_3_0.swim import \
    Swim as Swim_v1_3_0
from dnacentersdk.api.v1_3_0.site_profile import \
    SiteProfile as SiteProfile_v1_3_0
from dnacentersdk.api.v1_3_0.sites import \
    Sites as Sites_v1_3_0
from dnacentersdk.api.v1_3_0.tag import \
    Tag as Tag_v1_3_0
from dnacentersdk.api.v1_3_0.task import \
    Task as Task_v1_3_0
from dnacentersdk.api.v1_3_0.template_programmer import \
    TemplateProgrammer as TemplateProgrammer_v1_3_0
from dnacentersdk.api.v1_3_1.application_policy import \
    ApplicationPolicy as ApplicationPolicy_v1_3_1
from dnacentersdk.api.v1_3_1.clients import \
    Clients as Clients_v1_3_1
from dnacentersdk.api.v1_3_1.command_runner import \
    CommandRunner as CommandRunner_v1_3_1
from dnacentersdk.api.v1_3_1.configuration_templates import \
    ConfigurationTemplates as ConfigurationTemplates_v1_3_1
from dnacentersdk.api.v1_3_1.device_onboarding_pnp import \
    DeviceOnboardingPnp as DeviceOnboardingPnp_v1_3_1
from dnacentersdk.api.v1_3_1.devices import \
    Devices as Devices_v1_3_1
from dnacentersdk.api.v1_3_1.event_management import \
    EventManagement as EventManagement_v1_3_1
from dnacentersdk.api.v1_3_1.fabric_wired import \
    FabricWired as FabricWired_v1_3_1
from dnacentersdk.api.v1_3_1.file import \
    File as File_v1_3_1
from dnacentersdk.api.v1_3_1.issues import \
    Issues as Issues_v1_3_1
from dnacentersdk.api.v1_3_1.network_discovery import \
    NetworkDiscovery as NetworkDiscovery_v1_3_1
from dnacentersdk.api.v1_3_1.network_settings import \
    NetworkSettings as NetworkSettings_v1_3_1
from dnacentersdk.api.v1_3_1.non_fabric_wireless import \
    NonFabricWireless as NonFabricWireless_v1_3_1
from dnacentersdk.api.v1_3_1.path_trace import \
    PathTrace as PathTrace_v1_3_1
from dnacentersdk.api.v1_3_1.site_design import \
    SiteDesign as SiteDesign_v1_3_1
from dnacentersdk.api.v1_3_1.sites import \
    Sites as Sites_v1_3_1
from dnacentersdk.api.v1_3_1.software_image_management_swim import \
    SoftwareImageManagementSwim as SoftwareImageManagementSwim_v1_3_1
from dnacentersdk.api.v1_3_1.tag import \
    Tag as Tag_v1_3_1
from dnacentersdk.api.v1_3_1.task import \
    Task as Task_v1_3_1
from dnacentersdk.api.v1_3_1.topology import \
    Topology as Topology_v1_3_1
from dnacentersdk.api.v1_3_1.users import \
    Users as Users_v1_3_1
from dnacentersdk.api.v1_3_3.application_policy import \
    ApplicationPolicy as ApplicationPolicy_v1_3_3
from dnacentersdk.api.v1_3_3.clients import \
    Clients as Clients_v1_3_3
from dnacentersdk.api.v1_3_3.command_runner import \
    CommandRunner as CommandRunner_v1_3_3
from dnacentersdk.api.v1_3_3.configuration_templates import \
    ConfigurationTemplates as ConfigurationTemplates_v1_3_3
from dnacentersdk.api.v1_3_3.device_onboarding_pnp import \
    DeviceOnboardingPnp as DeviceOnboardingPnp_v1_3_3
from dnacentersdk.api.v1_3_3.devices import \
    Devices as Devices_v1_3_3
from dnacentersdk.api.v1_3_3.discovery import \
    Discovery as Discovery_v1_3_3
from dnacentersdk.api.v1_3_3.event_management import \
    EventManagement as EventManagement_v1_3_3
from dnacentersdk.api.v1_3_3.file import \
    File as File_v1_3_3
from dnacentersdk.api.v1_3_3.issues import \
    Issues as Issues_v1_3_3
from dnacentersdk.api.v1_3_3.network_settings import \
    NetworkSettings as NetworkSettings_v1_3_3
from dnacentersdk.api.v1_3_3.path_trace import \
    PathTrace as PathTrace_v1_3_3
from dnacentersdk.api.v1_3_3.sda import \
    Sda as Sda_v1_3_3
from dnacentersdk.api.v1_3_3.site_design import \
    SiteDesign as SiteDesign_v1_3_3
from dnacentersdk.api.v1_3_3.sites import \
    Sites as Sites_v1_3_3
from dnacentersdk.api.v1_3_3.software_image_management_swim import \
    SoftwareImageManagementSwim as SoftwareImageManagementSwim_v1_3_3
from dnacentersdk.api.v1_3_3.tag import \
    Tag as Tag_v1_3_3
from dnacentersdk.api.v1_3_3.task import \
    Task as Task_v1_3_3
from dnacentersdk.api.v1_3_3.topology import \
    Topology as Topology_v1_3_3
from dnacentersdk.api.v1_3_3.users import \
    Users as Users_v1_3_3
from dnacentersdk.api.v1_3_3.wireless import \
    Wireless as Wireless_v1_3_3
from dnacentersdk.api.v2_1_1.application_policy import \
    ApplicationPolicy as ApplicationPolicy_v2_1_1
from dnacentersdk.api.v2_1_1.clients import \
    Clients as Clients_v2_1_1
from dnacentersdk.api.v2_1_1.command_runner import \
    CommandRunner as CommandRunner_v2_1_1
from dnacentersdk.api.v2_1_1.configuration_templates import \
    ConfigurationTemplates as ConfigurationTemplates_v2_1_1
from dnacentersdk.api.v2_1_1.device_onboarding_pnp import \
    DeviceOnboardingPnp as DeviceOnboardingPnp_v2_1_1
from dnacentersdk.api.v2_1_1.device_replacement import \
    DeviceReplacement as DeviceReplacement_v2_1_1
from dnacentersdk.api.v2_1_1.devices import \
    Devices as Devices_v2_1_1
from dnacentersdk.api.v2_1_1.discovery import \
    Discovery as Discovery_v2_1_1
from dnacentersdk.api.v2_1_1.event_management import \
    EventManagement as EventManagement_v2_1_1
from dnacentersdk.api.v2_1_1.file import \
    File as File_v2_1_1
from dnacentersdk.api.v2_1_1.itsm import \
    Itsm as Itsm_v2_1_1
from dnacentersdk.api.v2_1_1.issues import \
    Issues as Issues_v2_1_1
from dnacentersdk.api.v2_1_1.network_settings import \
    NetworkSettings as NetworkSettings_v2_1_1
from dnacentersdk.api.v2_1_1.path_trace import \
    PathTrace as PathTrace_v2_1_1
from dnacentersdk.api.v2_1_1.sda import \
    Sda as Sda_v2_1_1
from dnacentersdk.api.v2_1_1.site_design import \
    SiteDesign as SiteDesign_v2_1_1
from dnacentersdk.api.v2_1_1.sites import \
    Sites as Sites_v2_1_1
from dnacentersdk.api.v2_1_1.software_image_management_swim import \
    SoftwareImageManagementSwim as SoftwareImageManagementSwim_v2_1_1
from dnacentersdk.api.v2_1_1.tag import \
    Tag as Tag_v2_1_1
from dnacentersdk.api.v2_1_1.task import \
    Task as Task_v2_1_1
from dnacentersdk.api.v2_1_1.topology import \
    Topology as Topology_v2_1_1
from dnacentersdk.api.v2_1_1.users import \
    Users as Users_v2_1_1
from dnacentersdk.api.v2_1_1.wireless import \
    Wireless as Wireless_v2_1_1
from dnacentersdk.api.v2_1_2.application_policy import \
    ApplicationPolicy as ApplicationPolicy_v2_1_2
from dnacentersdk.api.v2_1_2.applications import \
    Applications as Applications_v2_1_2
from dnacentersdk.api.v2_1_2.clients import \
    Clients as Clients_v2_1_2
from dnacentersdk.api.v2_1_2.command_runner import \
    CommandRunner as CommandRunner_v2_1_2
from dnacentersdk.api.v2_1_2.configuration_archive import \
    ConfigurationArchive as ConfigurationArchive_v2_1_2
from dnacentersdk.api.v2_1_2.configuration_templates import \
    ConfigurationTemplates as ConfigurationTemplates_v2_1_2
from dnacentersdk.api.v2_1_2.device_onboarding_pnp import \
    DeviceOnboardingPnp as DeviceOnboardingPnp_v2_1_2
from dnacentersdk.api.v2_1_2.device_replacement import \
    DeviceReplacement as DeviceReplacement_v2_1_2
from dnacentersdk.api.v2_1_2.devices import \
    Devices as Devices_v2_1_2
from dnacentersdk.api.v2_1_2.discovery import \
    Discovery as Discovery_v2_1_2
from dnacentersdk.api.v2_1_2.event_management import \
    EventManagement as EventManagement_v2_1_2
from dnacentersdk.api.v2_1_2.file import \
    File as File_v2_1_2
from dnacentersdk.api.v2_1_2.itsm import \
    Itsm as Itsm_v2_1_2
from dnacentersdk.api.v2_1_2.issues import \
    Issues as Issues_v2_1_2
from dnacentersdk.api.v2_1_2.network_settings import \
    NetworkSettings as NetworkSettings_v2_1_2
from dnacentersdk.api.v2_1_2.path_trace import \
    PathTrace as PathTrace_v2_1_2
from dnacentersdk.api.v2_1_2.sda import \
    Sda as Sda_v2_1_2
from dnacentersdk.api.v2_1_2.sensors import \
    Sensors as Sensors_v2_1_2
from dnacentersdk.api.v2_1_2.site_design import \
    SiteDesign as SiteDesign_v2_1_2
from dnacentersdk.api.v2_1_2.sites import \
    Sites as Sites_v2_1_2
from dnacentersdk.api.v2_1_2.software_image_management_swim import \
    SoftwareImageManagementSwim as SoftwareImageManagementSwim_v2_1_2
from dnacentersdk.api.v2_1_2.tag import \
    Tag as Tag_v2_1_2
from dnacentersdk.api.v2_1_2.task import \
    Task as Task_v2_1_2
from dnacentersdk.api.v2_1_2.topology import \
    Topology as Topology_v2_1_2
from dnacentersdk.api.v2_1_2.users import \
    Users as Users_v2_1_2
from dnacentersdk.api.v2_1_2.wireless import \
    Wireless as Wireless_v2_1_2
from dnacentersdk.api.v2_2_1.application_policy import \
    ApplicationPolicy as ApplicationPolicy_v2_2_1
from dnacentersdk.api.v2_2_1.applications import \
    Applications as Applications_v2_2_1
from dnacentersdk.api.v2_2_1.clients import \
    Clients as Clients_v2_2_1
from dnacentersdk.api.v2_2_1.command_runner import \
    CommandRunner as CommandRunner_v2_2_1
from dnacentersdk.api.v2_2_1.compliance import \
    Compliance as Compliance_v2_2_1
from dnacentersdk.api.v2_2_1.configuration_archive import \
    ConfigurationArchive as ConfigurationArchive_v2_2_1
from dnacentersdk.api.v2_2_1.configuration_templates import \
    ConfigurationTemplates as ConfigurationTemplates_v2_2_1
from dnacentersdk.api.v2_2_1.device_onboarding_pnp import \
    DeviceOnboardingPnp as DeviceOnboardingPnp_v2_2_1
from dnacentersdk.api.v2_2_1.device_replacement import \
    DeviceReplacement as DeviceReplacement_v2_2_1
from dnacentersdk.api.v2_2_1.devices import \
    Devices as Devices_v2_2_1
from dnacentersdk.api.v2_2_1.discovery import \
    Discovery as Discovery_v2_2_1
from dnacentersdk.api.v2_2_1.event_management import \
    EventManagement as EventManagement_v2_2_1
from dnacentersdk.api.v2_2_1.file import \
    File as File_v2_2_1
from dnacentersdk.api.v2_2_1.itsm import \
    Itsm as Itsm_v2_2_1
from dnacentersdk.api.v2_2_1.issues import \
    Issues as Issues_v2_2_1
from dnacentersdk.api.v2_2_1.network_settings import \
    NetworkSettings as NetworkSettings_v2_2_1
from dnacentersdk.api.v2_2_1.path_trace import \
    PathTrace as PathTrace_v2_2_1
from dnacentersdk.api.v2_2_1.reports import \
    Reports as Reports_v2_2_1
from dnacentersdk.api.v2_2_1.sda import \
    Sda as Sda_v2_2_1
from dnacentersdk.api.v2_2_1.security_advisories import \
    SecurityAdvisories as SecurityAdvisories_v2_2_1
from dnacentersdk.api.v2_2_1.sensors import \
    Sensors as Sensors_v2_2_1
from dnacentersdk.api.v2_2_1.site_design import \
    SiteDesign as SiteDesign_v2_2_1
from dnacentersdk.api.v2_2_1.sites import \
    Sites as Sites_v2_2_1
from dnacentersdk.api.v2_2_1.software_image_management_swim import \
    SoftwareImageManagementSwim as SoftwareImageManagementSwim_v2_2_1
from dnacentersdk.api.v2_2_1.tag import \
    Tag as Tag_v2_2_1
from dnacentersdk.api.v2_2_1.task import \
    Task as Task_v2_2_1
from dnacentersdk.api.v2_2_1.topology import \
    Topology as Topology_v2_2_1
from dnacentersdk.api.v2_2_1.users import \
    Users as Users_v2_2_1
from dnacentersdk.api.v2_2_1.wireless import \
    Wireless as Wireless_v2_2_1
from dnacentersdk.api.v2_2_2_3.application_policy import \
    ApplicationPolicy as ApplicationPolicy_v2_2_2_3
from dnacentersdk.api.v2_2_2_3.applications import \
    Applications as Applications_v2_2_2_3
from dnacentersdk.api.v2_2_2_3.authentication_management import \
    AuthenticationManagement as AuthenticationManagement_v2_2_2_3
from dnacentersdk.api.v2_2_2_3.clients import \
    Clients as Clients_v2_2_2_3
from dnacentersdk.api.v2_2_2_3.command_runner import \
    CommandRunner as CommandRunner_v2_2_2_3
from dnacentersdk.api.v2_2_2_3.compliance import \
    Compliance as Compliance_v2_2_2_3
from dnacentersdk.api.v2_2_2_3.configuration_archive import \
    ConfigurationArchive as ConfigurationArchive_v2_2_2_3
from dnacentersdk.api.v2_2_2_3.configuration_templates import \
    ConfigurationTemplates as ConfigurationTemplates_v2_2_2_3
from dnacentersdk.api.v2_2_2_3.device_onboarding_pnp import \
    DeviceOnboardingPnp as DeviceOnboardingPnp_v2_2_2_3
from dnacentersdk.api.v2_2_2_3.device_replacement import \
    DeviceReplacement as DeviceReplacement_v2_2_2_3
from dnacentersdk.api.v2_2_2_3.devices import \
    Devices as Devices_v2_2_2_3
from dnacentersdk.api.v2_2_2_3.discovery import \
    Discovery as Discovery_v2_2_2_3
from dnacentersdk.api.v2_2_2_3.event_management import \
    EventManagement as EventManagement_v2_2_2_3
from dnacentersdk.api.v2_2_2_3.file import \
    File as File_v2_2_2_3
from dnacentersdk.api.v2_2_2_3.health_and_performance import \
    HealthAndPerformance as HealthAndPerformance_v2_2_2_3
from dnacentersdk.api.v2_2_2_3.itsm import \
    Itsm as Itsm_v2_2_2_3
from dnacentersdk.api.v2_2_2_3.issues import \
    Issues as Issues_v2_2_2_3
from dnacentersdk.api.v2_2_2_3.licenses import \
    Licenses as Licenses_v2_2_2_3
from dnacentersdk.api.v2_2_2_3.network_settings import \
    NetworkSettings as NetworkSettings_v2_2_2_3
from dnacentersdk.api.v2_2_2_3.path_trace import \
    PathTrace as PathTrace_v2_2_2_3
from dnacentersdk.api.v2_2_2_3.platform_configuration import \
    PlatformConfiguration as PlatformConfiguration_v2_2_2_3
from dnacentersdk.api.v2_2_2_3.reports import \
    Reports as Reports_v2_2_2_3
from dnacentersdk.api.v2_2_2_3.sda import \
    Sda as Sda_v2_2_2_3
from dnacentersdk.api.v2_2_2_3.security_advisories import \
    SecurityAdvisories as SecurityAdvisories_v2_2_2_3
from dnacentersdk.api.v2_2_2_3.sensors import \
    Sensors as Sensors_v2_2_2_3
from dnacentersdk.api.v2_2_2_3.site_design import \
    SiteDesign as SiteDesign_v2_2_2_3
from dnacentersdk.api.v2_2_2_3.sites import \
    Sites as Sites_v2_2_2_3
from dnacentersdk.api.v2_2_2_3.software_image_management_swim import \
    SoftwareImageManagementSwim as SoftwareImageManagementSwim_v2_2_2_3
from dnacentersdk.api.v2_2_2_3.tag import \
    Tag as Tag_v2_2_2_3
from dnacentersdk.api.v2_2_2_3.task import \
    Task as Task_v2_2_2_3
from dnacentersdk.api.v2_2_2_3.topology import \
    Topology as Topology_v2_2_2_3
from dnacentersdk.api.v2_2_2_3.users import \
    Users as Users_v2_2_2_3
from dnacentersdk.api.v2_2_2_3.wireless import \
    Wireless as Wireless_v2_2_2_3
from dnacentersdk.api.v2_2_3_3.application_policy import \
    ApplicationPolicy as ApplicationPolicy_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.applications import \
    Applications as Applications_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.authentication_management import \
    AuthenticationManagement as AuthenticationManagement_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.clients import \
    Clients as Clients_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.command_runner import \
    CommandRunner as CommandRunner_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.compliance import \
    Compliance as Compliance_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.configuration_archive import \
    ConfigurationArchive as ConfigurationArchive_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.configuration_templates import \
    ConfigurationTemplates as ConfigurationTemplates_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.device_onboarding_pnp import \
    DeviceOnboardingPnp as DeviceOnboardingPnp_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.device_replacement import \
    DeviceReplacement as DeviceReplacement_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.devices import \
    Devices as Devices_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.disaster_recovery import \
    DisasterRecovery as DisasterRecovery_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.discovery import \
    Discovery as Discovery_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.event_management import \
    EventManagement as EventManagement_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.fabric_wireless import \
    FabricWireless as FabricWireless_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.file import \
    File as File_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.health_and_performance import \
    HealthAndPerformance as HealthAndPerformance_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.itsm import \
    Itsm as Itsm_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.issues import \
    Issues as Issues_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.licenses import \
    Licenses as Licenses_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.network_settings import \
    NetworkSettings as NetworkSettings_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.path_trace import \
    PathTrace as PathTrace_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.platform_configuration import \
    PlatformConfiguration as PlatformConfiguration_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.policy import \
    Policy as Policy_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.reports import \
    Reports as Reports_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.sda import \
    Sda as Sda_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.security_advisories import \
    SecurityAdvisories as SecurityAdvisories_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.sensors import \
    Sensors as Sensors_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.site_design import \
    SiteDesign as SiteDesign_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.sites import \
    Sites as Sites_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.software_image_management_swim import \
    SoftwareImageManagementSwim as SoftwareImageManagementSwim_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.tag import \
    Tag as Tag_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.task import \
    Task as Task_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.topology import \
    Topology as Topology_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.users import \
    Users as Users_v2_2_3_3
from dnacentersdk.api.v2_2_3_3.wireless import \
    Wireless as Wireless_v2_2_3_3
from dnacentersdk.api.authentication import Authentication
from dnacentersdk.api.v2_3_3_0.application_policy import \
    ApplicationPolicy as ApplicationPolicy_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.applications import \
    Applications as Applications_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.cisco_dna_center_system import \
    CiscoDnaCenterSystem as CiscoDnaCenterSystem_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.clients import \
    Clients as Clients_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.command_runner import \
    CommandRunner as CommandRunner_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.compliance import \
    Compliance as Compliance_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.configuration_archive import \
    ConfigurationArchive as ConfigurationArchive_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.configuration_templates import \
    ConfigurationTemplates as ConfigurationTemplates_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.device_onboarding_pnp import \
    DeviceOnboardingPnp as DeviceOnboardingPnp_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.device_replacement import \
    DeviceReplacement as DeviceReplacement_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.devices import \
    Devices as Devices_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.discovery import \
    Discovery as Discovery_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.event_management import \
    EventManagement as EventManagement_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.fabric_wireless import \
    FabricWireless as FabricWireless_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.file import \
    File as File_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.health_and_performance import \
    HealthAndPerformance as HealthAndPerformance_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.itsm import \
    Itsm as Itsm_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.issues import \
    Issues as Issues_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.lan_automation import \
    LanAutomation as LanAutomation_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.licenses import \
    Licenses as Licenses_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.network_settings import \
    NetworkSettings as NetworkSettings_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.path_trace import \
    PathTrace as PathTrace_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.platform_configuration import \
    PlatformConfiguration as PlatformConfiguration_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.reports import \
    Reports as Reports_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.sda import \
    Sda as Sda_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.security_advisories import \
    SecurityAdvisories as SecurityAdvisories_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.sensors import \
    Sensors as Sensors_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.site_design import \
    SiteDesign as SiteDesign_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.sites import \
    Sites as Sites_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.software_image_management_swim import \
    SoftwareImageManagementSwim as SoftwareImageManagementSwim_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.system_settings import \
    SystemSettings as SystemSettings_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.tag import \
    Tag as Tag_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.task import \
    Task as Task_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.topology import \
    Topology as Topology_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.users import \
    Users as Users_v2_3_3_0
from dnacentersdk.api.v2_3_3_0.wireless import \
    Wireless as Wireless_v2_3_3_0
from dnacentersdk.api.v2_3_5_3.application_policy import \
    ApplicationPolicy as ApplicationPolicy_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.applications import \
    Applications as Applications_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.authentication_management import \
    AuthenticationManagement as AuthenticationManagement_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.cisco_dna_center_system import \
    CiscoDnaCenterSystem as CiscoDnaCenterSystem_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.clients import \
    Clients as Clients_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.command_runner import \
    CommandRunner as CommandRunner_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.compliance import \
    Compliance as Compliance_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.configuration_archive import \
    ConfigurationArchive as ConfigurationArchive_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.configuration_templates import \
    ConfigurationTemplates as ConfigurationTemplates_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.device_onboarding_pnp import \
    DeviceOnboardingPnp as DeviceOnboardingPnp_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.device_replacement import \
    DeviceReplacement as DeviceReplacement_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.devices import \
    Devices as Devices_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.discovery import \
    Discovery as Discovery_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.eox import \
    EoX as EoX_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.event_management import \
    EventManagement as EventManagement_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.fabric_wireless import \
    FabricWireless as FabricWireless_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.file import \
    File as File_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.health_and_performance import \
    HealthAndPerformance as HealthAndPerformance_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.itsm import \
    Itsm as Itsm_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.itsm_integration import \
    ItsmIntegration as ItsmIntegration_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.issues import \
    Issues as Issues_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.lan_automation import \
    LanAutomation as LanAutomation_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.licenses import \
    Licenses as Licenses_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.network_settings import \
    NetworkSettings as NetworkSettings_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.path_trace import \
    PathTrace as PathTrace_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.platform import \
    Platform as Platform_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.reports import \
    Reports as Reports_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.sda import \
    Sda as Sda_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.security_advisories import \
    SecurityAdvisories as SecurityAdvisories_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.sensors import \
    Sensors as Sensors_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.site_design import \
    SiteDesign as SiteDesign_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.sites import \
    Sites as Sites_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.software_image_management_swim import \
    SoftwareImageManagementSwim as SoftwareImageManagementSwim_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.system_settings import \
    SystemSettings as SystemSettings_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.tag import \
    Tag as Tag_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.task import \
    Task as Task_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.topology import \
    Topology as Topology_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.user_and_roles import \
    UserandRoles as UserandRoles_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.users import \
    Users as Users_v2_3_5_3
from dnacentersdk.api.v2_3_5_3.wireless import \
    Wireless as Wireless_v2_3_5_3
from dnacentersdk.api.custom_caller import CustomCaller

from tests.config import (
    DEFAULT_VERIFY,
    DEFAULT_SINGLE_REQUEST_TIMEOUT,
    DEFAULT_WAIT_ON_RATE_LIMIT
)

import pytest


@pytest.mark.dnacentersdk
class TestDNACenterSDK:
    """Test the package-level code."""

    def test_package_contents(self):
        """Ensure the package contains the correct top-level objects."""
        # DNA Center API Wrapper
        assert hasattr(dnacentersdk, "DNACenterAPI")

        # Exceptions
        assert hasattr(dnacentersdk, "AccessTokenError")
        assert hasattr(dnacentersdk, "ApiError")
        assert hasattr(dnacentersdk, "dnacentersdkException")
        assert hasattr(dnacentersdk, "DownloadFailure")
        assert hasattr(dnacentersdk, "MalformedRequest")
        assert hasattr(dnacentersdk, "RateLimitError")
        assert hasattr(dnacentersdk, "RateLimitWarning")
        assert hasattr(dnacentersdk, "VersionError")

        # Data Models
        assert hasattr(dnacentersdk, "mydict_data_factory")

    @pytest.mark.dnacentersdk
    def test_default_base_url(self, api, base_url):
        assert api.base_url == base_url

    @pytest.mark.dnacentersdk
    def test_custom_base_url(self):
        custom_url = "https://custom.domain.com/v1/"
        with pytest.raises((dnacentersdk.exceptions.ApiError, requests.exceptions.RequestException)):
            dnacentersdk.DNACenterAPI(username=DNA_CENTER_USERNAME,
                                      password=DNA_CENTER_PASSWORD,
                                      encoded_auth=DNA_CENTER_ENCODED_AUTH,
                                      base_url=custom_url,
                                      verify=DEFAULT_VERIFY,
                                      version=DNA_CENTER_VERSION)

    @pytest.mark.dnacentersdk
    def test_default_single_request_timeout(self, api):
        assert api.single_request_timeout == \
            DEFAULT_SINGLE_REQUEST_TIMEOUT

    @pytest.mark.dnacentersdk
    def test_custom_single_request_timeout(self, base_url):
        custom_timeout = 10
        connection_object = dnacentersdk.DNACenterAPI(username=DNA_CENTER_USERNAME,
                                                      password=DNA_CENTER_PASSWORD,
                                                      encoded_auth=DNA_CENTER_ENCODED_AUTH,
                                                      base_url=base_url,
                                                      single_request_timeout=custom_timeout,
                                                      verify=DEFAULT_VERIFY,
                                                      version=DNA_CENTER_VERSION)
        assert connection_object.single_request_timeout == custom_timeout

    @pytest.mark.dnacentersdk
    def test_default_wait_on_rate_limit(self, api):
        assert api.wait_on_rate_limit == \
            DEFAULT_WAIT_ON_RATE_LIMIT

    @pytest.mark.dnacentersdk
    def test_non_default_wait_on_rate_limit(self, base_url):
        connection_object = dnacentersdk.DNACenterAPI(username=DNA_CENTER_USERNAME,
                                                      password=DNA_CENTER_PASSWORD,
                                                      encoded_auth=DNA_CENTER_ENCODED_AUTH,
                                                      base_url=base_url,
                                                      wait_on_rate_limit=not DEFAULT_WAIT_ON_RATE_LIMIT,
                                                      verify=DEFAULT_VERIFY,
                                                      version=DNA_CENTER_VERSION)
        assert connection_object.wait_on_rate_limit != \
            DEFAULT_WAIT_ON_RATE_LIMIT

    @pytest.mark.dnacentersdk
    def test_api_object_creation(self, api):
        assert isinstance(api.authentication, Authentication)
        assert isinstance(api.custom_caller, CustomCaller)
        if api.version == '1.2.10':
            assert isinstance(api.clients, Clients_v1_2_10)
            assert isinstance(api.command_runner, CommandRunner_v1_2_10)
            assert isinstance(api.devices, Devices_v1_2_10)
            assert isinstance(api.fabric_wired, FabricWired_v1_2_10)
            assert isinstance(api.file, File_v1_2_10)
            assert isinstance(api.network_discovery, NetworkDiscovery_v1_2_10)
            assert isinstance(api.networks, Networks_v1_2_10)
            assert isinstance(api.non_fabric_wireless, NonFabricWireless_v1_2_10)
            assert isinstance(api.path_trace, PathTrace_v1_2_10)
            assert isinstance(api.pnp, Pnp_v1_2_10)
            assert isinstance(api.swim, Swim_v1_2_10)
            assert isinstance(api.site_profile, SiteProfile_v1_2_10)
            assert isinstance(api.sites, Sites_v1_2_10)
            assert isinstance(api.tag, Tag_v1_2_10)
            assert isinstance(api.task, Task_v1_2_10)
            assert isinstance(api.template_programmer, TemplateProgrammer_v1_2_10)
        if api.version == '1.3.0':
            assert isinstance(api.clients, Clients_v1_3_0)
            assert isinstance(api.command_runner, CommandRunner_v1_3_0)
            assert isinstance(api.devices, Devices_v1_3_0)
            assert isinstance(api.fabric_wired, FabricWired_v1_3_0)
            assert isinstance(api.file, File_v1_3_0)
            assert isinstance(api.network_discovery, NetworkDiscovery_v1_3_0)
            assert isinstance(api.networks, Networks_v1_3_0)
            assert isinstance(api.non_fabric_wireless, NonFabricWireless_v1_3_0)
            assert isinstance(api.path_trace, PathTrace_v1_3_0)
            assert isinstance(api.pnp, Pnp_v1_3_0)
            assert isinstance(api.swim, Swim_v1_3_0)
            assert isinstance(api.site_profile, SiteProfile_v1_3_0)
            assert isinstance(api.sites, Sites_v1_3_0)
            assert isinstance(api.tag, Tag_v1_3_0)
            assert isinstance(api.task, Task_v1_3_0)
            assert isinstance(api.template_programmer, TemplateProgrammer_v1_3_0)
        if api.version == '1.3.1':
            assert isinstance(api.application_policy, ApplicationPolicy_v1_3_1)
            assert isinstance(api.clients, Clients_v1_3_1)
            assert isinstance(api.command_runner, CommandRunner_v1_3_1)
            assert isinstance(api.configuration_templates, ConfigurationTemplates_v1_3_1)
            assert isinstance(api.device_onboarding_pnp, DeviceOnboardingPnp_v1_3_1)
            assert isinstance(api.devices, Devices_v1_3_1)
            assert isinstance(api.event_management, EventManagement_v1_3_1)
            assert isinstance(api.fabric_wired, FabricWired_v1_3_1)
            assert isinstance(api.file, File_v1_3_1)
            assert isinstance(api.issues, Issues_v1_3_1)
            assert isinstance(api.network_discovery, NetworkDiscovery_v1_3_1)
            assert isinstance(api.network_settings, NetworkSettings_v1_3_1)
            assert isinstance(api.non_fabric_wireless, NonFabricWireless_v1_3_1)
            assert isinstance(api.path_trace, PathTrace_v1_3_1)
            assert isinstance(api.site_design, SiteDesign_v1_3_1)
            assert isinstance(api.sites, Sites_v1_3_1)
            assert isinstance(api.software_image_management_swim, SoftwareImageManagementSwim_v1_3_1)
            assert isinstance(api.tag, Tag_v1_3_1)
            assert isinstance(api.task, Task_v1_3_1)
            assert isinstance(api.topology, Topology_v1_3_1)
            assert isinstance(api.users, Users_v1_3_1)
        if api.version == '1.3.3':
            assert isinstance(api.application_policy, ApplicationPolicy_v1_3_3)
            assert isinstance(api.clients, Clients_v1_3_3)
            assert isinstance(api.command_runner, CommandRunner_v1_3_3)
            assert isinstance(api.configuration_templates, ConfigurationTemplates_v1_3_3)
            assert isinstance(api.device_onboarding_pnp, DeviceOnboardingPnp_v1_3_3)
            assert isinstance(api.devices, Devices_v1_3_3)
            assert isinstance(api.discovery, Discovery_v1_3_3)
            assert isinstance(api.event_management, EventManagement_v1_3_3)
            assert isinstance(api.file, File_v1_3_3)
            assert isinstance(api.issues, Issues_v1_3_3)
            assert isinstance(api.network_settings, NetworkSettings_v1_3_3)
            assert isinstance(api.path_trace, PathTrace_v1_3_3)
            assert isinstance(api.sda, Sda_v1_3_3)
            assert isinstance(api.site_design, SiteDesign_v1_3_3)
            assert isinstance(api.sites, Sites_v1_3_3)
            assert isinstance(api.software_image_management_swim, SoftwareImageManagementSwim_v1_3_3)
            assert isinstance(api.tag, Tag_v1_3_3)
            assert isinstance(api.task, Task_v1_3_3)
            assert isinstance(api.topology, Topology_v1_3_3)
            assert isinstance(api.users, Users_v1_3_3)
            assert isinstance(api.wireless, Wireless_v1_3_3)
        if api.version == '2.1.1':
            assert isinstance(api.application_policy, ApplicationPolicy_v2_1_1)
            assert isinstance(api.clients, Clients_v2_1_1)
            assert isinstance(api.command_runner, CommandRunner_v2_1_1)
            assert isinstance(api.configuration_templates, ConfigurationTemplates_v2_1_1)
            assert isinstance(api.device_onboarding_pnp, DeviceOnboardingPnp_v2_1_1)
            assert isinstance(api.device_replacement, DeviceReplacement_v2_1_1)
            assert isinstance(api.devices, Devices_v2_1_1)
            assert isinstance(api.discovery, Discovery_v2_1_1)
            assert isinstance(api.event_management, EventManagement_v2_1_1)
            assert isinstance(api.file, File_v2_1_1)
            assert isinstance(api.itsm, Itsm_v2_1_1)
            assert isinstance(api.issues, Issues_v2_1_1)
            assert isinstance(api.network_settings, NetworkSettings_v2_1_1)
            assert isinstance(api.path_trace, PathTrace_v2_1_1)
            assert isinstance(api.sda, Sda_v2_1_1)
            assert isinstance(api.site_design, SiteDesign_v2_1_1)
            assert isinstance(api.sites, Sites_v2_1_1)
            assert isinstance(api.software_image_management_swim, SoftwareImageManagementSwim_v2_1_1)
            assert isinstance(api.tag, Tag_v2_1_1)
            assert isinstance(api.task, Task_v2_1_1)
            assert isinstance(api.topology, Topology_v2_1_1)
            assert isinstance(api.users, Users_v2_1_1)
            assert isinstance(api.wireless, Wireless_v2_1_1)
        if api.version == '2.1.2':
            assert isinstance(api.application_policy, ApplicationPolicy_v2_1_2)
            assert isinstance(api.applications, Applications_v2_1_2)
            assert isinstance(api.clients, Clients_v2_1_2)
            assert isinstance(api.command_runner, CommandRunner_v2_1_2)
            assert isinstance(api.configuration_archive, ConfigurationArchive_v2_1_2)
            assert isinstance(api.configuration_templates, ConfigurationTemplates_v2_1_2)
            assert isinstance(api.device_onboarding_pnp, DeviceOnboardingPnp_v2_1_2)
            assert isinstance(api.device_replacement, DeviceReplacement_v2_1_2)
            assert isinstance(api.devices, Devices_v2_1_2)
            assert isinstance(api.discovery, Discovery_v2_1_2)
            assert isinstance(api.event_management, EventManagement_v2_1_2)
            assert isinstance(api.file, File_v2_1_2)
            assert isinstance(api.itsm, Itsm_v2_1_2)
            assert isinstance(api.issues, Issues_v2_1_2)
            assert isinstance(api.network_settings, NetworkSettings_v2_1_2)
            assert isinstance(api.path_trace, PathTrace_v2_1_2)
            assert isinstance(api.sda, Sda_v2_1_2)
            assert isinstance(api.sensors, Sensors_v2_1_2)
            assert isinstance(api.site_design, SiteDesign_v2_1_2)
            assert isinstance(api.sites, Sites_v2_1_2)
            assert isinstance(api.software_image_management_swim, SoftwareImageManagementSwim_v2_1_2)
            assert isinstance(api.tag, Tag_v2_1_2)
            assert isinstance(api.task, Task_v2_1_2)
            assert isinstance(api.topology, Topology_v2_1_2)
            assert isinstance(api.users, Users_v2_1_2)
            assert isinstance(api.wireless, Wireless_v2_1_2)
        if api.version == '2.2.1':
            assert isinstance(api.application_policy, ApplicationPolicy_v2_2_1)
            assert isinstance(api.applications, Applications_v2_2_1)
            assert isinstance(api.clients, Clients_v2_2_1)
            assert isinstance(api.command_runner, CommandRunner_v2_2_1)
            assert isinstance(api.compliance, Compliance_v2_2_1)
            assert isinstance(api.configuration_archive, ConfigurationArchive_v2_2_1)
            assert isinstance(api.configuration_templates, ConfigurationTemplates_v2_2_1)
            assert isinstance(api.device_onboarding_pnp, DeviceOnboardingPnp_v2_2_1)
            assert isinstance(api.device_replacement, DeviceReplacement_v2_2_1)
            assert isinstance(api.devices, Devices_v2_2_1)
            assert isinstance(api.discovery, Discovery_v2_2_1)
            assert isinstance(api.event_management, EventManagement_v2_2_1)
            assert isinstance(api.file, File_v2_2_1)
            assert isinstance(api.itsm, Itsm_v2_2_1)
            assert isinstance(api.issues, Issues_v2_2_1)
            assert isinstance(api.network_settings, NetworkSettings_v2_2_1)
            assert isinstance(api.path_trace, PathTrace_v2_2_1)
            assert isinstance(api.reports, Reports_v2_2_1)
            assert isinstance(api.sda, Sda_v2_2_1)
            assert isinstance(api.security_advisories, SecurityAdvisories_v2_2_1)
            assert isinstance(api.sensors, Sensors_v2_2_1)
            assert isinstance(api.site_design, SiteDesign_v2_2_1)
            assert isinstance(api.sites, Sites_v2_2_1)
            assert isinstance(api.software_image_management_swim, SoftwareImageManagementSwim_v2_2_1)
            assert isinstance(api.tag, Tag_v2_2_1)
            assert isinstance(api.task, Task_v2_2_1)
            assert isinstance(api.topology, Topology_v2_2_1)
            assert isinstance(api.users, Users_v2_2_1)
            assert isinstance(api.wireless, Wireless_v2_2_1)
        if api.version == '2.2.2.3':
            assert isinstance(api.application_policy, ApplicationPolicy_v2_2_2_3)
            assert isinstance(api.applications, Applications_v2_2_2_3)
            assert isinstance(api.authentication_management, AuthenticationManagement_v2_2_2_3)
            assert isinstance(api.clients, Clients_v2_2_2_3)
            assert isinstance(api.command_runner, CommandRunner_v2_2_2_3)
            assert isinstance(api.compliance, Compliance_v2_2_2_3)
            assert isinstance(api.configuration_archive, ConfigurationArchive_v2_2_2_3)
            assert isinstance(api.configuration_templates, ConfigurationTemplates_v2_2_2_3)
            assert isinstance(api.device_onboarding_pnp, DeviceOnboardingPnp_v2_2_2_3)
            assert isinstance(api.device_replacement, DeviceReplacement_v2_2_2_3)
            assert isinstance(api.devices, Devices_v2_2_2_3)
            assert isinstance(api.discovery, Discovery_v2_2_2_3)
            assert isinstance(api.event_management, EventManagement_v2_2_2_3)
            assert isinstance(api.file, File_v2_2_2_3)
            assert isinstance(api.health_and_performance, HealthAndPerformance_v2_2_2_3)
            assert isinstance(api.itsm, Itsm_v2_2_2_3)
            assert isinstance(api.issues, Issues_v2_2_2_3)
            assert isinstance(api.licenses, Licenses_v2_2_2_3)
            assert isinstance(api.network_settings, NetworkSettings_v2_2_2_3)
            assert isinstance(api.path_trace, PathTrace_v2_2_2_3)
            assert isinstance(api.platform_configuration, PlatformConfiguration_v2_2_2_3)
            assert isinstance(api.reports, Reports_v2_2_2_3)
            assert isinstance(api.sda, Sda_v2_2_2_3)
            assert isinstance(api.security_advisories, SecurityAdvisories_v2_2_2_3)
            assert isinstance(api.sensors, Sensors_v2_2_2_3)
            assert isinstance(api.site_design, SiteDesign_v2_2_2_3)
            assert isinstance(api.sites, Sites_v2_2_2_3)
            assert isinstance(api.software_image_management_swim, SoftwareImageManagementSwim_v2_2_2_3)
            assert isinstance(api.tag, Tag_v2_2_2_3)
            assert isinstance(api.task, Task_v2_2_2_3)
            assert isinstance(api.topology, Topology_v2_2_2_3)
            assert isinstance(api.users, Users_v2_2_2_3)
            assert isinstance(api.wireless, Wireless_v2_2_2_3)
        if api.version == '2.2.3.3':
            assert isinstance(api.application_policy, ApplicationPolicy_v2_2_3_3)
            assert isinstance(api.applications, Applications_v2_2_3_3)
            assert isinstance(api.authentication_management, AuthenticationManagement_v2_2_3_3)
            assert isinstance(api.clients, Clients_v2_2_3_3)
            assert isinstance(api.command_runner, CommandRunner_v2_2_3_3)
            assert isinstance(api.compliance, Compliance_v2_2_3_3)
            assert isinstance(api.configuration_archive, ConfigurationArchive_v2_2_3_3)
            assert isinstance(api.configuration_templates, ConfigurationTemplates_v2_2_3_3)
            assert isinstance(api.device_onboarding_pnp, DeviceOnboardingPnp_v2_2_3_3)
            assert isinstance(api.device_replacement, DeviceReplacement_v2_2_3_3)
            assert isinstance(api.devices, Devices_v2_2_3_3)
            assert isinstance(api.disaster_recovery, DisasterRecovery_v2_2_3_3)
            assert isinstance(api.discovery, Discovery_v2_2_3_3)
            assert isinstance(api.event_management, EventManagement_v2_2_3_3)
            assert isinstance(api.fabric_wireless, FabricWireless_v2_2_3_3)
            assert isinstance(api.file, File_v2_2_3_3)
            assert isinstance(api.health_and_performance, HealthAndPerformance_v2_2_3_3)
            assert isinstance(api.itsm, Itsm_v2_2_3_3)
            assert isinstance(api.issues, Issues_v2_2_3_3)
            assert isinstance(api.licenses, Licenses_v2_2_3_3)
            assert isinstance(api.network_settings, NetworkSettings_v2_2_3_3)
            assert isinstance(api.path_trace, PathTrace_v2_2_3_3)
            assert isinstance(api.platform_configuration, PlatformConfiguration_v2_2_3_3)
            assert isinstance(api.policy, Policy_v2_2_3_3)
            assert isinstance(api.reports, Reports_v2_2_3_3)
            assert isinstance(api.sda, Sda_v2_2_3_3)
            assert isinstance(api.security_advisories, SecurityAdvisories_v2_2_3_3)
            assert isinstance(api.sensors, Sensors_v2_2_3_3)
            assert isinstance(api.site_design, SiteDesign_v2_2_3_3)
            assert isinstance(api.sites, Sites_v2_2_3_3)
            assert isinstance(api.software_image_management_swim, SoftwareImageManagementSwim_v2_2_3_3)
            assert isinstance(api.tag, Tag_v2_2_3_3)
            assert isinstance(api.task, Task_v2_2_3_3)
            assert isinstance(api.topology, Topology_v2_2_3_3)
            assert isinstance(api.users, Users_v2_2_3_3)
            assert isinstance(api.wireless, Wireless_v2_2_3_3)
        if api.version == '2.3.3.0':
            assert isinstance(api.application_policy, ApplicationPolicy_v2_3_3_0)
            assert isinstance(api.applications, Applications_v2_3_3_0)
            assert isinstance(api.cisco_dna_center_system, CiscoDnaCenterSystem_v2_3_3_0)
            assert isinstance(api.clients, Clients_v2_3_3_0)
            assert isinstance(api.command_runner, CommandRunner_v2_3_3_0)
            assert isinstance(api.compliance, Compliance_v2_3_3_0)
            assert isinstance(api.configuration_archive, ConfigurationArchive_v2_3_3_0)
            assert isinstance(api.configuration_templates, ConfigurationTemplates_v2_3_3_0)
            assert isinstance(api.device_onboarding_pnp, DeviceOnboardingPnp_v2_3_3_0)
            assert isinstance(api.device_replacement, DeviceReplacement_v2_3_3_0)
            assert isinstance(api.devices, Devices_v2_3_3_0)
            assert isinstance(api.discovery, Discovery_v2_3_3_0)
            assert isinstance(api.event_management, EventManagement_v2_3_3_0)
            assert isinstance(api.fabric_wireless, FabricWireless_v2_3_3_0)
            assert isinstance(api.file, File_v2_3_3_0)
            assert isinstance(api.health_and_performance, HealthAndPerformance_v2_3_3_0)
            assert isinstance(api.itsm, Itsm_v2_3_3_0)
            assert isinstance(api.issues, Issues_v2_3_3_0)
            assert isinstance(api.lan_automation, LanAutomation_v2_3_3_0)
            assert isinstance(api.licenses, Licenses_v2_3_3_0)
            assert isinstance(api.network_settings, NetworkSettings_v2_3_3_0)
            assert isinstance(api.path_trace, PathTrace_v2_3_3_0)
            assert isinstance(api.platform_configuration, PlatformConfiguration_v2_3_3_0)
            assert isinstance(api.reports, Reports_v2_3_3_0)
            assert isinstance(api.sda, Sda_v2_3_3_0)
            assert isinstance(api.security_advisories, SecurityAdvisories_v2_3_3_0)
            assert isinstance(api.sensors, Sensors_v2_3_3_0)
            assert isinstance(api.site_design, SiteDesign_v2_3_3_0)
            assert isinstance(api.sites, Sites_v2_3_3_0)
            assert isinstance(api.software_image_management_swim, SoftwareImageManagementSwim_v2_3_3_0)
            assert isinstance(api.system_settings, SystemSettings_v2_3_3_0)
            assert isinstance(api.tag, Tag_v2_3_3_0)
            assert isinstance(api.task, Task_v2_3_3_0)
            assert isinstance(api.topology, Topology_v2_3_3_0)
            assert isinstance(api.users, Users_v2_3_3_0)
            assert isinstance(api.wireless, Wireless_v2_3_3_0)
        if api.version == '2.3.5.3':
            assert isinstance(api.application_policy, ApplicationPolicy_v2_3_5_3)
            assert isinstance(api.applications, Applications_v2_3_5_3)
            assert isinstance(api.authentication_management, AuthenticationManagement_v2_3_5_3)
            assert isinstance(api.cisco_dna_center_system, CiscoDnaCenterSystem_v2_3_5_3)
            assert isinstance(api.clients, Clients_v2_3_5_3)
            assert isinstance(api.command_runner, CommandRunner_v2_3_5_3)
            assert isinstance(api.compliance, Compliance_v2_3_5_3)
            assert isinstance(api.configuration_archive, ConfigurationArchive_v2_3_5_3)
            assert isinstance(api.configuration_templates, ConfigurationTemplates_v2_3_5_3)
            assert isinstance(api.device_onboarding_pnp, DeviceOnboardingPnp_v2_3_5_3)
            assert isinstance(api.device_replacement, DeviceReplacement_v2_3_5_3)
            assert isinstance(api.devices, Devices_v2_3_5_3)
            assert isinstance(api.discovery, Discovery_v2_3_5_3)
            assert isinstance(api.eo_x, EoX_v2_3_5_3)
            assert isinstance(api.event_management, EventManagement_v2_3_5_3)
            assert isinstance(api.fabric_wireless, FabricWireless_v2_3_5_3)
            assert isinstance(api.file, File_v2_3_5_3)
            assert isinstance(api.health_and_performance, HealthAndPerformance_v2_3_5_3)
            assert isinstance(api.itsm, Itsm_v2_3_5_3)
            assert isinstance(api.itsm_integration, ItsmIntegration_v2_3_5_3)
            assert isinstance(api.issues, Issues_v2_3_5_3)
            assert isinstance(api.lan_automation, LanAutomation_v2_3_5_3)
            assert isinstance(api.licenses, Licenses_v2_3_5_3)
            assert isinstance(api.network_settings, NetworkSettings_v2_3_5_3)
            assert isinstance(api.path_trace, PathTrace_v2_3_5_3)
            assert isinstance(api.platform, Platform_v2_3_5_3)
            assert isinstance(api.reports, Reports_v2_3_5_3)
            assert isinstance(api.sda, Sda_v2_3_5_3)
            assert isinstance(api.security_advisories, SecurityAdvisories_v2_3_5_3)
            assert isinstance(api.sensors, Sensors_v2_3_5_3)
            assert isinstance(api.site_design, SiteDesign_v2_3_5_3)
            assert isinstance(api.sites, Sites_v2_3_5_3)
            assert isinstance(api.software_image_management_swim, SoftwareImageManagementSwim_v2_3_5_3)
            assert isinstance(api.system_settings, SystemSettings_v2_3_5_3)
            assert isinstance(api.tag, Tag_v2_3_5_3)
            assert isinstance(api.task, Task_v2_3_5_3)
            assert isinstance(api.topology, Topology_v2_3_5_3)
            assert isinstance(api.userand_roles, UserandRoles_v2_3_5_3)
            assert isinstance(api.users, Users_v2_3_5_3)
            assert isinstance(api.wireless, Wireless_v2_3_5_3)
