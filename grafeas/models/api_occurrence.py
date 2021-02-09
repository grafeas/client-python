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


class ApiOccurrence(object):
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
        'name': 'str',
        'resource_url': 'str',
        'note_name': 'str',
        'kind': 'ApiNoteKind',
        'vulnerability_details': 'VulnerabilityTypeVulnerabilityDetails',
        'build_details': 'ApiBuildDetails',
        'derived_image_details': 'DockerImageDerivedDetails',
        'installation_details': 'PackageManagerInstallationDetails',
        'deployment_details': 'DeployableDeploymentDetails',
        'discovered_details': 'DiscoveryDiscoveredDetails',
        'attestation_details': 'AttestationAuthorityAttestationDetails',
        'remediation': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'operation_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'resource_url': 'resource_url',
        'note_name': 'note_name',
        'kind': 'kind',
        'vulnerability_details': 'vulnerability_details',
        'build_details': 'build_details',
        'derived_image_details': 'derived_image_details',
        'installation_details': 'installation_details',
        'deployment_details': 'deployment_details',
        'discovered_details': 'discovered_details',
        'attestation_details': 'attestation_details',
        'remediation': 'remediation',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'operation_name': 'operation_name'
    }

    def __init__(self, name=None, resource_url=None, note_name=None, kind=None, vulnerability_details=None, build_details=None, derived_image_details=None, installation_details=None, deployment_details=None, discovered_details=None, attestation_details=None, remediation=None, create_time=None, update_time=None, operation_name=None):  # noqa: E501
        """ApiOccurrence - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._resource_url = None
        self._note_name = None
        self._kind = None
        self._vulnerability_details = None
        self._build_details = None
        self._derived_image_details = None
        self._installation_details = None
        self._deployment_details = None
        self._discovered_details = None
        self._attestation_details = None
        self._remediation = None
        self._create_time = None
        self._update_time = None
        self._operation_name = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if resource_url is not None:
            self.resource_url = resource_url
        if note_name is not None:
            self.note_name = note_name
        if kind is not None:
            self.kind = kind
        if vulnerability_details is not None:
            self.vulnerability_details = vulnerability_details
        if build_details is not None:
            self.build_details = build_details
        if derived_image_details is not None:
            self.derived_image_details = derived_image_details
        if installation_details is not None:
            self.installation_details = installation_details
        if deployment_details is not None:
            self.deployment_details = deployment_details
        if discovered_details is not None:
            self.discovered_details = discovered_details
        if attestation_details is not None:
            self.attestation_details = attestation_details
        if remediation is not None:
            self.remediation = remediation
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if operation_name is not None:
            self.operation_name = operation_name

    @property
    def name(self):
        """Gets the name of this ApiOccurrence.  # noqa: E501


        :return: The name of this ApiOccurrence.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiOccurrence.


        :param name: The name of this ApiOccurrence.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def resource_url(self):
        """Gets the resource_url of this ApiOccurrence.  # noqa: E501

        The unique URL of the image or the container for which the `Occurrence` applies. For example, https://gcr.io/project/image@sha256:foo This field can be used as a filter in list requests.  # noqa: E501

        :return: The resource_url of this ApiOccurrence.  # noqa: E501
        :rtype: str
        """
        return self._resource_url

    @resource_url.setter
    def resource_url(self, resource_url):
        """Sets the resource_url of this ApiOccurrence.

        The unique URL of the image or the container for which the `Occurrence` applies. For example, https://gcr.io/project/image@sha256:foo This field can be used as a filter in list requests.  # noqa: E501

        :param resource_url: The resource_url of this ApiOccurrence.  # noqa: E501
        :type: str
        """

        self._resource_url = resource_url

    @property
    def note_name(self):
        """Gets the note_name of this ApiOccurrence.  # noqa: E501

        An analysis note associated with this image, in the form \"providers/{provider_id}/notes/{NOTE_ID}\" This field can be used as a filter in list requests.  # noqa: E501

        :return: The note_name of this ApiOccurrence.  # noqa: E501
        :rtype: str
        """
        return self._note_name

    @note_name.setter
    def note_name(self, note_name):
        """Sets the note_name of this ApiOccurrence.

        An analysis note associated with this image, in the form \"providers/{provider_id}/notes/{NOTE_ID}\" This field can be used as a filter in list requests.  # noqa: E501

        :param note_name: The note_name of this ApiOccurrence.  # noqa: E501
        :type: str
        """

        self._note_name = note_name

    @property
    def kind(self):
        """Gets the kind of this ApiOccurrence.  # noqa: E501

        Output only. This explicitly denotes which of the `Occurrence` details are specified. This field can be used as a filter in list requests.  # noqa: E501

        :return: The kind of this ApiOccurrence.  # noqa: E501
        :rtype: ApiNoteKind
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this ApiOccurrence.

        Output only. This explicitly denotes which of the `Occurrence` details are specified. This field can be used as a filter in list requests.  # noqa: E501

        :param kind: The kind of this ApiOccurrence.  # noqa: E501
        :type: ApiNoteKind
        """

        self._kind = kind

    @property
    def vulnerability_details(self):
        """Gets the vulnerability_details of this ApiOccurrence.  # noqa: E501

        Details of a security vulnerability note.  # noqa: E501

        :return: The vulnerability_details of this ApiOccurrence.  # noqa: E501
        :rtype: VulnerabilityTypeVulnerabilityDetails
        """
        return self._vulnerability_details

    @vulnerability_details.setter
    def vulnerability_details(self, vulnerability_details):
        """Sets the vulnerability_details of this ApiOccurrence.

        Details of a security vulnerability note.  # noqa: E501

        :param vulnerability_details: The vulnerability_details of this ApiOccurrence.  # noqa: E501
        :type: VulnerabilityTypeVulnerabilityDetails
        """

        self._vulnerability_details = vulnerability_details

    @property
    def build_details(self):
        """Gets the build_details of this ApiOccurrence.  # noqa: E501

        Build details for a verifiable build.  # noqa: E501

        :return: The build_details of this ApiOccurrence.  # noqa: E501
        :rtype: ApiBuildDetails
        """
        return self._build_details

    @build_details.setter
    def build_details(self, build_details):
        """Sets the build_details of this ApiOccurrence.

        Build details for a verifiable build.  # noqa: E501

        :param build_details: The build_details of this ApiOccurrence.  # noqa: E501
        :type: ApiBuildDetails
        """

        self._build_details = build_details

    @property
    def derived_image_details(self):
        """Gets the derived_image_details of this ApiOccurrence.  # noqa: E501

        Describes how this resource derives from the basis in the associated note.  # noqa: E501

        :return: The derived_image_details of this ApiOccurrence.  # noqa: E501
        :rtype: DockerImageDerivedDetails
        """
        return self._derived_image_details

    @derived_image_details.setter
    def derived_image_details(self, derived_image_details):
        """Sets the derived_image_details of this ApiOccurrence.

        Describes how this resource derives from the basis in the associated note.  # noqa: E501

        :param derived_image_details: The derived_image_details of this ApiOccurrence.  # noqa: E501
        :type: DockerImageDerivedDetails
        """

        self._derived_image_details = derived_image_details

    @property
    def installation_details(self):
        """Gets the installation_details of this ApiOccurrence.  # noqa: E501

        Describes the installation of a package on the linked resource.  # noqa: E501

        :return: The installation_details of this ApiOccurrence.  # noqa: E501
        :rtype: PackageManagerInstallationDetails
        """
        return self._installation_details

    @installation_details.setter
    def installation_details(self, installation_details):
        """Sets the installation_details of this ApiOccurrence.

        Describes the installation of a package on the linked resource.  # noqa: E501

        :param installation_details: The installation_details of this ApiOccurrence.  # noqa: E501
        :type: PackageManagerInstallationDetails
        """

        self._installation_details = installation_details

    @property
    def deployment_details(self):
        """Gets the deployment_details of this ApiOccurrence.  # noqa: E501

        Describes the deployment of an artifact on a runtime.  # noqa: E501

        :return: The deployment_details of this ApiOccurrence.  # noqa: E501
        :rtype: DeployableDeploymentDetails
        """
        return self._deployment_details

    @deployment_details.setter
    def deployment_details(self, deployment_details):
        """Sets the deployment_details of this ApiOccurrence.

        Describes the deployment of an artifact on a runtime.  # noqa: E501

        :param deployment_details: The deployment_details of this ApiOccurrence.  # noqa: E501
        :type: DeployableDeploymentDetails
        """

        self._deployment_details = deployment_details

    @property
    def discovered_details(self):
        """Gets the discovered_details of this ApiOccurrence.  # noqa: E501

        Describes the initial scan status for this resource.  # noqa: E501

        :return: The discovered_details of this ApiOccurrence.  # noqa: E501
        :rtype: DiscoveryDiscoveredDetails
        """
        return self._discovered_details

    @discovered_details.setter
    def discovered_details(self, discovered_details):
        """Sets the discovered_details of this ApiOccurrence.

        Describes the initial scan status for this resource.  # noqa: E501

        :param discovered_details: The discovered_details of this ApiOccurrence.  # noqa: E501
        :type: DiscoveryDiscoveredDetails
        """

        self._discovered_details = discovered_details

    @property
    def attestation_details(self):
        """Gets the attestation_details of this ApiOccurrence.  # noqa: E501

        Describes an attestation of an artifact.  # noqa: E501

        :return: The attestation_details of this ApiOccurrence.  # noqa: E501
        :rtype: AttestationAuthorityAttestationDetails
        """
        return self._attestation_details

    @attestation_details.setter
    def attestation_details(self, attestation_details):
        """Sets the attestation_details of this ApiOccurrence.

        Describes an attestation of an artifact.  # noqa: E501

        :param attestation_details: The attestation_details of this ApiOccurrence.  # noqa: E501
        :type: AttestationAuthorityAttestationDetails
        """

        self._attestation_details = attestation_details

    @property
    def remediation(self):
        """Gets the remediation of this ApiOccurrence.  # noqa: E501


        :return: The remediation of this ApiOccurrence.  # noqa: E501
        :rtype: str
        """
        return self._remediation

    @remediation.setter
    def remediation(self, remediation):
        """Sets the remediation of this ApiOccurrence.


        :param remediation: The remediation of this ApiOccurrence.  # noqa: E501
        :type: str
        """

        self._remediation = remediation

    @property
    def create_time(self):
        """Gets the create_time of this ApiOccurrence.  # noqa: E501

        Output only. The time this `Occurrence` was created.  # noqa: E501

        :return: The create_time of this ApiOccurrence.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ApiOccurrence.

        Output only. The time this `Occurrence` was created.  # noqa: E501

        :param create_time: The create_time of this ApiOccurrence.  # noqa: E501
        :type: datetime
        """

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ApiOccurrence.  # noqa: E501

        Output only. The time this `Occurrence` was last updated.  # noqa: E501

        :return: The update_time of this ApiOccurrence.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ApiOccurrence.

        Output only. The time this `Occurrence` was last updated.  # noqa: E501

        :param update_time: The update_time of this ApiOccurrence.  # noqa: E501
        :type: datetime
        """

        self._update_time = update_time

    @property
    def operation_name(self):
        """Gets the operation_name of this ApiOccurrence.  # noqa: E501


        :return: The operation_name of this ApiOccurrence.  # noqa: E501
        :rtype: str
        """
        return self._operation_name

    @operation_name.setter
    def operation_name(self, operation_name):
        """Sets the operation_name of this ApiOccurrence.


        :param operation_name: The operation_name of this ApiOccurrence.  # noqa: E501
        :type: str
        """

        self._operation_name = operation_name

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
        if issubclass(ApiOccurrence, dict):
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
        if not isinstance(other, ApiOccurrence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other