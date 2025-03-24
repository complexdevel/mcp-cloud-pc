# Cloud PC Management MCP Server

MCP Server for managing Azure Cloud PCs using the Microsoft Graph API.

### Features
TBD

## Tools
TBD

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
      ]
    }
  }
}
```

## License

This MCP server is licensed under the MIT License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License. For more details, please see the LICENSE file in the project repository.
