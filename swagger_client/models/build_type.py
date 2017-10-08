# coding: utf-8

"""
    Grafeas API

    An API to insert and retrieve annotations on cloud artifacts.

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class BuildType(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, builder_version=None, signature=None):
        """
        BuildType - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'builder_version': 'str',
            'signature': 'BuildSignature'
        }

        self.attribute_map = {
            'builder_version': 'builderVersion',
            'signature': 'signature'
        }

        self._builder_version = builder_version
        self._signature = signature

    @property
    def builder_version(self):
        """
        Gets the builder_version of this BuildType.
        Version of the builder which produced this Note.

        :return: The builder_version of this BuildType.
        :rtype: str
        """
        return self._builder_version

    @builder_version.setter
    def builder_version(self, builder_version):
        """
        Sets the builder_version of this BuildType.
        Version of the builder which produced this Note.

        :param builder_version: The builder_version of this BuildType.
        :type: str
        """

        self._builder_version = builder_version

    @property
    def signature(self):
        """
        Gets the signature of this BuildType.
        Signature of the build in Occurrences pointing to the Note containing this BuilderDetails.

        :return: The signature of this BuildType.
        :rtype: BuildSignature
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """
        Sets the signature of this BuildType.
        Signature of the build in Occurrences pointing to the Note containing this BuilderDetails.

        :param signature: The signature of this BuildType.
        :type: BuildSignature
        """

        self._signature = signature

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
