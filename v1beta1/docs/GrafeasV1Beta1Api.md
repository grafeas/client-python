# swagger_client.GrafeasV1Beta1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_create_notes**](GrafeasV1Beta1Api.md#batch_create_notes) | **POST** /v1beta1/{parent&#x3D;projects/*}/notes:batchCreate | Creates new notes in batch.
[**batch_create_occurrences**](GrafeasV1Beta1Api.md#batch_create_occurrences) | **POST** /v1beta1/{parent&#x3D;projects/*}/occurrences:batchCreate | Creates new occurrences in batch.
[**create_note**](GrafeasV1Beta1Api.md#create_note) | **POST** /v1beta1/{parent&#x3D;projects/*}/notes | Creates a new note.
[**create_occurrence**](GrafeasV1Beta1Api.md#create_occurrence) | **POST** /v1beta1/{parent&#x3D;projects/*}/occurrences | Creates a new occurrence.
[**delete_note**](GrafeasV1Beta1Api.md#delete_note) | **DELETE** /v1beta1/{name&#x3D;projects/*/notes/*} | Deletes the specified note.
[**delete_occurrence**](GrafeasV1Beta1Api.md#delete_occurrence) | **DELETE** /v1beta1/{name&#x3D;projects/*/occurrences/*} | Deletes the specified occurrence. For example, use this method to delete an occurrence when the occurrence is no longer applicable for the given resource.
[**get_note**](GrafeasV1Beta1Api.md#get_note) | **GET** /v1beta1/{name&#x3D;projects/*/notes/*} | Gets the specified note.
[**get_occurrence**](GrafeasV1Beta1Api.md#get_occurrence) | **GET** /v1beta1/{name&#x3D;projects/*/occurrences/*} | Gets the specified occurrence.
[**get_occurrence_note**](GrafeasV1Beta1Api.md#get_occurrence_note) | **GET** /v1beta1/{name&#x3D;projects/*/occurrences/*}/notes | Gets the note attached to the specified occurrence. Consumer projects can use this method to get a note that belongs to a provider project.
[**get_vulnerability_occurrences_summary**](GrafeasV1Beta1Api.md#get_vulnerability_occurrences_summary) | **GET** /v1beta1/{parent&#x3D;projects/*}/occurrences:vulnerabilitySummary | Gets a summary of the number and severity of occurrences.
[**list_note_occurrences**](GrafeasV1Beta1Api.md#list_note_occurrences) | **GET** /v1beta1/{name&#x3D;projects/*/notes/*}/occurrences | Lists occurrences referencing the specified note. Provider projects can use this method to get all occurrences across consumer projects referencing the specified note.
[**list_notes**](GrafeasV1Beta1Api.md#list_notes) | **GET** /v1beta1/{parent&#x3D;projects/*}/notes | Lists notes for the specified project.
[**list_occurrences**](GrafeasV1Beta1Api.md#list_occurrences) | **GET** /v1beta1/{parent&#x3D;projects/*}/occurrences | Lists occurrences for the specified project.
[**update_note**](GrafeasV1Beta1Api.md#update_note) | **PATCH** /v1beta1/{name&#x3D;projects/*/notes/*} | Updates the specified note.
[**update_occurrence**](GrafeasV1Beta1Api.md#update_occurrence) | **PATCH** /v1beta1/{name&#x3D;projects/*/occurrences/*} | Updates the specified occurrence.


# **batch_create_notes**
> V1beta1BatchCreateNotesResponse batch_create_notes(parent, body)

Creates new notes in batch.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GrafeasV1Beta1Api()
parent = 'parent_example' # str | The name of the project in the form of `projects/[PROJECT_ID]`, under which the notes are to be created.
body = swagger_client.V1beta1BatchCreateNotesRequest() # V1beta1BatchCreateNotesRequest | 

try:
    # Creates new notes in batch.
    api_response = api_instance.batch_create_notes(parent, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasV1Beta1Api->batch_create_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| The name of the project in the form of &#x60;projects/[PROJECT_ID]&#x60;, under which the notes are to be created. | 
 **body** | [**V1beta1BatchCreateNotesRequest**](V1beta1BatchCreateNotesRequest.md)|  | 

### Return type

[**V1beta1BatchCreateNotesResponse**](V1beta1BatchCreateNotesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_create_occurrences**
> V1beta1BatchCreateOccurrencesResponse batch_create_occurrences(parent, body)

Creates new occurrences in batch.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GrafeasV1Beta1Api()
parent = 'parent_example' # str | The name of the project in the form of `projects/[PROJECT_ID]`, under which the occurrences are to be created.
body = swagger_client.V1beta1BatchCreateOccurrencesRequest() # V1beta1BatchCreateOccurrencesRequest | 

try:
    # Creates new occurrences in batch.
    api_response = api_instance.batch_create_occurrences(parent, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasV1Beta1Api->batch_create_occurrences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| The name of the project in the form of &#x60;projects/[PROJECT_ID]&#x60;, under which the occurrences are to be created. | 
 **body** | [**V1beta1BatchCreateOccurrencesRequest**](V1beta1BatchCreateOccurrencesRequest.md)|  | 

### Return type

[**V1beta1BatchCreateOccurrencesResponse**](V1beta1BatchCreateOccurrencesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_note**
> V1beta1Note create_note(parent, body)

Creates a new note.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GrafeasV1Beta1Api()
parent = 'parent_example' # str | The name of the project in the form of `projects/[PROJECT_ID]`, under which the note is to be created.
body = swagger_client.V1beta1Note() # V1beta1Note | The note to create.

try:
    # Creates a new note.
    api_response = api_instance.create_note(parent, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasV1Beta1Api->create_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| The name of the project in the form of &#x60;projects/[PROJECT_ID]&#x60;, under which the note is to be created. | 
 **body** | [**V1beta1Note**](V1beta1Note.md)| The note to create. | 

### Return type

[**V1beta1Note**](V1beta1Note.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_occurrence**
> V1beta1Occurrence create_occurrence(parent, body)

Creates a new occurrence.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GrafeasV1Beta1Api()
parent = 'parent_example' # str | The name of the project in the form of `projects/[PROJECT_ID]`, under which the occurrence is to be created.
body = swagger_client.V1beta1Occurrence() # V1beta1Occurrence | The occurrence to create.

try:
    # Creates a new occurrence.
    api_response = api_instance.create_occurrence(parent, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasV1Beta1Api->create_occurrence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| The name of the project in the form of &#x60;projects/[PROJECT_ID]&#x60;, under which the occurrence is to be created. | 
 **body** | [**V1beta1Occurrence**](V1beta1Occurrence.md)| The occurrence to create. | 

### Return type

[**V1beta1Occurrence**](V1beta1Occurrence.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_note**
> object delete_note(name)

Deletes the specified note.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GrafeasV1Beta1Api()
name = 'name_example' # str | The name of the note in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`.

try:
    # Deletes the specified note.
    api_response = api_instance.delete_note(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasV1Beta1Api->delete_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the note in the form of &#x60;projects/[PROVIDER_ID]/notes/[NOTE_ID]&#x60;. | 

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

Deletes the specified occurrence. For example, use this method to delete an occurrence when the occurrence is no longer applicable for the given resource.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GrafeasV1Beta1Api()
name = 'name_example' # str | The name of the occurrence in the form of `projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]`.

try:
    # Deletes the specified occurrence. For example, use this method to delete an occurrence when the occurrence is no longer applicable for the given resource.
    api_response = api_instance.delete_occurrence(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasV1Beta1Api->delete_occurrence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the occurrence in the form of &#x60;projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]&#x60;. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_note**
> V1beta1Note get_note(name)

Gets the specified note.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GrafeasV1Beta1Api()
name = 'name_example' # str | The name of the note in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`.

try:
    # Gets the specified note.
    api_response = api_instance.get_note(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasV1Beta1Api->get_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the note in the form of &#x60;projects/[PROVIDER_ID]/notes/[NOTE_ID]&#x60;. | 

### Return type

[**V1beta1Note**](V1beta1Note.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_occurrence**
> V1beta1Occurrence get_occurrence(name)

Gets the specified occurrence.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GrafeasV1Beta1Api()
name = 'name_example' # str | The name of the occurrence in the form of `projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]`.

try:
    # Gets the specified occurrence.
    api_response = api_instance.get_occurrence(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasV1Beta1Api->get_occurrence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the occurrence in the form of &#x60;projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]&#x60;. | 

### Return type

[**V1beta1Occurrence**](V1beta1Occurrence.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_occurrence_note**
> V1beta1Note get_occurrence_note(name)

Gets the note attached to the specified occurrence. Consumer projects can use this method to get a note that belongs to a provider project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GrafeasV1Beta1Api()
name = 'name_example' # str | The name of the occurrence in the form of `projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]`.

try:
    # Gets the note attached to the specified occurrence. Consumer projects can use this method to get a note that belongs to a provider project.
    api_response = api_instance.get_occurrence_note(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasV1Beta1Api->get_occurrence_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the occurrence in the form of &#x60;projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]&#x60;. | 

### Return type

[**V1beta1Note**](V1beta1Note.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vulnerability_occurrences_summary**
> V1beta1VulnerabilityOccurrencesSummary get_vulnerability_occurrences_summary(parent, filter=filter)

Gets a summary of the number and severity of occurrences.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GrafeasV1Beta1Api()
parent = 'parent_example' # str | The name of the project to get a vulnerability summary for in the form of `projects/[PROJECT_ID]`.
filter = 'filter_example' # str | The filter expression. (optional)

try:
    # Gets a summary of the number and severity of occurrences.
    api_response = api_instance.get_vulnerability_occurrences_summary(parent, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasV1Beta1Api->get_vulnerability_occurrences_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| The name of the project to get a vulnerability summary for in the form of &#x60;projects/[PROJECT_ID]&#x60;. | 
 **filter** | **str**| The filter expression. | [optional] 

### Return type

[**V1beta1VulnerabilityOccurrencesSummary**](V1beta1VulnerabilityOccurrencesSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_note_occurrences**
> V1beta1ListNoteOccurrencesResponse list_note_occurrences(name, filter=filter, page_size=page_size, page_token=page_token)

Lists occurrences referencing the specified note. Provider projects can use this method to get all occurrences across consumer projects referencing the specified note.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GrafeasV1Beta1Api()
name = 'name_example' # str | The name of the note to list occurrences for in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`.
filter = 'filter_example' # str | The filter expression. (optional)
page_size = 56 # int | Number of occurrences to return in the list. (optional)
page_token = 'page_token_example' # str | Token to provide to skip to a particular spot in the list. (optional)

try:
    # Lists occurrences referencing the specified note. Provider projects can use this method to get all occurrences across consumer projects referencing the specified note.
    api_response = api_instance.list_note_occurrences(name, filter=filter, page_size=page_size, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasV1Beta1Api->list_note_occurrences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the note to list occurrences for in the form of &#x60;projects/[PROVIDER_ID]/notes/[NOTE_ID]&#x60;. | 
 **filter** | **str**| The filter expression. | [optional] 
 **page_size** | **int**| Number of occurrences to return in the list. | [optional] 
 **page_token** | **str**| Token to provide to skip to a particular spot in the list. | [optional] 

### Return type

[**V1beta1ListNoteOccurrencesResponse**](V1beta1ListNoteOccurrencesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_notes**
> V1beta1ListNotesResponse list_notes(parent, filter=filter, page_size=page_size, page_token=page_token)

Lists notes for the specified project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GrafeasV1Beta1Api()
parent = 'parent_example' # str | The name of the project to list notes for in the form of `projects/[PROJECT_ID]`.
filter = 'filter_example' # str | The filter expression. (optional)
page_size = 56 # int | Number of notes to return in the list. Must be positive. Max allowed page size is 1000. If not specified, page size defaults to 20. (optional)
page_token = 'page_token_example' # str | Token to provide to skip to a particular spot in the list. (optional)

try:
    # Lists notes for the specified project.
    api_response = api_instance.list_notes(parent, filter=filter, page_size=page_size, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasV1Beta1Api->list_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| The name of the project to list notes for in the form of &#x60;projects/[PROJECT_ID]&#x60;. | 
 **filter** | **str**| The filter expression. | [optional] 
 **page_size** | **int**| Number of notes to return in the list. Must be positive. Max allowed page size is 1000. If not specified, page size defaults to 20. | [optional] 
 **page_token** | **str**| Token to provide to skip to a particular spot in the list. | [optional] 

### Return type

[**V1beta1ListNotesResponse**](V1beta1ListNotesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_occurrences**
> V1beta1ListOccurrencesResponse list_occurrences(parent, filter=filter, page_size=page_size, page_token=page_token)

Lists occurrences for the specified project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GrafeasV1Beta1Api()
parent = 'parent_example' # str | The name of the project to list occurrences for in the form of `projects/[PROJECT_ID]`.
filter = 'filter_example' # str | The filter expression. (optional)
page_size = 56 # int | Number of occurrences to return in the list. Must be positive. Max allowed page size is 1000. If not specified, page size defaults to 20. (optional)
page_token = 'page_token_example' # str | Token to provide to skip to a particular spot in the list. (optional)

try:
    # Lists occurrences for the specified project.
    api_response = api_instance.list_occurrences(parent, filter=filter, page_size=page_size, page_token=page_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasV1Beta1Api->list_occurrences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| The name of the project to list occurrences for in the form of &#x60;projects/[PROJECT_ID]&#x60;. | 
 **filter** | **str**| The filter expression. | [optional] 
 **page_size** | **int**| Number of occurrences to return in the list. Must be positive. Max allowed page size is 1000. If not specified, page size defaults to 20. | [optional] 
 **page_token** | **str**| Token to provide to skip to a particular spot in the list. | [optional] 

### Return type

[**V1beta1ListOccurrencesResponse**](V1beta1ListOccurrencesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_note**
> V1beta1Note update_note(name, body)

Updates the specified note.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GrafeasV1Beta1Api()
name = 'name_example' # str | The name of the note in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`.
body = swagger_client.V1beta1Note() # V1beta1Note | The updated note.

try:
    # Updates the specified note.
    api_response = api_instance.update_note(name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasV1Beta1Api->update_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the note in the form of &#x60;projects/[PROVIDER_ID]/notes/[NOTE_ID]&#x60;. | 
 **body** | [**V1beta1Note**](V1beta1Note.md)| The updated note. | 

### Return type

[**V1beta1Note**](V1beta1Note.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_occurrence**
> V1beta1Occurrence update_occurrence(name, body)

Updates the specified occurrence.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GrafeasV1Beta1Api()
name = 'name_example' # str | The name of the occurrence in the form of `projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]`.
body = swagger_client.V1beta1Occurrence() # V1beta1Occurrence | The updated occurrence.

try:
    # Updates the specified occurrence.
    api_response = api_instance.update_occurrence(name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrafeasV1Beta1Api->update_occurrence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the occurrence in the form of &#x60;projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]&#x60;. | 
 **body** | [**V1beta1Occurrence**](V1beta1Occurrence.md)| The updated occurrence. | 

### Return type

[**V1beta1Occurrence**](V1beta1Occurrence.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

