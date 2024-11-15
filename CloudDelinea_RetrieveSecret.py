import requests
from getpass import getpass


# Global Variables
site = 'https://EXAMPLE.secretservercloud.com'
slug_number = '1234'


def GetToken():
    # Authenticate | Valid for 20 minutes
    username = input("Enter username: ")
    password = getpass()

    api_path = '/oauth2/token'

    # data
    auth_cred = {
        "grant_type": "password",
        "username": username,
        "password": password,
    }
    headers = {'content-type':'application/x-www-form-urlencoded'}
    try:
        resp = requests.post(site + api_path, headers=headers, data=auth_cred)
        if resp.status_code == 200:
            response = resp.json()
            token = response["access_token"]
            #refresh_token = response["refresh_token"]
            return token
        else:
            print(resp.status_code)
            print(resp.json())
            return token
    
    except Exception as error:
        print(f"Error: {error}")

# REST call to retrieve a secret by ID
def GetSecret(token, secretId):
    try:
        api_path = '/api/v2/secrets/'
        headers = {'Authorization':'Bearer ' + token, 'content-type':'application/json'}
        resp = requests.get(site + api_path + str(secretId), headers=headers)    
        response = resp.json()
        client_url = response["items"][0]["itemValue"]
        client_username = response["items"][1]["itemValue"]
        client_password = response["items"][2]["itemValue"]
        return client_url, client_username, client_password
    except Exception as error:
        print(f"Error: {error}")
        return None

token = GetToken()

# Results

client_url, client_username, client_password = GetSecret(token,slug_number)
print("Retrieved Information")
print(client_url)
print(client_username)
print(client_password)

