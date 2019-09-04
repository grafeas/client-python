# DeploymentDeployment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_email** | **str** | Identity of the user that triggered this deployment. | [optional] 
**deploy_time** | **datetime** | Required. Beginning of the lifetime of this deployment. | [optional] 
**undeploy_time** | **datetime** | End of the lifetime of this deployment. | [optional] 
**config** | **str** | Configuration used to create this deployment. | [optional] 
**address** | **str** | Address of the runtime element hosting this deployment. | [optional] 
**resource_uri** | **list[str]** | Output only. Resource URI for the artifact being deployed taken from the deployable field with the same name. | [optional] 
**platform** | [**DeploymentPlatform**](DeploymentPlatform.md) | Platform hosting this deployment. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


