# DockerImageDerivedDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fingerprint** | [**DockerImageFingerprint**](DockerImageFingerprint.md) |  | [optional] 
**distance** | **int** | Output only. The number of layers by which this image differs from the associated image basis. | [optional] 
**layer_info** | [**list[DockerImageLayer]**](DockerImageLayer.md) | This contains layer-specific metadata, if populated it has length \&quot;distance\&quot; and is ordered with [distance] being the layer immediately following the base image and [1] being the final layer. | [optional] 
**base_resource_url** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


