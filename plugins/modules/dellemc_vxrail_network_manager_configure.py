#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved


# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_network_manager_configure

short_description: Configures the VxRail Manager IP address

description:
- This module will change the VxRail Manager IP prior to cluster build.
options:

  vxmip:
    description:
      The IP address of the VxRail Manager System
    required: True
    type: str

  new_ip:
    description:
      The new IP address to assign to the VxRail manager
    required: True
    type: str

  gateway:
    description:
      The gateway IP for the new manager address
    required: True
    type: str

  netmask:
    description:
      The subnet mask for the new manager address
    required: True
    type: str

  new_ipv6:
    description:
      The new IPv6 address to assign to the VxRail manager
    required: True
    type: str

  gateway_ipv6:
    description:
      The gateway IPv6 for the new manager address
    required: True
    type: str

  prefix_length_ipv6:
    description:
      The prefix length for the new manager address
    required: True
    type: str

  vlan_id:
    description:
      The VLAN ID for the new manager address
    required: True
    type: str

  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: False
    type: int

  timeout:
    description:
      Time out value for setting VxRail IP information, the default value is 60 seconds
    required: false
    type: int
    default: 60

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Configure the VxRail Manager IP address
    dellemc_vxrail_network_manager_configure:
        vxmip: "{{ vxmip }}"
        new_ip: "{{ new_ip }}"
        gateway: "{{ gateway }}"
        netmask: "{{ netmask }}"
        new_ipv6: "{{ new_ipv6 }}"
        gateway_ipv6: "{{ gateway_ipv6 }}"
        prefix_length_ipv6: "{{ prefix_length_ipv6 }}"
        vlan_id: "{{ vlan_id }}"
        timeout: "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"
'''

RETURN = r'''
Network_Manager_Configure:
  description: This module will change the VxRail Manager IP prior to cluster build.
  returned: always
  type: dict
  sample: >-
    {
        "state": "PENDING",
        "message": "The request was sent successfully and it needs time to complete in background, please try new VxRail Manager IP after a minute or more."
    }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOG_FILE_PATH = "/tmp/vxrail_ansible_network_manager_configure.log"
LOGGER = utils.get_logger("dellemc_vxrail_network_manager_configure", LOG_FILE_PATH, log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class VxrailClusterUrls():

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return f"https://{self.vxm_ip}/rest/vxm"


class VxRailCluster():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.timeout = module.params.get('timeout')
        self.new_ip = module.params.get('new_ip')
        self.gateway = module.params.get('gateway')
        self.netmask = module.params.get('netmask')
        self.new_ipv6 = module.params.get('new_ipv6')
        self.gateway_ipv6 = module.params.get('gateway_ipv6')
        self.prefix_length_ipv6 = module.params.get('prefix_length_ipv6')
        self.vlan_id = module.params.get('vlan_id')
        self.api_version_number = module.params.get('api_version_number')

        self.system_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()
        self.api_version_string = "v?"

    def get_versioned_response(self, api_instance, module_path, manager_change_info):
        # Set api version string and version number if undefined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path,
                                                                   LOGGER)

        # Calls versioned method as attribute (ex: v1_network_vxm_post)
        call_string = self.api_version_string + '_network_vxm_post'
        LOGGER.info("Using utility method: %s\n", call_string)
        network_vxm_post = getattr(api_instance, call_string)
        return network_vxm_post(manager_change_info)

    def post_manager_ip(self):
        manager_return_info = {}
        manager_change_info = {
            "vlan_id": self.vlan_id
        }
        if self.new_ip:
            manager_change_info["ip"] = self.new_ip
        if self.gateway:
            manager_change_info["gateway"] = self.gateway
        if self.netmask:
            manager_change_info["netmask"] = self.netmask
        if self.new_ipv6:
            manager_change_info["ipv6"] = self.new_ipv6
        if self.gateway_ipv6:
            manager_change_info["gateway_ipv6"] = self.gateway_ipv6
        if self.prefix_length_ipv6:
            manager_change_info["prefix_length_ipv6"] = self.prefix_length_ipv6

        LOGGER.info("Sending Configuration: %s", manager_change_info)

        # create an instance of the API class
        api_instance = vxrail_ansible_utility.PreInstallationStaticIPApi(
            vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # post manager configuration
            response = self.get_versioned_response(api_instance, "POST /network/vxrail-manager", manager_change_info)
        except ApiException as e:
            LOGGER.error("Exception when calling PreInstallationStaticIPApi->%s_network_vxm_post: %s\n",
                         self.api_version_string, e)
            return 'error'
        LOGGER.info("%s/network/vxrail-manager POST api response: %s\n", self.api_version_string, response)
        data = response
        manager_return_info['message'] = data.message
        manager_return_info['state'] = data.state
        return dict(manager_return_info.items())


def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        new_ip=dict(required=False),
        gateway=dict(required=False),
        netmask=dict(required=False),
        new_ipv6=dict(required=False),
        gateway_ipv6=dict(required=False),
        prefix_length_ipv6=dict(type='int', required=False),
        vlan_id=dict(required=True, type='str'),
        api_version_number=dict(type='int'),
        timeout=dict(type='int', default=60)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
        required_if=([('api_version_number', 1, ['new_ip', 'gateway', 'netmask'])]),
    )
    result = VxRailCluster().post_manager_ip()
    if result == 'error':
        module.fail_json(
            msg=f"Call POST /network/vxrail-manager API failed,please see log file {LOG_FILE_PATH} for more error details.")
    vx_facts = {'Network_Manager_Configure': result}
    vx_facts_result = dict(changed=True, NETWORK_MANAGER_API=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
