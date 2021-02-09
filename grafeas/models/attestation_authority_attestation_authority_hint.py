# coding: utf-8

"""
    An API to insert and retrieve metadata on cloud artifacts.

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1alpha1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AttestationAuthorityAttestationAuthorityHint(object):
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
        'human_readable_name': 'str'
    }

    attribute_map = {
        'human_readable_name': 'humanReadableName'
    }

    def __init__(self, human_readable_name=None):  # noqa: E501
        """AttestationAuthorityAttestationAuthorityHint - a model defined in Swagger"""  # noqa: E501

        self._human_readable_name = None
        self.discriminator = None

        if human_readable_name is not None:
            self.human_readable_name = human_readable_name

    @property
    def human_readable_name(self):
        """Gets the human_readable_name of this AttestationAuthorityAttestationAuthorityHint.  # noqa: E501

        The human readable name of this Attestation Authority, e.g. \"qa\".  # noqa: E501

        :return: The human_readable_name of this AttestationAuthorityAttestationAuthorityHint.  # noqa: E501
        :rtype: str
        """
        return self._human_readable_name

    @human_readable_name.setter
    def human_readable_name(self, human_readable_name):
        """Sets the human_readable_name of this AttestationAuthorityAttestationAuthorityHint.

        The human readable name of this Attestation Authority, e.g. \"qa\".  # noqa: E501

        :param human_readable_name: The human_readable_name of this AttestationAuthorityAttestationAuthorityHint.  # noqa: E501
        :type: str
        """

        self._human_readable_name = human_readable_name

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
        if issubclass(AttestationAuthorityAttestationAuthorityHint, dict):
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
        if not isinstance(other, AttestationAuthorityAttestationAuthorityHint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
