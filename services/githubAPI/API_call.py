import json
import requests

class API_call:
   # user = ''

    def __init__(self, user):
        self.user = user

    def setUserName(self, user):
        self.user = user
    
    def getUserName(self):
        return self.user

    def getMainURL(self):
        url = f'https://api.github.com/users/{self.user}'
        return url

    def getReposURL(self):
        url = f'https://api.github.com/users/{self.user}/repos'
        return url        

    def call(self, address):
        response = requests.get(address)
        print('Calling the API...\n')
        if response.status_code == 200: #Validating response status
            return response.json()
        else:
            return response.status_code

    def getRepositories(self):
        urlRepos = self.getReposURL()
        response = self.call(urlRepos)
        reposArray = []
        if type(response) != int:
            for repo in response: #The data is structured in repository objects into an array. This can also be written like: for n in range(len(response))   print(response[n]['name']):
                reposArray.append(repo['name']) #[{name: 'repo1', id: 1234}, {name: 'repo2', ...}, {name: 'repo3', ...}, ...]
        else:
            print(f'Something went wrong :( \n Code {response}')
        return reposArray

    def printRepositories(self):
        reposArray = self.getRepositories()
        if type(reposArray) != int:
            for repo in reposArray: #The data is structured in repository objects into an array. This can also be written like: for n in range(len(response))   print(response[n]['name]):
                print(repo) #[{name: 'repo1', id: 1234}, {name: 'repo2', ...}, {name: 'repo3', ...}, ...]
        else:
            print(reposArray)

    def getUserInfo(self):
        urlUser = self.getMainURL()
        response = self.call(urlUser)
        if type(response) != int: #Validating response status
            return response
        else:
            return f'Something went wrong :( \n Code {response}'

    def printUser(self):
        user = self.getUserInfo()
        print(
            f"""
                Name: {user['name']}
                Login: {user['login']}
                Bio: {user['bio']}
                Profile picture: {user['avatar_url']}
                Public Repositories: {user['public_repos']}
                No followers: {user['followers']}
                No following: {user['following']}
                User's blog: {user['blog']}
            """
        )

#Execução
def main():
    # Initializing object
    user = input('Insita o nome de perfil a ser pesquisado:  ')
    api = API_call(user)
    #userInfo = api.getUserInfo()
    #print(userInfo)
    #repos = api.printRepositories()
    api.printUser()

main()