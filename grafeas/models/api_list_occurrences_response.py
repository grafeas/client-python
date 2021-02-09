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


class ApiListOccurrencesResponse(object):
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
        'occurrences': 'list[ApiOccurrence]',
        'next_page_token': 'str'
    }

    attribute_map = {
        'occurrences': 'occurrences',
        'next_page_token': 'next_page_token'
    }

    def __init__(self, occurrences=None, next_page_token=None):  # noqa: E501
        """ApiListOccurrencesResponse - a model defined in Swagger"""  # noqa: E501

        self._occurrences = None
        self._next_page_token = None
        self.discriminator = None

        if occurrences is not None:
            self.occurrences = occurrences
        if next_page_token is not None:
            self.next_page_token = next_page_token

    @property
    def occurrences(self):
        """Gets the occurrences of this ApiListOccurrencesResponse.  # noqa: E501

        The occurrences requested.  # noqa: E501

        :return: The occurrences of this ApiListOccurrencesResponse.  # noqa: E501
        :rtype: list[ApiOccurrence]
        """
        return self._occurrences

    @occurrences.setter
    def occurrences(self, occurrences):
        """Sets the occurrences of this ApiListOccurrencesResponse.

        The occurrences requested.  # noqa: E501

        :param occurrences: The occurrences of this ApiListOccurrencesResponse.  # noqa: E501
        :type: list[ApiOccurrence]
        """

        self._occurrences = occurrences

    @property
    def next_page_token(self):
        """Gets the next_page_token of this ApiListOccurrencesResponse.  # noqa: E501

        The next pagination token in the list response. It should be used as `page_token` for the following request. An empty value means no more results.  # noqa: E501

        :return: The next_page_token of this ApiListOccurrencesResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, next_page_token):
        """Sets the next_page_token of this ApiListOccurrencesResponse.

        The next pagination token in the list response. It should be used as `page_token` for the following request. An empty value means no more results.  # noqa: E501

        :param next_page_token: The next_page_token of this ApiListOccurrencesResponse.  # noqa: E501
        :type: str
        """

        self._next_page_token = next_page_token

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
        if issubclass(ApiListOccurrencesResponse, dict):
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
        if not isinstance(other, ApiListOccurrencesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other