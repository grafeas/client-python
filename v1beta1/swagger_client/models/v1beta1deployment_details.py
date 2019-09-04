# coding: utf-8

"""
    grafeas.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from swagger_client.models.deployment_deployment import DeploymentDeployment  # noqa: F401,E501


class V1beta1deploymentDetails(object):
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
        'deployment': 'DeploymentDeployment'
    }

    attribute_map = {
        'deployment': 'deployment'
    }

    def __init__(self, deployment=None):  # noqa: E501
        """V1beta1deploymentDetails - a model defined in Swagger"""  # noqa: E501
        self._deployment = None
        self.discriminator = None
        if deployment is not None:
            self.deployment = deployment

    @property
    def deployment(self):
        """Gets the deployment of this V1beta1deploymentDetails.  # noqa: E501


        :return: The deployment of this V1beta1deploymentDetails.  # noqa: E501
        :rtype: DeploymentDeployment
        """
        return self._deployment

    @deployment.setter
    def deployment(self, deployment):
        """Sets the deployment of this V1beta1deploymentDetails.


        :param deployment: The deployment of this V1beta1deploymentDetails.  # noqa: E501
        :type: DeploymentDeployment
        """

        self._deployment = deployment

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
        if issubclass(V1beta1deploymentDetails, dict):
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
        if not isinstance(other, V1beta1deploymentDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
