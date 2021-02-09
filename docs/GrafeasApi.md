# grafeas.GrafeasApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grafeas_create_note**](GrafeasApi.md#grafeas_create_note) | **POST** /v1alpha1/{parent&#x3D;projects/*}/notes | Creates a new &#x60;Note&#x60;.
[**grafeas_create_occurrence**](GrafeasApi.md#grafeas_create_occurrence) | **POST** /v1alpha1/{parent&#x3D;projects/*}/occurrences | Creates a new &#x60;Occurrence&#x60;. Use this method to create &#x60;Occurrences&#x60; for a resource.
[**grafeas_create_operation**](GrafeasApi.md#grafeas_create_operation) | **POST** /v1alpha1/{parent&#x3D;projects/*}/operations | Creates a new &#x60;Operation&#x60;.
[**grafeas_delete_note**](GrafeasApi.md#grafeas_delete_note) | **DELETE** /v1alpha1/{name&#x3D;projects/*/notes/*} | Deletes the given &#x60;Note&#x60; from the system.
[**grafeas_delete_occurrence**](GrafeasApi.md#grafeas_delete_occurrence) | **DELETE** /v1alpha1/{name&#x3D;projects/*/occurrences/*} | Deletes the given &#x60;Occurrence&#x60; from the system. Use this when an &#x60;Occurrence&#x60; is no longer applicable for the given resource.
[**grafeas_get_note**](GrafeasApi.md#grafeas_get_note) | **GET** /v1alpha1/{name&#x3D;projects/*/notes/*} | Returns the requested &#x60;Note&#x60;.
[**grafeas_get_occurrence**](GrafeasApi.md#grafeas_get_occurrence) | **GET** /v1alpha1/{name&#x3D;projects/*/occurrences/*} | Returns the requested &#x60;Occurrence&#x60;.
[**grafeas_get_occurrence_note**](GrafeasApi.md#grafeas_get_occurrence_note) | **GET** /v1alpha1/{name&#x3D;projects/*/occurrences/*}/notes | Gets the &#x60;Note&#x60; attached to the given &#x60;Occurrence&#x60;.
[**grafeas_list_note_occurrences**](GrafeasApi.md#grafeas_list_note_occurrences) | **GET** /v1alpha1/{name&#x3D;projects/*/notes/*}/occurrences | Lists &#x60;Occurrences&#x60; referencing the specified &#x60;Note&#x60;. Use this method to get all occurrences referencing your &#x60;Note&#x60; across all your customer projects.
[**grafeas_list_notes**](GrafeasApi.md#grafeas_list_notes) | **GET** /v1alpha1/{parent&#x3D;projects/*}/notes | Lists all &#x60;Notes&#x60; for a given project.
[**grafeas_list_occurrences**](GrafeasApi.md#grafeas_list_occurrences) | **GET** /v1alpha1/{parent&#x3D;projects/*}/occurrences | Lists active &#x60;Occurrences&#x60; for a given project matching the filters.
[**grafeas_update_note**](GrafeasApi.md#grafeas_update_note) | **PATCH** /v1alpha1/{name&#x3D;projects/*/notes/*} | Updates an existing &#x60;Note&#x60;.
[**grafeas_update_occurrence**](GrafeasApi.md#grafeas_update_occurrence) | **PATCH** /v1alpha1/{name&#x3D;projects/*/occurrences/*} | Updates an existing occurrence.
[**grafeas_update_operation**](GrafeasApi.md#grafeas_update_operation) | **PATCH** /v1alpha1/{name&#x3D;projects/*/operations/*} | Updates an existing operation returns an error if operation  does not exist. The only valid operations are to update mark the done bit change the result.


# **grafeas_create_note**
> ApiNote grafeas_create_note(parent, body, note_id=note_id)

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
note_id = 'note_id_example' # str | The ID to use for this note. (optional)

try:
    # Creates a new `Note`.
    api_response = api_instance.grafeas_create_note(parent, body, note_id=note_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasApi->grafeas_create_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| This field contains the project Id for example: \&quot;project/{project_id} | 
 **body** | [**ApiNote**](ApiNote.md)| The Note to be inserted | 
 **note_id** | **str**| The ID to use for this note. | [optional] 

### Return type

[**ApiNote**](ApiNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grafeas_create_occurrence**
> ApiOccurrence grafeas_create_occurrence(parent, body)

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
    api_response = api_instance.grafeas_create_occurrence(parent, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasApi->grafeas_create_occurrence: %s\n" % e)
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

# **grafeas_create_operation**
> GooglelongrunningOperation grafeas_create_operation(parent, body)

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
    api_response = api_instance.grafeas_create_operation(parent, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasApi->grafeas_create_operation: %s\n" % e)
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

# **grafeas_delete_note**
> object grafeas_delete_note(name)

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
    api_response = api_instance.grafeas_delete_note(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasApi->grafeas_delete_note: %s\n" % e)
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

# **grafeas_delete_occurrence**
> object grafeas_delete_occurrence(name)

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
    api_response = api_instance.grafeas_delete_occurrence(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasApi->grafeas_delete_occurrence: %s\n" % e)
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

# **grafeas_get_note**
> ApiNote grafeas_get_note(name)

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
    api_response = api_instance.grafeas_get_note(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasApi->grafeas_get_note: %s\n" % e)
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

# **grafeas_get_occurrence**
> ApiOccurrence grafeas_get_occurrence(name)

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
    api_response = api_instance.grafeas_get_occurrence(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasApi->grafeas_get_occurrence: %s\n" % e)
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

# **grafeas_get_occurrence_note**
> ApiNote grafeas_get_occurrence_note(name)

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
    api_response = api_instance.grafeas_get_occurrence_note(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasApi->grafeas_get_occurrence_note: %s\n" % e)
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

# **grafeas_list_note_occurrences**
> ApiListNoteOccurrencesResponse grafeas_list_note_occurrences(name, filter=filter, page_size=page_size, page_token=page_token)

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
    api_response = api_instance.grafeas_list_note_occurrences(name, filter=filter, page_size=page_size, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasApi->grafeas_list_note_occurrences: %s\n" % e)
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

# **grafeas_list_notes**
> ApiListNotesResponse grafeas_list_notes(parent, filter=filter, page_size=page_size, page_token=page_token)

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
    api_response = api_instance.grafeas_list_notes(parent, filter=filter, page_size=page_size, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasApi->grafeas_list_notes: %s\n" % e)
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

# **grafeas_list_occurrences**
> ApiListOccurrencesResponse grafeas_list_occurrences(parent, filter=filter, page_size=page_size, page_token=page_token)

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
    api_response = api_instance.grafeas_list_occurrences(parent, filter=filter, page_size=page_size, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasApi->grafeas_list_occurrences: %s\n" % e)
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

# **grafeas_update_note**
> ApiNote grafeas_update_note(name, body, update_mask=update_mask)

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
update_mask = ['update_mask_example'] # list[str] | The fields to update. (optional)

try:
    # Updates an existing `Note`.
    api_response = api_instance.grafeas_update_note(name, body, update_mask=update_mask)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasApi->grafeas_update_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the note. Should be of the form \&quot;projects/{provider_id}/notes/{note_id}\&quot;. | 
 **body** | [**ApiNote**](ApiNote.md)| The updated note. | 
 **update_mask** | [**list[str]**](str.md)| The fields to update. | [optional] 

### Return type

[**ApiNote**](ApiNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grafeas_update_occurrence**
> ApiOccurrence grafeas_update_occurrence(name, body, update_mask=update_mask)

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
update_mask = ['update_mask_example'] # list[str] | The fields to update. (optional)

try:
    # Updates an existing occurrence.
    api_response = api_instance.grafeas_update_occurrence(name, body, update_mask=update_mask)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasApi->grafeas_update_occurrence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the occurrence. Should be of the form \&quot;projects/{project_id}/occurrences/{OCCURRENCE_ID}\&quot;. | 
 **body** | [**ApiOccurrence**](ApiOccurrence.md)| The updated occurrence. | 
 **update_mask** | [**list[str]**](str.md)| The fields to update. | [optional] 

### Return type

[**ApiOccurrence**](ApiOccurrence.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grafeas_update_operation**
> GooglelongrunningOperation grafeas_update_operation(name, body)

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
    api_response = api_instance.grafeas_update_operation(name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasApi->grafeas_update_operation: %s\n" % e)
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

