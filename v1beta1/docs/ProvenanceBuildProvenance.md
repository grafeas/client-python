# ProvenanceBuildProvenance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Required. Unique identifier of the build. | [optional] 
**project_id** | **str** | ID of the project. | [optional] 
**commands** | [**list[ProvenanceCommand]**](ProvenanceCommand.md) | Commands requested by the build. | [optional] 
**built_artifacts** | [**list[ProvenanceArtifact]**](ProvenanceArtifact.md) | Output of the build. | [optional] 
**create_time** | **datetime** | Time at which the build was created. | [optional] 
**start_time** | **datetime** | Time at which execution of the build was started. | [optional] 
**end_time** | **datetime** | Time at which execution of the build was finished. | [optional] 
**creator** | **str** | E-mail address of the user who initiated this build. Note that this was the user&#x27;s e-mail address at the time the build was initiated; this address may not represent the same end-user for all time. | [optional] 
**logs_uri** | **str** | URI where any logs for this provenance were written. | [optional] 
**source_provenance** | [**ProvenanceSource**](ProvenanceSource.md) |  | [optional] 
**trigger_id** | **str** | Trigger identifier if the build was triggered automatically; empty if not. | [optional] 
**build_options** | **dict(str, str)** | Special options applied to this build. This is a catch-all field where build providers can enter any desired additional details. | [optional] 
**builder_version** | **str** | Version string of the builder at the time this build was executed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

