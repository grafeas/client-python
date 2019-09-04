# DiscoveryDiscovered

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continuous_analysis** | [**DiscoveredContinuousAnalysis**](DiscoveredContinuousAnalysis.md) | Whether the resource is continuously analyzed. | [optional] 
**last_analysis_time** | **datetime** | The last time continuous analysis was done for this resource. Deprecated, do not use. | [optional] 
**analysis_status** | [**DiscoveredAnalysisStatus**](DiscoveredAnalysisStatus.md) | The status of discovery for the resource. | [optional] 
**analysis_status_error** | [**RpcStatus**](RpcStatus.md) | When an error is encountered this will contain a LocalizedMessage under details to show to the user. The LocalizedMessage is output only and populated by the API. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


