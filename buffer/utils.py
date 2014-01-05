import json
import requests

from functools import wraps

from .config import API_URL, OK_STATUS, TYPES
from .exceptions import ApiResponseException, ApiValidationException, ApiInvalidRequestException

def api_endpoint(req_type, url):
    def api_endpoint_decorator(func):
        @wraps(func)
        def inner(self, **kwargs):
            # Make sure the type of the request is supported
            if req_type not in TYPES.values():
                raise ApiInvalidRequestException()

            # Make the request with the URL provided
            endpoint_url = "%s%s" % (API_URL, url)

            # Validate the data, if provided
            params = kwargs.pop('data', {})
            validator = kwargs.pop('validator', None)
            
            if params and validator and type(validator) == 'function':
                validation = validator(params)

                if validation['ACK'] == False:
                    raise ApiValidationException(validation)

            # Update the data with the access token
            params.update({ 'access_token': self.access_token })

            # Make the request
            request_type = getattr(requests, req_type)
            response = request_type(
                endpoint_url,
                params=params
                )

            # Check if status is what is expected
            if response.status_code not in OK_STATUS[req_type]:
                raise ApiResponseException(response)

            # Try to parse the response from the API 
            data = JsonObject(json.loads(response.content))

            # Call the wrapped function 
            response = func(self, data, **kwargs)
            
            return response if response else data
        return inner
    return api_endpoint_decorator
            
def args_to_kwargs(*args):
    def args_to_kwargs_decorator(func):
        @wraps(func)
        def inner(self, *inner_args, **kwargs):
            kwargs.update(dict(map(None, args, inner_args)))
            return func(self, **kwargs)
        return inner
    return args_to_kwargs_decorator


class JsonObject(dict):
    '''
    general json object that can bind any fields but also act as a dict.
    '''
    def __getattr__(self, attr):
        return self[attr]

    def __setattr__(self, attr, value):
        self[attr] = value

    def __getstate__(self):
        return self.copy()

    def __setstate__(self, state):
        self.update(state)