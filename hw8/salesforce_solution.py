import requests
import json
import configparser

def get_salesforce_access_token(config):
    # 从配置文件中获取OAuth2认证信息
    grant_type = config.get('OAUTH', 'grant_type')
    client_id = config.get('OAUTH', 'client_id')
    client_secret = config.get('OAUTH', 'client_secret')
    username = config.get('OAUTH', 'username')
    password = config.get('OAUTH', 'password')
    security_token = config.get('OAUTH', 'security_token')
    base_url = config.get('OAUTH', 'base_url')

    # OAuth2令牌请求的URL
    token_url = f"{base_url}/services/oauth2/token"

    # 请求的负载
    payload = {
        'grant_type': grant_type,
        'client_id': client_id,
        'client_secret': client_secret,
        'username': username,
        'password': password + security_token
    }

    # 发送POST请求以获取访问令牌
    response = requests.post(token_url, data=payload)

    if response.status_code == 200:
        # 返回令牌
        return response.json().get('access_token')
    else:
        print("Failed to obtain access token:", response.text)
        return None

def get_salesforce_accounts(config, access_token):
    base_url = config.get('OAUTH', 'base_url')
    # 查询Account数据的URL
    query_url = f"{base_url}/services/data/v55.0/query/?q=SELECT+NAME,+ID,+BillingAddress+FROM+ACCOUNT"

    # 请求头，使用获取的access token
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    # 发送GET请求以获取Account数据
    response = requests.get(query_url, headers=headers)

    if response.status_code == 200:
        # 返回字节流
        return response.content
    else:
        print("Failed to retrieve account data:", response.text)
        return None

def main():
    # 读取配置文件
    config = configparser.ConfigParser()
    config.read('salesforceconfig.ini')

    # 获取Salesforce的访问令牌
    access_token = get_salesforce_access_token(config)

    if access_token:
        # 使用访问令牌获取Account数据
        account_data = get_salesforce_accounts(config, access_token)

        if account_data:
            # 打印返回的Account数据（字节流形式）
            print(account_data)

if __name__ == "__main__":
    main()
