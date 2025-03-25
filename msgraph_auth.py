import requests
import os
import json

msgraph_tenant_id = os.getenv("MSGRAPH_TENANT_ID")
msgraph_client_id = os.getenv("MSGRAPH_CLIENT_ID")
msgraph_client_secret = os.getenv("MSGRAPH_CLIENT_SECRET")

if not msgraph_tenant_id or not msgraph_client_id or not msgraph_client_secret:
    raise Exception("MSGRAPH_TENANT_ID, MSGRAPH_CLIENT_ID, and MSGRAPH_CLIENT_SECRET must be set in the environment variables")


def msgraph_get_api_token():
    # Return Graph API access token

    url = f"https://login.microsoftonline.com/{msgraph_tenant_id}/oauth2/token?$select=id"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    fields = {
        "grant_type": "client_credentials",
        "client_id": msgraph_client_id,
        "client_secret": msgraph_client_secret,
        "scope": "CloudPC.ReadWrite.All",
        "resource": "https://graph.microsoft.com"
    }
    response = requests.post(url, headers=headers, data=fields)

    if response.status_code != requests.codes.ok: # 200:
        raise Exception(f"Failed to get token: {response.json()}")

    msgraph_access_token = response.json()["access_token"]

    return msgraph_access_token

