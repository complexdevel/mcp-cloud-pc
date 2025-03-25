import json
import msw365_cloud_pc
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp-cloud-pc")

@mcp.tool()
async def cloud_pc_list() -> str:
    """Get list of Cloud PCs available to the current tenant
    """
    pcs = msw365_cloud_pc.get_cloud_pc_list()
    return json.dumps(pcs)

if __name__ == "__main__":
    # Initialize and run the MCP server
    mcp.run(transport='stdio')