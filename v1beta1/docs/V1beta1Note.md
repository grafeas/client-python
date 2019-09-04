# V1beta1Note

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Output only. The name of the note in the form of &#x60;projects/[PROVIDER_ID]/notes/[NOTE_ID]&#x60;. | [optional] 
**short_description** | **str** | A one sentence description of this note. | [optional] 
**long_description** | **str** | A detailed description of this note. | [optional] 
**kind** | [**V1beta1NoteKind**](V1beta1NoteKind.md) | Output only. The type of analysis. This field can be used as a filter in list requests. | [optional] 
**related_url** | [**list[V1beta1RelatedUrl]**](V1beta1RelatedUrl.md) | URLs associated with this note. | [optional] 
**expiration_time** | **datetime** | Time of expiration for this note. Empty if note does not expire. | [optional] 
**create_time** | **datetime** | Output only. The time this note was created. This field can be used as a filter in list requests. | [optional] 
**update_time** | **datetime** | Output only. The time this note was last updated. This field can be used as a filter in list requests. | [optional] 
**related_note_names** | **list[str]** | Other notes related to this note. | [optional] 
**vulnerability** | [**VulnerabilityVulnerability**](VulnerabilityVulnerability.md) | A note describing a package vulnerability. | [optional] 
**build** | [**BuildBuild**](BuildBuild.md) | A note describing build provenance for a verifiable build. | [optional] 
**base_image** | [**ImageBasis**](ImageBasis.md) | A note describing a base image. | [optional] 
**package** | [**PackagePackage**](PackagePackage.md) | A note describing a package hosted by various package managers. | [optional] 
**deployable** | [**DeploymentDeployable**](DeploymentDeployable.md) | A note describing something that can be deployed. | [optional] 
**discovery** | [**DiscoveryDiscovery**](DiscoveryDiscovery.md) | A note describing the initial analysis of a resource. | [optional] 
**attestation_authority** | [**AttestationAuthority**](AttestationAuthority.md) | A note describing an attestation role. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


