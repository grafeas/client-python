# grafeas.GrafeasApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_note**](GrafeasApi.md#create_note) | **POST** /v1alpha1/{parent}/notes | Creates a new &#x60;Note&#x60;.
[**create_occurrence**](GrafeasApi.md#create_occurrence) | **POST** /v1alpha1/{parent}/occurrences | Creates a new &#x60;Occurrence&#x60;. Use this method to create &#x60;Occurrences&#x60; for a resource.
[**create_operation**](GrafeasApi.md#create_operation) | **POST** /v1alpha1/{parent}/operations | Creates a new &#x60;Operation&#x60;.
[**get_occurrence_note**](GrafeasApi.md#get_occurrence_note) | **GET** /v1alpha1/{name}/notes | Gets the &#x60;Note&#x60; attached to the given &#x60;Occurrence&#x60;.
[**list_note_occurrences**](GrafeasApi.md#list_note_occurrences) | **GET** /v1alpha1/{name}/occurrences | Lists &#x60;Occurrences&#x60; referencing the specified &#x60;Note&#x60;. Use this method to get all occurrences referencing your &#x60;Note&#x60; across all your customer projects.
[**list_notes**](GrafeasApi.md#list_notes) | **GET** /v1alpha1/{parent}/notes | Lists all &#x60;Notes&#x60; for a given project.
[**list_occurrences**](GrafeasApi.md#list_occurrences) | **GET** /v1alpha1/{parent}/occurrences | Lists active &#x60;Occurrences&#x60; for a given project matching the filters.
[**update_note**](GrafeasApi.md#update_note) | **PATCH** /v1alpha1/{name} | Updates an existing &#x60;Note&#x60;.


# **create_note**
> ApiNote create_note(parent, body)

Creates a new `Note`.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.GrafeasApi()
parent = 'parent_example' # str | 
body = grafeas.ApiNote() # ApiNote | 

try:
    # Creates a new `Note`.
    api_response = api_instance.create_note(parent, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasApi->create_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**|  | 
 **body** | [**ApiNote**](ApiNote.md)|  | 

### Return type

[**ApiNote**](ApiNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_occurrence**
> ApiOccurrence create_occurrence(parent, body)

Creates a new `Occurrence`. Use this method to create `Occurrences` for a resource.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.GrafeasApi()
parent = 'parent_example' # str | 
body = grafeas.ApiOccurrence() # ApiOccurrence | 

try:
    # Creates a new `Occurrence`. Use this method to create `Occurrences` for a resource.
    api_response = api_instance.create_occurrence(parent, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasApi->create_occurrence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**|  | 
 **body** | [**ApiOccurrence**](ApiOccurrence.md)|  | 

### Return type

[**ApiOccurrence**](ApiOccurrence.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_operation**
> LongrunningOperation create_operation(parent, body)

Creates a new `Operation`.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.GrafeasApi()
parent = 'parent_example' # str | 
body = grafeas.ApiCreateOperationRequest() # ApiCreateOperationRequest | 

try:
    # Creates a new `Operation`.
    api_response = api_instance.create_operation(parent, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasApi->create_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**|  | 
 **body** | [**ApiCreateOperationRequest**](ApiCreateOperationRequest.md)|  | 

### Return type

[**LongrunningOperation**](LongrunningOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_occurrence_note**
> ApiNote get_occurrence_note(name)

Gets the `Note` attached to the given `Occurrence`.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.GrafeasApi()
name = 'name_example' # str | 

try:
    # Gets the `Note` attached to the given `Occurrence`.
    api_response = api_instance.get_occurrence_note(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasApi->get_occurrence_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**ApiNote**](ApiNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_note_occurrences**
> ApiListNoteOccurrencesResponse list_note_occurrences(name, filter=filter, page_size=page_size, page_token=page_token)

Lists `Occurrences` referencing the specified `Note`. Use this method to get all occurrences referencing your `Note` across all your customer projects.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.GrafeasApi()
name = 'name_example' # str | 
filter = 'filter_example' # str | The filter expression. (optional)
page_size = 56 # int | Number of notes to return in the list. (optional)
page_token = 'page_token_example' # str | Token to provide to skip to a particular spot in the list. (optional)

try:
    # Lists `Occurrences` referencing the specified `Note`. Use this method to get all occurrences referencing your `Note` across all your customer projects.
    api_response = api_instance.list_note_occurrences(name, filter=filter, page_size=page_size, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasApi->list_note_occurrences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **filter** | **str**| The filter expression. | [optional] 
 **page_size** | **int**| Number of notes to return in the list. | [optional] 
 **page_token** | **str**| Token to provide to skip to a particular spot in the list. | [optional] 

### Return type

[**ApiListNoteOccurrencesResponse**](ApiListNoteOccurrencesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_notes**
> ApiListNotesResponse list_notes(parent, filter=filter, page_size=page_size, page_token=page_token)

Lists all `Notes` for a given project.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.GrafeasApi()
parent = 'parent_example' # str | 
filter = 'filter_example' # str | The filter expression. (optional)
page_size = 56 # int | Number of notes to return in the list. (optional)
page_token = 'page_token_example' # str | Token to provide to skip to a particular spot in the list. (optional)

try:
    # Lists all `Notes` for a given project.
    api_response = api_instance.list_notes(parent, filter=filter, page_size=page_size, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasApi->list_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**|  | 
 **filter** | **str**| The filter expression. | [optional] 
 **page_size** | **int**| Number of notes to return in the list. | [optional] 
 **page_token** | **str**| Token to provide to skip to a particular spot in the list. | [optional] 

### Return type

[**ApiListNotesResponse**](ApiListNotesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_occurrences**
> ApiListOccurrencesResponse list_occurrences(parent, filter=filter, page_size=page_size, page_token=page_token)

Lists active `Occurrences` for a given project matching the filters.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.GrafeasApi()
parent = 'parent_example' # str | 
filter = 'filter_example' # str | The filter expression. (optional)
page_size = 56 # int | Number of occurrences to return in the list. (optional)
page_token = 'page_token_example' # str | Token to provide to skip to a particular spot in the list. (optional)

try:
    # Lists active `Occurrences` for a given project matching the filters.
    api_response = api_instance.list_occurrences(parent, filter=filter, page_size=page_size, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasApi->list_occurrences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**|  | 
 **filter** | **str**| The filter expression. | [optional] 
 **page_size** | **int**| Number of occurrences to return in the list. | [optional] 
 **page_token** | **str**| Token to provide to skip to a particular spot in the list. | [optional] 

### Return type

[**ApiListOccurrencesResponse**](ApiListOccurrencesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_note**
> ApiNote update_note(name, body)

Updates an existing `Note`.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.GrafeasApi()
name = 'name_example' # str | 
body = grafeas.ApiNote() # ApiNote | 

try:
    # Updates an existing `Note`.
    api_response = api_instance.update_note(name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasApi->update_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **body** | [**ApiNote**](ApiNote.md)|  | 

### Return type

[**ApiNote**](ApiNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

