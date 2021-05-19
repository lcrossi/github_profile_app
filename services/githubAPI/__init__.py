import API_call

user = input('Insita o nome de perfil a ser pesquisado:  ')
api = API_call(user)
userInfo = api.getUser()
print(userInfo)
api.printRepositories()