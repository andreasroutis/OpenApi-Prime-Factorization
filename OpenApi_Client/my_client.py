from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import sys
import json

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient())
body = swagger_client.InputNumbers([int(n) for n in sys.argv[1:]]) # InputNumbers | The numbers to be factorized (optional)
pprint(body)

try:
    api_response = api_instance.primes_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->primes_post: %s\n" % e)
    print(json.loads(e.body)['detail'])