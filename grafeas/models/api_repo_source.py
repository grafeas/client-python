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


class ApiRepoSource(object):
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
        'project_id': 'str',
        'repo_name': 'str',
        'branch_name': 'str',
        'tag_name': 'str',
        'commit_sha': 'str'
    }

    attribute_map = {
        'project_id': 'projectId',
        'repo_name': 'repoName',
        'branch_name': 'branchName',
        'tag_name': 'tagName',
        'commit_sha': 'commitSha'
    }

    def __init__(self, project_id=None, repo_name=None, branch_name=None, tag_name=None, commit_sha=None):  # noqa: E501
        """ApiRepoSource - a model defined in Swagger"""  # noqa: E501

        self._project_id = None
        self._repo_name = None
        self._branch_name = None
        self._tag_name = None
        self._commit_sha = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if repo_name is not None:
            self.repo_name = repo_name
        if branch_name is not None:
            self.branch_name = branch_name
        if tag_name is not None:
            self.tag_name = tag_name
        if commit_sha is not None:
            self.commit_sha = commit_sha

    @property
    def project_id(self):
        """Gets the project_id of this ApiRepoSource.  # noqa: E501

        ID of the project that owns the repo.  # noqa: E501

        :return: The project_id of this ApiRepoSource.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ApiRepoSource.

        ID of the project that owns the repo.  # noqa: E501

        :param project_id: The project_id of this ApiRepoSource.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def repo_name(self):
        """Gets the repo_name of this ApiRepoSource.  # noqa: E501

        Name of the repo.  # noqa: E501

        :return: The repo_name of this ApiRepoSource.  # noqa: E501
        :rtype: str
        """
        return self._repo_name

    @repo_name.setter
    def repo_name(self, repo_name):
        """Sets the repo_name of this ApiRepoSource.

        Name of the repo.  # noqa: E501

        :param repo_name: The repo_name of this ApiRepoSource.  # noqa: E501
        :type: str
        """

        self._repo_name = repo_name

    @property
    def branch_name(self):
        """Gets the branch_name of this ApiRepoSource.  # noqa: E501

        Name of the branch to build.  # noqa: E501

        :return: The branch_name of this ApiRepoSource.  # noqa: E501
        :rtype: str
        """
        return self._branch_name

    @branch_name.setter
    def branch_name(self, branch_name):
        """Sets the branch_name of this ApiRepoSource.

        Name of the branch to build.  # noqa: E501

        :param branch_name: The branch_name of this ApiRepoSource.  # noqa: E501
        :type: str
        """

        self._branch_name = branch_name

    @property
    def tag_name(self):
        """Gets the tag_name of this ApiRepoSource.  # noqa: E501

        Name of the tag to build.  # noqa: E501

        :return: The tag_name of this ApiRepoSource.  # noqa: E501
        :rtype: str
        """
        return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name):
        """Sets the tag_name of this ApiRepoSource.

        Name of the tag to build.  # noqa: E501

        :param tag_name: The tag_name of this ApiRepoSource.  # noqa: E501
        :type: str
        """

        self._tag_name = tag_name

    @property
    def commit_sha(self):
        """Gets the commit_sha of this ApiRepoSource.  # noqa: E501

        Explicit commit SHA to build.  # noqa: E501

        :return: The commit_sha of this ApiRepoSource.  # noqa: E501
        :rtype: str
        """
        return self._commit_sha

    @commit_sha.setter
    def commit_sha(self, commit_sha):
        """Sets the commit_sha of this ApiRepoSource.

        Explicit commit SHA to build.  # noqa: E501

        :param commit_sha: The commit_sha of this ApiRepoSource.  # noqa: E501
        :type: str
        """

        self._commit_sha = commit_sha

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
        if issubclass(ApiRepoSource, dict):
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
        if not isinstance(other, ApiRepoSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
