import getUserRepos
import APICall

username = input('Which user are you looking for?\n')
userRepos = f'/users/{username}/repos'

github_service_address = 'https://api.github.com'

address = github_service_address + userRepos

getUserRepos.printRepositories(address)