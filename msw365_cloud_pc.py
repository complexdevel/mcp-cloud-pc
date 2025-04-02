import msgraph_auth
import json
import subprocess


def get_cloud_pc_list():
    # Get list of Cloud PCs by using curl while Python msgraph-sdk API is being stabilizing 
    token = msgraph_auth.msgraph_get_api_token()

    res = subprocess.run(
        ["curl",
         f"https://graph.microsoft.com/v1.0/deviceManagement/virtualEndpoint/cloudPCs",
         "-H", "Authorization: Bearer " + token,
         "-H", "Content-Type: application/json",
         "-H", "Content-Length: 0",
         "-X", "GET",
         "-v"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    response = res.stdout

    if res.returncode != 0:
        raise Exception(f"Failed to get list of Cloud PCs (err={res.returncode}): {response}")

    response_json = json.loads(response)

    if "error" in response_json:
        err_code = response_json["error"]["code"]
        err_msg = response_json["error"]["message"]
        raise Exception(f"Failed to get list of Cloud PCs (err code:{err_code}, err msg:{err_msg})")

    pcs = response_json["value"]

    return pcs  # Return list of Cloud PCs in JSON format


def reboot_cloud_pc(pc_id):
    # Reboot Cloud PC with the give ID
    token = msgraph_auth.msgraph_get_api_token()

    res = subprocess.run(
        ["curl",
         f"https://graph.microsoft.com/v1.0/deviceManagement/virtualEndpoint/cloudPCs/{pc_id}/reboot",
         "-H", "Authorization: Bearer " + token,
         "-H", "Content-Type: application/json",
         "-H", "Content-Length: 0",
         "-X", "POST",
         "-v"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    response = res.stdout

    if res.returncode != 0:
        raise Exception(f"Failed to reboot Cloud PCs (err={res.returncode}): {response}")

    response_json = json.loads(response)

    if "error" in response_json:
        err_code = response_json["error"]["code"]
        err_msg = response_json["error"]["message"]
        raise Exception(f"Failed to reboot Cloud PCs (err code:{err_code}, err msg:{err_msg})")


def rename_cloud_pc(pc_id, new_name):
    # Rename display name of Cloud PC with the give ID
    token = msgraph_auth.msgraph_get_api_token()

    json_body = json.dumps({
        "displayName": new_name
    })

    res = subprocess.run(
        ["curl",
         f"https://graph.microsoft.com/v1.0/deviceManagement/virtualEndpoint/cloudPCs/{pc_id}/rename",
         "-H", "Authorization: Bearer " + token,
         "-H", "Content-Type: application/json",
         "-H", f"Content-Length: {len(json_body)}",
         "-d", json_body,
         "-X", "POST",
         "-v"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    response = res.stdout

    if res.returncode != 0:
        raise Exception(f"Failed to rename Cloud PCs (err={res.returncode}): {response}")

    response_json = json.loads(response)

    if "error" in response_json:
        err_code = response_json["error"]["code"]
        err_msg = response_json["error"]["message"]
        raise Exception(f"Failed to rename Cloud PCs (err code:{err_code}, err msg:{err_msg})")
