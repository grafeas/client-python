# ProvenanceCommand

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Required. Name of the command, as presented on the command line, or if the command is packaged as a Docker container, as presented to &#x60;docker pull&#x60;. | [optional] 
**env** | **list[str]** | Environment variables set before running this command. | [optional] 
**args** | **list[str]** | Command-line arguments used when executing this command. | [optional] 
**dir** | **str** | Working directory (relative to project source root) used when running this command. | [optional] 
**id** | **str** | Optional unique identifier for this command, used in wait_for to reference this command as a dependency. | [optional] 
**wait_for** | **list[str]** | The ID(s) of the command(s) that this command depends on. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


