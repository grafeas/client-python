# ApiNote

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the note in the form \&quot;projects/{PROJECT_ID}/notes/{NOTE_ID}\&quot;. | [optional] 
**short_description** | **str** | A one sentence description of this &#x60;Note&#x60;. | [optional] 
**long_description** | **str** | A detailed description of this &#x60;Note&#x60;. | [optional] 
**kind** | [**ApiNoteKind**](ApiNoteKind.md) | Output only. This explicitly denotes which kind of note is specified. This field can be used as a filter in list requests. | [optional] 
**vulnerability_type** | [**ApiVulnerabilityType**](ApiVulnerabilityType.md) | A package vulnerability type of note. | [optional] 
**build_type** | [**ApiBuildType**](ApiBuildType.md) | Build provenance type for a verifiable build. | [optional] 
**base_image** | [**DockerImageBasis**](DockerImageBasis.md) | A note describing a base image. | [optional] 
**package** | [**PackageManagerPackage**](PackageManagerPackage.md) | A note describing a package hosted by various package managers. | [optional] 
**deployable** | [**ApiDeployable**](ApiDeployable.md) | A note describing something that can be deployed. | [optional] 
**discovery** | [**ApiDiscovery**](ApiDiscovery.md) | A note describing a provider/analysis type. | [optional] 
**attestation_authority** | [**ApiAttestationAuthority**](ApiAttestationAuthority.md) | A note describing an attestation role. | [optional] 
**related_url** | [**list[NoteRelatedUrl]**](NoteRelatedUrl.md) | URLs associated with this note. | [optional] 
**expiration_time** | **datetime** | Time of expiration for this note, null if note does not expire. | [optional] 
**create_time** | **datetime** | Output only. The time this note was created. This field can be used as a filter in list requests. | [optional] 
**update_time** | **datetime** | Output only. The time this note was last updated. This field can be used as a filter in list requests. | [optional] 
**operation_name** | **str** | The name of the &#x60;Operation&#x60; in the form \&quot;projects/{PROJECT_ID}/operations/{OPERATION_ID}\&quot;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


