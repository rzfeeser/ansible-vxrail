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

class OptionsDGInfLayoutSepc(object):
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
        'slot': 'str',
        'bay': 'str',
        'type': 'str',
        'usage': 'str',
        'diskgroup': 'str'
    }

    attribute_map = {
        'slot': 'slot',
        'bay': 'bay',
        'type': 'type',
        'usage': 'usage',
        'diskgroup': 'diskgroup'
    }

    def __init__(self, slot=None, bay=None, type=None, usage=None, diskgroup=None):  # noqa: E501
        """OptionsDGInfLayoutSepc - a model defined in Swagger"""  # noqa: E501
        self._slot = None
        self._bay = None
        self._type = None
        self._usage = None
        self._diskgroup = None
        self.discriminator = None
        self.slot = slot
        self.bay = bay
        self.type = type
        self.usage = usage
        self.diskgroup = diskgroup

    @property
    def slot(self):
        """Gets the slot of this OptionsDGInfLayoutSepc.  # noqa: E501

        Disk group type of the host  # noqa: E501

        :return: The slot of this OptionsDGInfLayoutSepc.  # noqa: E501
        :rtype: str
        """
        return self._slot

    @slot.setter
    def slot(self, slot):
        """Sets the slot of this OptionsDGInfLayoutSepc.

        Disk group type of the host  # noqa: E501

        :param slot: The slot of this OptionsDGInfLayoutSepc.  # noqa: E501
        :type: str
        """
        if slot is None:
            raise ValueError("Invalid value for `slot`, must not be `None`")  # noqa: E501

        self._slot = slot

    @property
    def bay(self):
        """Gets the bay of this OptionsDGInfLayoutSepc.  # noqa: E501

        Disk group type of the host  # noqa: E501

        :return: The bay of this OptionsDGInfLayoutSepc.  # noqa: E501
        :rtype: str
        """
        return self._bay

    @bay.setter
    def bay(self, bay):
        """Sets the bay of this OptionsDGInfLayoutSepc.

        Disk group type of the host  # noqa: E501

        :param bay: The bay of this OptionsDGInfLayoutSepc.  # noqa: E501
        :type: str
        """
        if bay is None:
            raise ValueError("Invalid value for `bay`, must not be `None`")  # noqa: E501

        self._bay = bay

    @property
    def type(self):
        """Gets the type of this OptionsDGInfLayoutSepc.  # noqa: E501

        Disk group type of the host  # noqa: E501

        :return: The type of this OptionsDGInfLayoutSepc.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OptionsDGInfLayoutSepc.

        Disk group type of the host  # noqa: E501

        :param type: The type of this OptionsDGInfLayoutSepc.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def usage(self):
        """Gets the usage of this OptionsDGInfLayoutSepc.  # noqa: E501

        Disk group type of the host  # noqa: E501

        :return: The usage of this OptionsDGInfLayoutSepc.  # noqa: E501
        :rtype: str
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this OptionsDGInfLayoutSepc.

        Disk group type of the host  # noqa: E501

        :param usage: The usage of this OptionsDGInfLayoutSepc.  # noqa: E501
        :type: str
        """
        if usage is None:
            raise ValueError("Invalid value for `usage`, must not be `None`")  # noqa: E501

        self._usage = usage

    @property
    def diskgroup(self):
        """Gets the diskgroup of this OptionsDGInfLayoutSepc.  # noqa: E501

        Disk group type of the host  # noqa: E501

        :return: The diskgroup of this OptionsDGInfLayoutSepc.  # noqa: E501
        :rtype: str
        """
        return self._diskgroup

    @diskgroup.setter
    def diskgroup(self, diskgroup):
        """Sets the diskgroup of this OptionsDGInfLayoutSepc.

        Disk group type of the host  # noqa: E501

        :param diskgroup: The diskgroup of this OptionsDGInfLayoutSepc.  # noqa: E501
        :type: str
        """
        if diskgroup is None:
            raise ValueError("Invalid value for `diskgroup`, must not be `None`")  # noqa: E501

        self._diskgroup = diskgroup

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
        if issubclass(OptionsDGInfLayoutSepc, dict):
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
        if not isinstance(other, OptionsDGInfLayoutSepc):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
