import requests
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv("FRANCE_TRAVAIL_CLIENT_ID")
client_secret = os.getenv("FRANCE_TRAVAIL_CLIENT_SECRET")

url = "https://entreprise.francetravail.fr/connexion/oauth2/access_token?realm=%2Fpartenaire"

def get_access_token () -> str :
    
    #payload and Oauth2 credentials
    payload = {
        "grant_type" : "client_credentials",
        "client_id" : client_id,
        "client_secret" : client_secret,
        "scope" : "api_offresdemploiv2 o2dsoffre"
    }

    headers = {
        "content-type" : "application/x-www-form-urlencoded"
    }

    try:
        response = requests.post(url, data=payload, headers=headers)

         #raise an error if the request is failed
        response.raise_for_status()
        token_data = response.json()
        #Parse data json res
        return token_data.get("access_token")
    except requests.exceptions.RequestException as e :
        print(f'An error occured {e}')
        return None
    
token = get_access_token()

print(f'your token is {token}')

    