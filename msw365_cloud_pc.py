import msgraph_auth
import json
import subprocess


def get_cloud_pc_list():
    # Get list of Cloud PCs by using curl while Python msgraph-sdk API is being stabilizing 
    token = msgraph_auth.msgraph_get_api_token()

    res = subprocess.run(
        ["curl",
         f"https://graph.microsoft.com/v1.0/deviceManagement/virtualEndpoint/cloudPCs",
         "-H", f"Authorization: Bearer {token}",
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
         "-H", f"Authorization: Bearer {token}",
         "-H", "Content-Type: application/json",
         "-H", "Content-Length: 0",
         "-X", "POST",
         "-v"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    response = res.stdout

    if res.returncode != 0:
        raise Exception(f"Failed to reboot Cloud PC (err={res.returncode}): {response}")

    response_json = json.loads(response)

    if "error" in response_json:
        err_code = response_json["error"]["code"]
        err_msg = response_json["error"]["message"]
        raise Exception(f"Failed to reboot Cloud PC (err code:{err_code}, err msg:{err_msg})")


def rename_cloud_pc(pc_id, new_name):
    # Rename display name of Cloud PC with the give ID
    token = msgraph_auth.msgraph_get_api_token()

    json_body = json.dumps({
        "displayName": new_name
    })

    res = subprocess.run(
        ["curl",
         f"https://graph.microsoft.com/v1.0/deviceManagement/virtualEndpoint/cloudPCs/{pc_id}/rename",
         "-H", f"Authorization: Bearer {token}",
         "-H", "Content-Type: application/json",
         "-H", f"Content-Length: {len(json_body)}",
         "-d", json_body,
         "-X", "POST",
         "-v"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    response = res.stdout

    if res.returncode != 0:
        raise Exception(f"Failed to rename Cloud PC (err={res.returncode}): {response}")

    if len(response) > 0:
        response_json = json.loads(response)

        if "error" in response_json:
            err_code = response_json["error"]["code"]
            err_msg = response_json["error"]["message"]
            raise Exception(f"Failed to rename Cloud PC (err code:{err_code}, err msg:{err_msg})")


def troubleshoot_cloud_pc(pc_id):
    # Troubleshoot Cloud PC with the give ID
    token = msgraph_auth.msgraph_get_api_token()

    res = subprocess.run(
        ["curl",
         f"https://graph.microsoft.com/v1.0/deviceManagement/virtualEndpoint/cloudPCs/{pc_id}/troubleshoot",
         "-H", f"Authorization: Bearer {token}",
         "-H", "Content-Type: application/json",
         "-H", "Content-Length: 0",
         "-X", "POST",
         "-v"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    response = res.stdout

    if res.returncode != 0:
        raise Exception(f"Failed to troubleshoot Cloud PC (err={res.returncode}): {response}")

    if len(response) > 0:
        response_json = json.loads(response)

        if "error" in response_json:
            err_code = response_json["error"]["code"]
            err_msg = response_json["error"]["message"]
            raise Exception(f"Failed to troubleshoot Cloud PC (err code:{err_code}, err msg:{err_msg})")


def end_cloud_pc_grace_period(pc_id):
    # End grace period of Cloud PC with the give ID
    token = msgraph_auth.msgraph_get_api_token()

    res = subprocess.run(
        ["curl",
         f"https://graph.microsoft.com/v1.0/deviceManagement/virtualEndpoint/cloudPCs/{pc_id}/endGracePeriod",
         "-H", f"Authorization: Bearer {token}",
         "-H", "Content-Type: application/json",
         "-H", "Content-Length: 0",
         "-X", "POST",
         "-v"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    response = res.stdout

    if res.returncode != 0:
        raise Exception(f"Failed to end grace period of Cloud PC (err={res.returncode}): {response}")

    if len(response) > 0:
        response_json = json.loads(response)

        if "error" in response_json:
            err_code = response_json["error"]["code"]
            err_msg = response_json["error"]["message"]
            raise Exception(f"Failed to end grace period of Cloud PC (err code:{err_code}, err msg:{err_msg})")


def get_cloud_pc_review_status(pc_id):
    # Get review status of the Cloud PC with the given ID.
    # TODO: retrieveReviewStatus GET request is available in Microsoft Graph beta only.
    # Need to replace it with the stable GET request when it will be available.
    token = msgraph_auth.msgraph_get_api_token()

    res = subprocess.run(
        ["curl",
         f"https://graph.microsoft.com/beta/deviceManagement/virtualEndpoint/cloudPCs/{pc_id}/retrieveReviewStatus",
         "-H", f"Authorization: Bearer {token}",
         "-H", "Content-Type: application/json",
         "-H", "Content-Length: 0",
         "-X", "GET",
         "-v"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    response = res.stdout

    if res.returncode != 0:
        raise Exception(f"Failed to retrieve review status for the Cloud PC {pc_id} (err={res.returncode}): {response}")

    response_json = json.loads(response)

    if "error" in response_json:
        err_code = response_json["error"]["code"]
        err_msg = response_json["error"]["message"]
        raise Exception(f"Failed to retrieve review status for the Cloud PC (err code:{err_code}, err msg:{err_msg})")

    del response_json["@odata.context"] # Remove @odata.context from the response to make it more readable

    return response_json  # Return review status in JSON format


def reprovision_cloud_pc_for_user(pc_id, user_type, os_version):
    # Reprovision the Cloud PC with the given ID for the user with the given type and Windows operating system version.
    # TODO: reprovision POST request is available in Microsoft Graph beta only.
    # Need to replace it with the stable POST request when it will be available.
    token = msgraph_auth.msgraph_get_api_token()

    # Validate user account type, use standardUser as default if invalid
    if user_type != "standardUser" and user_type != "administrator":
        user_type = "standardUser"

    # Validate Windows operating system version, use windows11 as default if invalid
    if os_version != "windows10" and os_version != "windows11":
        os_version = "windows11"

    json_body = json.dumps({
        "userAccountType": user_type,
        "osVersion": os_version
    })

    res = subprocess.run(
        ["curl",
         f"https://graph.microsoft.com/beta/deviceManagement/virtualEndpoint/cloudPCs/{pc_id}/reprovision",
         "-H", f"Authorization: Bearer {token}",
         "-H", "Content-Type: application/json",
         "-H", f"Content-Length: {len(json_body)}",
         "-d", json_body,
         "-X", "POST",
         "-v"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    response = res.stdout

    if res.returncode != 0:
        raise Exception(f"Failed to reprovision the Cloud PC {pc_id} (err={res.returncode}): {response}")

    if len(response) > 0:
        response_json = json.loads(response)

        if "error" in response_json:
            err_code = response_json["error"]["code"]
            err_msg = response_json["error"]["message"]
            raise Exception(f"Failed to reprovision the Cloud PC (err code:{err_code}, err msg:{err_msg})")
