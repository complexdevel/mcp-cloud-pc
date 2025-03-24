from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp-cloud-pc")

if __name__ == "__main__":
    # Initialize and run the MCP server
    mcp.run(transport='stdio')