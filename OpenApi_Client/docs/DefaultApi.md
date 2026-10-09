# swagger_client.DefaultApi

All URIs are relative to *https://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**primes_post**](DefaultApi.md#primes_post) | **POST** /primes | 

# **primes_post**
> PrimeFactorization primes_post(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.InputNumbers() # InputNumbers | The numbers to be factorized (optional)

try:
    api_response = api_instance.primes_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->primes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InputNumbers**](InputNumbers.md)| The numbers to be factorized | [optional] 

### Return type

[**PrimeFactorization**](PrimeFactorization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

