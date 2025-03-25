import msgraph_auth
import json
import subprocess


def get_cloud_pc_list():
    # Get list of Cloud PCs by using curl while Python msgraph-sdk API is being stabilizing 
    token = msgraph_auth.msgraph_get_api_token()

    res = subprocess.run(
        ["curl",
         "-H", "Authorization: Bearer " + token,
         "-H", "Content-Type: application/json",
         "-H", "Content-Length: 0",
         "-X", "GET",
         "-v", "https://graph.microsoft.com/v1.0/deviceManagement/virtualEndpoint/cloudPCs"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    response = res.stdout

    if res.returncode != 0:
        raise Exception(f"Failed to get list of Cloud PCs (err={res.returncode}): {response}")

    response_json = json.loads(response)
    pcs = response_json["value"]

    return pcs  # Return list of Cloud PCs in JSON format

