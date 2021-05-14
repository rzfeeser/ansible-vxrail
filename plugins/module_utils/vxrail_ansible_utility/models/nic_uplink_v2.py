# coding: utf-8

"""
    VxRail Disk and Cluster Management

    APIs for disk and cluster management  # noqa: E501

    OpenAPI spec version: 7.0.240
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NicUplinkV2(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'vds_name': 'str',
        'name': 'str',
        'physical_nic': 'str'
    }

    attribute_map = {
        'vds_name': 'vds_name',
        'name': 'name',
        'physical_nic': 'physical_nic'
    }

    def __init__(self, vds_name=None, name=None, physical_nic=None):  # noqa: E501
        """NicUplinkV2 - a model defined in Swagger"""  # noqa: E501
        self._vds_name = None
        self._name = None
        self._physical_nic = None
        self.discriminator = None
        self.vds_name = vds_name
        self.name = name
        self.physical_nic = physical_nic

    @property
    def vds_name(self):
        """Gets the vds_name of this NicUplinkV2.  # noqa: E501

        Name of the VDS  # noqa: E501

        :return: The vds_name of this NicUplinkV2.  # noqa: E501
        :rtype: str
        """
        return self._vds_name

    @vds_name.setter
    def vds_name(self, vds_name):
        """Sets the vds_name of this NicUplinkV2.

        Name of the VDS  # noqa: E501

        :param vds_name: The vds_name of this NicUplinkV2.  # noqa: E501
        :type: str
        """
        if vds_name is None:
            raise ValueError("Invalid value for `vds_name`, must not be `None`")  # noqa: E501

        self._vds_name = vds_name

    @property
    def name(self):
        """Gets the name of this NicUplinkV2.  # noqa: E501

        Name of the uplink  # noqa: E501

        :return: The name of this NicUplinkV2.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NicUplinkV2.

        Name of the uplink  # noqa: E501

        :param name: The name of this NicUplinkV2.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def physical_nic(self):
        """Gets the physical_nic of this NicUplinkV2.  # noqa: E501

        Name of the physical NIC  # noqa: E501

        :return: The physical_nic of this NicUplinkV2.  # noqa: E501
        :rtype: str
        """
        return self._physical_nic

    @physical_nic.setter
    def physical_nic(self, physical_nic):
        """Sets the physical_nic of this NicUplinkV2.

        Name of the physical NIC  # noqa: E501

        :param physical_nic: The physical_nic of this NicUplinkV2.  # noqa: E501
        :type: str
        """
        if physical_nic is None:
            raise ValueError("Invalid value for `physical_nic`, must not be `None`")  # noqa: E501

        self._physical_nic = physical_nic

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(NicUplinkV2, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NicUplinkV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
