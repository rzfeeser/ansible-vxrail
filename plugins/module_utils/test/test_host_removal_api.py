# coding: utf-8

"""
    VxRail Disk and Cluster Management

    APIs for disk and cluster management  # noqa: E501

    OpenAPI spec version: 7.0.240
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import vxrail_ansible_utility
from vxrail_ansible_utility.api.host_removal_api import HostRemovalApi  # noqa: E501
from vxrail_ansible_utility.rest import ApiException


class TestHostRemovalApi(unittest.TestCase):
    """HostRemovalApi unit test stubs"""

    def setUp(self):
        self.api = HostRemovalApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v1_cluster_remove_host_post(self):
        """Test case for v1_cluster_remove_host_post

        Removes a host from the cluster.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
