# ApiOccurrence

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**resource_url** | **str** | The unique URL of the image or the container for which the &#x60;Occurrence&#x60; applies. For example, https://gcr.io/project/image@sha256:foo This field can be used as a filter in list requests. | [optional] 
**note_name** | **str** | An analysis note associated with this image, in the form \&quot;providers/{provider_id}/notes/{NOTE_ID}\&quot; This field can be used as a filter in list requests. | [optional] 
**kind** | [**ApiNoteKind**](ApiNoteKind.md) | Output only. This explicitly denotes which of the &#x60;Occurrence&#x60; details are specified. This field can be used as a filter in list requests. | [optional] 
**vulnerability_details** | [**VulnerabilityTypeVulnerabilityDetails**](VulnerabilityTypeVulnerabilityDetails.md) | Details of a security vulnerability note. | [optional] 
**build_details** | [**ApiBuildDetails**](ApiBuildDetails.md) | Build details for a verifiable build. | [optional] 
**derived_image_details** | [**DockerImageDerivedDetails**](DockerImageDerivedDetails.md) | Describes how this resource derives from the basis in the associated note. | [optional] 
**installation_details** | [**PackageManagerInstallationDetails**](PackageManagerInstallationDetails.md) | Describes the installation of a package on the linked resource. | [optional] 
**deployment_details** | [**DeployableDeploymentDetails**](DeployableDeploymentDetails.md) | Describes the deployment of an artifact on a runtime. | [optional] 
**discovered_details** | [**DiscoveryDiscoveredDetails**](DiscoveryDiscoveredDetails.md) | Describes the initial scan status for this resource. | [optional] 
**attestation_details** | [**AttestationAuthorityAttestationDetails**](AttestationAuthorityAttestationDetails.md) | Describes an attestation of an artifact. | [optional] 
**remediation** | **str** |  | [optional] 
**create_time** | **datetime** | Output only. The time this &#x60;Occurrence&#x60; was created. | [optional] 
**update_time** | **datetime** | Output only. The time this &#x60;Occurrence&#x60; was last updated. | [optional] 
**operation_name** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


