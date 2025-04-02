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

@mcp.tool()
async def cloud_pc_reboot(pc_id: str) -> str:
    """Reboot a Cloud PC with the given ID.

    Args:
        pc_id: Cloud PC ID
    """
    msw365_cloud_pc.reboot_cloud_pc(pc_id)
    return f"Request to reboot Cloud PC '{pc_id}' was submitted successfully."

@mcp.tool()
async def cloud_pc_rename(pc_id: str, new_name: str) -> str:
    """Set new display name for a Cloud PC with the given ID.

    Args:
        pc_id: Cloud PC ID
        new_name: New display name
    """
    msw365_cloud_pc.rename_cloud_pc(pc_id, new_name)
    return f"Request to rename Cloud PC '{pc_id}' to '{new_name}' was submitted successfully."

if __name__ == "__main__":
    # Initialize and run the MCP server
    mcp.run(transport='stdio')