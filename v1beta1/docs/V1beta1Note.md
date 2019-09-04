# V1beta1Note

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Output only. The name of the note in the form of &#x60;projects/[PROVIDER_ID]/notes/[NOTE_ID]&#x60;. | [optional] 
**short_description** | **str** | A one sentence description of this note. | [optional] 
**long_description** | **str** | A detailed description of this note. | [optional] 
**kind** | [**V1beta1NoteKind**](V1beta1NoteKind.md) |  | [optional] 
**related_url** | [**list[V1beta1RelatedUrl]**](V1beta1RelatedUrl.md) | URLs associated with this note. | [optional] 
**expiration_time** | **datetime** | Time of expiration for this note. Empty if note does not expire. | [optional] 
**create_time** | **datetime** | Output only. The time this note was created. This field can be used as a filter in list requests. | [optional] 
**update_time** | **datetime** | Output only. The time this note was last updated. This field can be used as a filter in list requests. | [optional] 
**related_note_names** | **list[str]** | Other notes related to this note. | [optional] 
**vulnerability** | [**VulnerabilityVulnerability**](VulnerabilityVulnerability.md) |  | [optional] 
**build** | [**BuildBuild**](BuildBuild.md) |  | [optional] 
**base_image** | [**ImageBasis**](ImageBasis.md) |  | [optional] 
**package** | [**PackagePackage**](PackagePackage.md) |  | [optional] 
**deployable** | [**DeploymentDeployable**](DeploymentDeployable.md) |  | [optional] 
**discovery** | [**DiscoveryDiscovery**](DiscoveryDiscovery.md) |  | [optional] 
**attestation_authority** | [**AttestationAuthority**](AttestationAuthority.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

