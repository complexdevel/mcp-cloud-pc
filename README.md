# Cloud PC Management MCP Server

MCP Server for managing Azure Cloud PCs using the Microsoft Graph API.

### Features
The MCP server currently uses 'curl' to send Graph API requests, because Python msgraph-sdk documentation doesn't match the current sdk implementation.

## Tools
* `cloud_pc_list`
   - List all Cloud PCs available to the current tenant
   - Returns: List of Cloud PCs in JSON formated string
* `cloud_pc_reboot`
   - Reboot Cloud PCs with the given ID
   - Args: Cloud PC ID
* `cloud_pc_rename`
   - Set new display name for a Cloud PC with the given ID.
   - Arg: Cloud PC ID
   - Arg: New display name for the Cloud PC


### Usage with Claude Desktop
To use this with Claude Desktop, add the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "mcp-cloud-pc": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/ABSOLUTE/PATH/TO/PARENT/FOLDER/mcp-cloud-pc",
        "mcp-cloud-pc.py"
      ],
      "env": {
        "MSGRAPH_TENANT_ID": "<YOUR GRAPH API TENANT ID>",
        "MSGRAPH_CLIENT_ID": "<YOUR GRAPH API CLIENT ID>",
        "MSGRAPH_CLIENT_SECRET": "<YOUR GRAPH API CLIENT SECRET>"
      }
    }
  }
}
```

## License

This MCP server is licensed under the MIT License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License. For more details, please see the LICENSE file in the project repository.
