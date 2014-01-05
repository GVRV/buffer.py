"""
Collection of configuration parameters for the 
Buffer client and API wrapper
"""

API_URL = "https://api.bufferapp.com/1/"

TYPES = {
    'GET': 'get',
    'POST': 'post'
}

OK_STATUS = {
    TYPES['GET']: [200],
    TYPES['POST']: [200, 201]
}