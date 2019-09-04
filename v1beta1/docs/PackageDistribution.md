# PackageDistribution

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpe_uri** | **str** | Required. The cpe_uri in [CPE format](https://cpe.mitre.org/specification/) denoting the package manager version distributing a package. | [optional] 
**architecture** | [**PackageArchitecture**](PackageArchitecture.md) | The CPU architecture for which packages in this distribution channel were built. | [optional] 
**latest_version** | [**PackageVersion**](PackageVersion.md) | The latest available version of this package in this distribution channel. | [optional] 
**maintainer** | **str** | A freeform string denoting the maintainer of this package. | [optional] 
**url** | **str** | The distribution channel-specific homepage for this package. | [optional] 
**description** | **str** | The distribution channel-specific description of this package. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


