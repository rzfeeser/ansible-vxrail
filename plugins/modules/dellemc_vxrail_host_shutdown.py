#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved


# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_host_shutdown

short_description: Shuts down a specific VxRail Host

description:
- This module will shut down a specified host
options:

  vxmip:
    description:
      The IP address of the VxRail Manager System
    required: True
    type: str

  vcadmin:
    description:
      Administrative account of the vCenter Server the VxRail Manager is registered to
    required: True
    type: str

  vcpasswd:
    description:
      The password for the administrator account provided in vcadmin
    required: True
    type: str

  host_sn:
    description:
      The serial number for the host to shut down
    required: True
    type: str

  dryrun:
    description:
      Perform an optional dry run to check whether it is safe to shut down the host. The default value is false.
    required: false
    type: bool
    default: False

  evacuate_poweredoff_vms:
    description:
      Choose whether powered off vms should be evacuated off of the chosen host before shutdown. The default value is true.
    required: false
    type: bool
    default: True

  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: False
    type: int

  timeout:
    description:
      Time out value for cancelling the host shutdown, the default value is 60 seconds
    required: false
    type: int
    default: 1800

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Shut down a specific VxRail Host
    dellemc_vxrail_host_shutdown:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        host_sn: "{{ host_sn }}"
        dryrun: "{{ dryrun }}"
        evacuate_poweredoff_vms: "{{ evacuate_poweredoff_vms }}"
        timeout : "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"
'''

RETURN = r'''
Host_Shutdown_API:
  description: Returns the request ID and whether the operation was successful.
  returned: always
  type: dict
  sample: >-
        {
            "Request_ID": "8b7539c2-bcb8-48cf-897d-1f50ab39227f",
            "Request_Status": "COMPLETED"
        }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
import time
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

# Defining global variables
API = "/hosts/{sn}/shutdown"
MODULE = "dellemc_vxrail_host_shutdown"
LOG_FILE_PATH = "/tmp/vxrail_ansible_host_shutdown.log"

LOGGER = utils.get_logger(MODULE, LOG_FILE_PATH, log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class VxrailClusterUrls():
    cluster_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxrailClusterUrls.cluster_url.format(self.vxm_ip)


class VxRailCluster():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.timeout = module.params.get('timeout')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.host_sn = module.params.get('host_sn')
        self.dryrun_info = module.params.get('dryrun')
        self.evacuate_poweredoff_vms = module.params.get('evacuate_poweredoff_vms')
        self.api_version_number = module.params.get('api_version_number')
        self.system_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()
        # Added for auto-version detection
        self.api_version_string = "v?"

    # Obtains the response for the given module path with specified api_version_number or highest found version
    def get_versioned_response(self, api_instance, module_path):
        # Set api version string and version number if undefined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path, LOGGER)

        # Calls versioned method as attribute (ex: v1_hosts_sn_shutdown_post)
        call_string = self.api_version_string + '_hosts_sn_shutdown_post'
        LOGGER.info("Using utility method: %s\n", call_string)
        api_host_shutdown_post = getattr(api_instance, call_string)
        host_shutdown_json = {}
        host_shutdown_json['dryrun'] = self.dryrun_info
        host_shutdown_json['evacuate_poweredoff_vms'] = self.evacuate_poweredoff_vms
        return api_host_shutdown_post(body=host_shutdown_json, sn=self.host_sn)

    def post_host_shutdown(self):
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.HostInformationApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # start host shutdown
            response = self.get_versioned_response(api_instance, "POST /hosts/{sn}/shutdown")
        except ApiException as e:
            LOGGER.error("Exception when calling HostInformationApi->%s_host_sn_shutdown_post: %s\n", self.api_version_string, e)
            return 'error'
        requestid = response.request_id
        return requestid


def main():
    ''' Entry point into execution flow '''
    result_request_id = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        host_sn=dict(required=True),
        dryrun=dict(type='bool', required=False, default='False'),
        evacuate_poweredoff_vms=dict(type='bool', required=False, default='True'),
        api_version_number=dict(type='int', required=False),
        timeout=dict(type='int', default=1800)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result_request_id = VxRailCluster().post_host_shutdown()
    if result_request_id == 'error':
        module.fail_json(msg=f"Call {API} API failed,please see log file {LOG_FILE_PATH} for more error details.")
    LOGGER.info('Host Shutdown request_id: %s.', result_request_id)
    dryrun = module.params.get('dryrun')
    evac_off_vms = module.params.get('evacuate_poweredoff_vms')
    vxmip = module.params.get('vxmip')
    vcadmin = module.params.get('vcadmin')
    vcpasswd = module.params.get('vcpasswd')
    LOGGER.info('Host Shutdown dryrun: %s.', dryrun)
    LOGGER.info('Evacuate Poweredoff VMs: %s.', evac_off_vms)
    task_state = 0
    time_out = 0
    initial_timeout = module.params.get('timeout')
    LOGGER.info('Timeout setting: %s seconds.', initial_timeout)
    # Check call to v1/requests/{request_id}
    result_response = utils.get_request_status(vxm_ip=vxmip, vcadmin=vcadmin, vcpasswd=vcpasswd, logger=LOGGER, request_id=result_request_id)
    if result_response == 'error':
        module.fail_json(msg="Call v1/requests/request_id API failed,please see "
                             "log file /tmp/vxrail_ansible_host_shutdown.log for more error details.")
    else:
        LOGGER.info('No issues found in call to v1/requests/request_id API. Begin checking status of host shutdown operation.')
    while task_state not in ('COMPLETED', 'FAILED') and time_out < initial_timeout:
        result_response = utils.get_request_status(vxm_ip=vxmip, vcadmin=vcadmin, vcpasswd=vcpasswd, logger=LOGGER, request_id=result_request_id)
        task_state = result_response.state
        LOGGER.info('Request_status: %s', task_state)
        ''' call frequently to capture 'COMPLETED' status before host shut down'''
        time_out = time_out + 1
        time.sleep(1)
    error_message = result_response.error
    if task_state == 'COMPLETED' and not error_message:
        vx_facts = {'Request_ID': result_request_id, 'Request_Status': task_state}
        if dryrun:
            LOGGER.info("Host Shutdown Dryrun Completed")
            vx_facts_result = dict(changed=False, Host_Shutdown_API=vx_facts, msg="Host Shutdown Dryrun has completed. Please see the "
                                                                                  "logs at /tmp/vxrail_ansible_host_shutdown.log for more details")
        else:
            LOGGER.info("Host Shutdown Completed")
            vx_facts_result = dict(changed=True, Host_Shutdown_API=vx_facts, msg="Host Shutdown has completed. Please see the "
                                                                                 "logs at /tmp/vxrail_ansible_host_shutdown.log for more details")
    else:
        LOGGER.info("Host Shutdown or Dryrun has Failed")
        vx_facts = {'Request_ID': result_request_id}
        vx_facts_result = dict(failed=True, Host_Shutdown_API=vx_facts, msg="Please see the /tmp/vxrail_ansible_host_shutdown.log for more details")
    LOGGER.info('Request_info: %s', result_response)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
