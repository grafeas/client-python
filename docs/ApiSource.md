# ApiSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_source** | [**ApiStorageSource**](ApiStorageSource.md) | If provided, get the source from this location in in Google Cloud Storage. | [optional] 
**repo_source** | [**ApiRepoSource**](ApiRepoSource.md) | If provided, get source from this location in a Cloud Repo. | [optional] 
**artifact_storage_source** | [**ApiStorageSource**](ApiStorageSource.md) | If provided, the input binary artifacts for the build came from this location. | [optional] 
**file_hashes** | [**dict(str, ApiFileHashes)**](ApiFileHashes.md) | Hash(es) of the build source, which can be used to verify that the original source integrity was maintained in the build.  The keys to this map are file paths used as build source and the values contain the hash values for those files.  If the build source came in a single package such as a gzipped tarfile (.tar.gz), the FileHash will be for the single path to that file. | [optional] 
**context** | [**ApiSourceContext**](ApiSourceContext.md) | If provided, the source code used for the build came from this location. | [optional] 
**additional_contexts** | [**list[ApiSourceContext]**](ApiSourceContext.md) | If provided, some of the source code used for the build may be found in these locations, in the case where the source repository had multiple remotes or submodules. This list will not include the context specified in the context field. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


