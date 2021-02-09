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


class ApiPackageManagerLocation(object):
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
        'cpe_uri': 'str',
        'version': 'VulnerabilityTypeVersion',
        'path': 'str'
    }

    attribute_map = {
        'cpe_uri': 'cpe_uri',
        'version': 'version',
        'path': 'path'
    }

    def __init__(self, cpe_uri=None, version=None, path=None):  # noqa: E501
        """ApiPackageManagerLocation - a model defined in Swagger"""  # noqa: E501

        self._cpe_uri = None
        self._version = None
        self._path = None
        self.discriminator = None

        if cpe_uri is not None:
            self.cpe_uri = cpe_uri
        if version is not None:
            self.version = version
        if path is not None:
            self.path = path

    @property
    def cpe_uri(self):
        """Gets the cpe_uri of this ApiPackageManagerLocation.  # noqa: E501

        The cpe_uri in [cpe format](https://cpe.mitre.org/specification/) denoting the package manager version distributing a package.  # noqa: E501

        :return: The cpe_uri of this ApiPackageManagerLocation.  # noqa: E501
        :rtype: str
        """
        return self._cpe_uri

    @cpe_uri.setter
    def cpe_uri(self, cpe_uri):
        """Sets the cpe_uri of this ApiPackageManagerLocation.

        The cpe_uri in [cpe format](https://cpe.mitre.org/specification/) denoting the package manager version distributing a package.  # noqa: E501

        :param cpe_uri: The cpe_uri of this ApiPackageManagerLocation.  # noqa: E501
        :type: str
        """

        self._cpe_uri = cpe_uri

    @property
    def version(self):
        """Gets the version of this ApiPackageManagerLocation.  # noqa: E501

        The version installed at this location.  # noqa: E501

        :return: The version of this ApiPackageManagerLocation.  # noqa: E501
        :rtype: VulnerabilityTypeVersion
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ApiPackageManagerLocation.

        The version installed at this location.  # noqa: E501

        :param version: The version of this ApiPackageManagerLocation.  # noqa: E501
        :type: VulnerabilityTypeVersion
        """

        self._version = version

    @property
    def path(self):
        """Gets the path of this ApiPackageManagerLocation.  # noqa: E501

        The path from which we gathered that this package/version is installed.  # noqa: E501

        :return: The path of this ApiPackageManagerLocation.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ApiPackageManagerLocation.

        The path from which we gathered that this package/version is installed.  # noqa: E501

        :param path: The path of this ApiPackageManagerLocation.  # noqa: E501
        :type: str
        """

        self._path = path

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
        if issubclass(ApiPackageManagerLocation, dict):
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
        if not isinstance(other, ApiPackageManagerLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other