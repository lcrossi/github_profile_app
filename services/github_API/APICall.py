import requests
import json

#not required in this case
key = ''

def APICall(address):
    request = requests.get(address)
    msg = ''
    print('Calling the API...\n')
    if request.status_code == 200: #Validating response status
        msg = request.json()
        return request.json()
        
    else:
        msg = request.status_code
        return request.status_code 

# Raise an exception if the call returns an error code
#response.raise_for_status()

# Display the JSON results returned
#results = response.json()
#print(json.dumps(results))
