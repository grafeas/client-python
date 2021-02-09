# grafeas.GrafeasProjectsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](GrafeasProjectsApi.md#create_project) | **POST** /v1alpha1/projects | Creates a new project.
[**delete_project**](GrafeasProjectsApi.md#delete_project) | **DELETE** /v1alpha1/{name&#x3D;projects/*} | Deletes the specified project.
[**get_project**](GrafeasProjectsApi.md#get_project) | **GET** /v1alpha1/{name&#x3D;projects/*} | Gets the specified project.
[**list_projects**](GrafeasProjectsApi.md#list_projects) | **GET** /v1alpha1/projects | Lists projects.


# **create_project**
> object create_project(body)

Creates a new project.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.GrafeasProjectsApi()
body = grafeas.ApiProject() # ApiProject | The project to create.

try:
    # Creates a new project.
    api_response = api_instance.create_project(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasProjectsApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiProject**](ApiProject.md)| The project to create. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> object delete_project(name)

Deletes the specified project.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.GrafeasProjectsApi()
name = 'name_example' # str | The name of the project in the form of `projects/{PROJECT_ID}`.

try:
    # Deletes the specified project.
    api_response = api_instance.delete_project(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasProjectsApi->delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the project in the form of &#x60;projects/{PROJECT_ID}&#x60;. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> ApiProject get_project(name)

Gets the specified project.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.GrafeasProjectsApi()
name = 'name_example' # str | The name of the project in the form of `projects/{PROJECT_ID}`.

try:
    # Gets the specified project.
    api_response = api_instance.get_project(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasProjectsApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the project in the form of &#x60;projects/{PROJECT_ID}&#x60;. | 

### Return type

[**ApiProject**](ApiProject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_projects**
> ApiListProjectsResponse list_projects(filter=filter, page_size=page_size, page_token=page_token)

Lists projects.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.GrafeasProjectsApi()
filter = 'filter_example' # str | The filter expression. (optional)
page_size = 56 # int | Number of projects to return in the list. (optional)
page_token = 'page_token_example' # str | Token to provide to skip to a particular spot in the list. (optional)

try:
    # Lists projects.
    api_response = api_instance.list_projects(filter=filter, page_size=page_size, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasProjectsApi->list_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The filter expression. | [optional] 
 **page_size** | **int**| Number of projects to return in the list. | [optional] 
 **page_token** | **str**| Token to provide to skip to a particular spot in the list. | [optional] 

### Return type

[**ApiListProjectsResponse**](ApiListProjectsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

