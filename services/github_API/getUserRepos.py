import requests
import json
import APICall

def printRepositories(address):
    #Response with repositories data or an error code (int) whether something went wrong
    response = APICall.APICall(address)
    if type(response) != int:
        for repo in response: #The data is structured in repository objects into an array. This can also be written like: for n in range(len(response))   print(response[n]['name]):
            print(repo['name']) #[{name: 'repo1', id: 1234}, {name: 'repo2', ...}, {name: 'repo3', ...}, ...]
    else:
        print(f'Something went wrong :( \n Code {response}')

#We can use JSON Linters to better visualization of json content
#https://jsonlint.com/