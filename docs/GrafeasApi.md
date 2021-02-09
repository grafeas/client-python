# grafeas.GrafeasApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_note**](GrafeasApi.md#create_note) | **POST** /v1alpha1/{parent&#x3D;projects/*}/notes | Creates a new &#x60;Note&#x60;.
[**create_occurrence**](GrafeasApi.md#create_occurrence) | **POST** /v1alpha1/{parent&#x3D;projects/*}/occurrences | Creates a new &#x60;Occurrence&#x60;. Use this method to create &#x60;Occurrences&#x60; for a resource.
[**create_operation**](GrafeasApi.md#create_operation) | **POST** /v1alpha1/{parent&#x3D;projects/*}/operations | Creates a new &#x60;Operation&#x60;.
[**delete_note**](GrafeasApi.md#delete_note) | **DELETE** /v1alpha1/{name&#x3D;projects/*/notes/*} | Deletes the given &#x60;Note&#x60; from the system.
[**delete_occurrence**](GrafeasApi.md#delete_occurrence) | **DELETE** /v1alpha1/{name&#x3D;projects/*/occurrences/*} | Deletes the given &#x60;Occurrence&#x60; from the system. Use this when an &#x60;Occurrence&#x60; is no longer applicable for the given resource.
[**get_note**](GrafeasApi.md#get_note) | **GET** /v1alpha1/{name&#x3D;projects/*/notes/*} | Returns the requested &#x60;Note&#x60;.
[**get_occurrence**](GrafeasApi.md#get_occurrence) | **GET** /v1alpha1/{name&#x3D;projects/*/occurrences/*} | Returns the requested &#x60;Occurrence&#x60;.
[**get_occurrence_note**](GrafeasApi.md#get_occurrence_note) | **GET** /v1alpha1/{name&#x3D;projects/*/occurrences/*}/notes | Gets the &#x60;Note&#x60; attached to the given &#x60;Occurrence&#x60;.
[**list_note_occurrences**](GrafeasApi.md#list_note_occurrences) | **GET** /v1alpha1/{name&#x3D;projects/*/notes/*}/occurrences | Lists &#x60;Occurrences&#x60; referencing the specified &#x60;Note&#x60;. Use this method to get all occurrences referencing your &#x60;Note&#x60; across all your customer projects.
[**list_notes**](GrafeasApi.md#list_notes) | **GET** /v1alpha1/{parent&#x3D;projects/*}/notes | Lists all &#x60;Notes&#x60; for a given project.
[**list_occurrences**](GrafeasApi.md#list_occurrences) | **GET** /v1alpha1/{parent&#x3D;projects/*}/occurrences | Lists active &#x60;Occurrences&#x60; for a given project matching the filters.
[**update_note**](GrafeasApi.md#update_note) | **PATCH** /v1alpha1/{name&#x3D;projects/*/notes/*} | Updates an existing &#x60;Note&#x60;.
[**update_occurrence**](GrafeasApi.md#update_occurrence) | **PATCH** /v1alpha1/{name&#x3D;projects/*/occurrences/*} | Updates an existing occurrence.
[**update_operation**](GrafeasApi.md#update_operation) | **PATCH** /v1alpha1/{name&#x3D;projects/*/operations/*} | Updates an existing operation returns an error if operation  does not exist. The only valid operations are to update mark the done bit change the result.


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
parent = 'parent_example' # str | This field contains the project Id for example: \"project/{project_id}
body = grafeas.ApiNote() # ApiNote | The Note to be inserted

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
 **parent** | **str**| This field contains the project Id for example: \&quot;project/{project_id} | 
 **body** | [**ApiNote**](ApiNote.md)| The Note to be inserted | 

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
parent = 'parent_example' # str | This field contains the project Id for example: \"projects/{project_id}\"
body = grafeas.ApiOccurrence() # ApiOccurrence | The occurrence to be inserted.

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
 **parent** | **str**| This field contains the project Id for example: \&quot;projects/{project_id}\&quot; | 
 **body** | [**ApiOccurrence**](ApiOccurrence.md)| The occurrence to be inserted. | 

### Return type

[**ApiOccurrence**](ApiOccurrence.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_operation**
> GooglelongrunningOperation create_operation(parent, body)

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
parent = 'parent_example' # str | The projectId that this operation should be created under.
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
 **parent** | **str**| The projectId that this operation should be created under. | 
 **body** | [**ApiCreateOperationRequest**](ApiCreateOperationRequest.md)|  | 

### Return type

[**GooglelongrunningOperation**](GooglelongrunningOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_note**
> object delete_note(name)

Deletes the given `Note` from the system.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.GrafeasApi()
name = 'name_example' # str | The name of the note in the form of \"providers/{provider_id}/notes/{NOTE_ID}\"

try:
    # Deletes the given `Note` from the system.
    api_response = api_instance.delete_note(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasApi->delete_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the note in the form of \&quot;providers/{provider_id}/notes/{NOTE_ID}\&quot; | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_occurrence**
> object delete_occurrence(name)

Deletes the given `Occurrence` from the system. Use this when an `Occurrence` is no longer applicable for the given resource.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.GrafeasApi()
name = 'name_example' # str | The name of the occurrence in the form of \"projects/{project_id}/occurrences/{OCCURRENCE_ID}\"

try:
    # Deletes the given `Occurrence` from the system. Use this when an `Occurrence` is no longer applicable for the given resource.
    api_response = api_instance.delete_occurrence(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasApi->delete_occurrence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the occurrence in the form of \&quot;projects/{project_id}/occurrences/{OCCURRENCE_ID}\&quot; | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_note**
> ApiNote get_note(name)

Returns the requested `Note`.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.GrafeasApi()
name = 'name_example' # str | The name of the note in the form of \"providers/{provider_id}/notes/{NOTE_ID}\"

try:
    # Returns the requested `Note`.
    api_response = api_instance.get_note(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasApi->get_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the note in the form of \&quot;providers/{provider_id}/notes/{NOTE_ID}\&quot; | 

### Return type

[**ApiNote**](ApiNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_occurrence**
> ApiOccurrence get_occurrence(name)

Returns the requested `Occurrence`.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.GrafeasApi()
name = 'name_example' # str | The name of the occurrence of the form \"projects/{project_id}/occurrences/{OCCURRENCE_ID}\"

try:
    # Returns the requested `Occurrence`.
    api_response = api_instance.get_occurrence(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasApi->get_occurrence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the occurrence of the form \&quot;projects/{project_id}/occurrences/{OCCURRENCE_ID}\&quot; | 

### Return type

[**ApiOccurrence**](ApiOccurrence.md)

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
name = 'name_example' # str | The name of the occurrence in the form \"projects/{project_id}/occurrences/{OCCURRENCE_ID}\"

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
 **name** | **str**| The name of the occurrence in the form \&quot;projects/{project_id}/occurrences/{OCCURRENCE_ID}\&quot; | 

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
name = 'name_example' # str | The name field will contain the note name for example:   \"provider/{provider_id}/notes/{note_id}\"
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
 **name** | **str**| The name field will contain the note name for example:   \&quot;provider/{provider_id}/notes/{note_id}\&quot; | 
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
parent = 'parent_example' # str | This field contains the project ID for example: \"projects/{project_id}\".
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
 **parent** | **str**| This field contains the project ID for example: \&quot;projects/{project_id}\&quot;. | 
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
parent = 'parent_example' # str | This contains the project Id for example: projects/{project_id}.
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
 **parent** | **str**| This contains the project Id for example: projects/{project_id}. | 
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
name = 'name_example' # str | The name of the note. Should be of the form \"projects/{provider_id}/notes/{note_id}\".
body = grafeas.ApiNote() # ApiNote | The updated note.

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
 **name** | **str**| The name of the note. Should be of the form \&quot;projects/{provider_id}/notes/{note_id}\&quot;. | 
 **body** | [**ApiNote**](ApiNote.md)| The updated note. | 

### Return type

[**ApiNote**](ApiNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_occurrence**
> ApiOccurrence update_occurrence(name, body)

Updates an existing occurrence.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.GrafeasApi()
name = 'name_example' # str | The name of the occurrence. Should be of the form \"projects/{project_id}/occurrences/{OCCURRENCE_ID}\".
body = grafeas.ApiOccurrence() # ApiOccurrence | The updated occurrence.

try:
    # Updates an existing occurrence.
    api_response = api_instance.update_occurrence(name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasApi->update_occurrence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the occurrence. Should be of the form \&quot;projects/{project_id}/occurrences/{OCCURRENCE_ID}\&quot;. | 
 **body** | [**ApiOccurrence**](ApiOccurrence.md)| The updated occurrence. | 

### Return type

[**ApiOccurrence**](ApiOccurrence.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_operation**
> GooglelongrunningOperation update_operation(name, body)

Updates an existing operation returns an error if operation  does not exist. The only valid operations are to update mark the done bit change the result.

### Example
```python
from __future__ import print_function
import time
import grafeas
from grafeas.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = grafeas.GrafeasApi()
name = 'name_example' # str | The name of the Operation. Should be of the form \"projects/{provider_id}/operations/{operation_id}\".
body = grafeas.ApiUpdateOperationRequest() # ApiUpdateOperationRequest | 

try:
    # Updates an existing operation returns an error if operation  does not exist. The only valid operations are to update mark the done bit change the result.
    api_response = api_instance.update_operation(name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasApi->update_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Operation. Should be of the form \&quot;projects/{provider_id}/operations/{operation_id}\&quot;. | 
 **body** | [**ApiUpdateOperationRequest**](ApiUpdateOperationRequest.md)|  | 

### Return type

[**GooglelongrunningOperation**](GooglelongrunningOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

