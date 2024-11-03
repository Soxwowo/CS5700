# Jitong Zou
# CS5700
# Homework 8 Salesforce OAuth 2-Python

import requests
import configparser
import json

# Read configuration file
config = configparser.ConfigParser()
config.read('salesforceconfig.ini')

# Retrieve OAuth2 information from the configuration file
grant_type = config.get('OAUTH', 'grant_type')
client_id = config.get('OAUTH', 'client_id')
client_secret = config.get('OAUTH', 'client_secret')
username = config.get('OAUTH', 'username')
password = config.get('OAUTH', 'password')
security_token = config.get('OAUTH', 'security_token')
base_url = config.get('OAUTH', 'base_url')

# Splicing passwords for authentication
full_password = password + security_token

with requests.Session() as session:
    # Request URL and data
    auth_url = f"{base_url}/services/oauth2/token"
    auth_data = {
        'grant_type': grant_type,
        'client_id': client_id,
        'client_secret': client_secret,
        'username': username,
        'password': full_password
    }

    try:
        # Request access token
        response = session.post(auth_url, data=auth_data)
        response.raise_for_status()
        access_token = response.json().get('access_token')

        # Set header information
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }

        # Request Account Data
        account_url = f"{base_url}/services/data/v55.0/query/?q=SELECT+NAME+,+ID+,+BillingAddress+FROM+ACCOUNT"
        account_response = session.get(account_url, headers=headers)
        account_response.raise_for_status()

        byte_stream = account_response.content
        print(byte_stream)
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"Error occurred: {err}")
