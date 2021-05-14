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

class Layer3ExpansionValidationRequest(object):
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
        'hosts': 'list[Layer3ExpansionHostSpec]',
        'vcenter': 'Account',
        'skipped_validators': 'str',
        'segment_label': 'str'
    }

    attribute_map = {
        'hosts': 'hosts',
        'vcenter': 'vcenter',
        'skipped_validators': 'skipped_validators',
        'segment_label': 'segment_label'
    }

    def __init__(self, hosts=None, vcenter=None, skipped_validators=None, segment_label=None):  # noqa: E501
        """Layer3ExpansionValidationRequest - a model defined in Swagger"""  # noqa: E501
        self._hosts = None
        self._vcenter = None
        self._skipped_validators = None
        self._segment_label = None
        self.discriminator = None
        self.hosts = hosts
        self.vcenter = vcenter
        if skipped_validators is not None:
            self.skipped_validators = skipped_validators
        self.segment_label = segment_label

    @property
    def hosts(self):
        """Gets the hosts of this Layer3ExpansionValidationRequest.  # noqa: E501

        A list of the host information.  # noqa: E501

        :return: The hosts of this Layer3ExpansionValidationRequest.  # noqa: E501
        :rtype: list[Layer3ExpansionHostSpec]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this Layer3ExpansionValidationRequest.

        A list of the host information.  # noqa: E501

        :param hosts: The hosts of this Layer3ExpansionValidationRequest.  # noqa: E501
        :type: list[Layer3ExpansionHostSpec]
        """
        if hosts is None:
            raise ValueError("Invalid value for `hosts`, must not be `None`")  # noqa: E501

        self._hosts = hosts

    @property
    def vcenter(self):
        """Gets the vcenter of this Layer3ExpansionValidationRequest.  # noqa: E501


        :return: The vcenter of this Layer3ExpansionValidationRequest.  # noqa: E501
        :rtype: Account
        """
        return self._vcenter

    @vcenter.setter
    def vcenter(self, vcenter):
        """Sets the vcenter of this Layer3ExpansionValidationRequest.


        :param vcenter: The vcenter of this Layer3ExpansionValidationRequest.  # noqa: E501
        :type: Account
        """
        if vcenter is None:
            raise ValueError("Invalid value for `vcenter`, must not be `None`")  # noqa: E501

        self._vcenter = vcenter

    @property
    def skipped_validators(self):
        """Gets the skipped_validators of this Layer3ExpansionValidationRequest.  # noqa: E501


        :return: The skipped_validators of this Layer3ExpansionValidationRequest.  # noqa: E501
        :rtype: str
        """
        return self._skipped_validators

    @skipped_validators.setter
    def skipped_validators(self, skipped_validators):
        """Sets the skipped_validators of this Layer3ExpansionValidationRequest.


        :param skipped_validators: The skipped_validators of this Layer3ExpansionValidationRequest.  # noqa: E501
        :type: str
        """

        self._skipped_validators = skipped_validators

    @property
    def segment_label(self):
        """Gets the segment_label of this Layer3ExpansionValidationRequest.  # noqa: E501


        :return: The segment_label of this Layer3ExpansionValidationRequest.  # noqa: E501
        :rtype: str
        """
        return self._segment_label

    @segment_label.setter
    def segment_label(self, segment_label):
        """Sets the segment_label of this Layer3ExpansionValidationRequest.


        :param segment_label: The segment_label of this Layer3ExpansionValidationRequest.  # noqa: E501
        :type: str
        """
        if segment_label is None:
            raise ValueError("Invalid value for `segment_label`, must not be `None`")  # noqa: E501

        self._segment_label = segment_label

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
        if issubclass(Layer3ExpansionValidationRequest, dict):
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
        if not isinstance(other, Layer3ExpansionValidationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
